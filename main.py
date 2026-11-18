import os
import time
from pathlib import Path
import soundfile as sf
import torch
import tiny_voca.infer as tts  # pyright: ignore

os.environ["DIZIONE_DATA"] = "tiny-voca/phonemizer"
os.makedirs("outputs", exist_ok=True)

# 1. Load Model
t0 = time.perf_counter()
model = tts.load_model("tiny-voca/tiny-voca.pt", device="cpu", check_frontend=False)
load_t = time.perf_counter() - t0

# 2. Task 1: Short Video Hook
text1 = Path("inputs/short_hook.txt").read_text(encoding="utf-8").strip()
t1 = time.perf_counter()
w1, _ = tts.speak_text(model, text1, voice="M2", speed=1.1)
c1 = time.perf_counter() - t1
sf.write("outputs/short_hook.wav", w1.numpy(), 24000)

# 3. Task 2: Dialogue (Parse [F2]/[M2] tags, synthesize turns & merge with pause)
t2 = time.perf_counter()
w2_list, pause = [], torch.zeros(int(24000 * 0.3))
for line in Path("inputs/dialogue.txt").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    voice = "M2" if "[M2]" in line else "F2"
    clean = line.replace("[F2]", "").replace("[M2]", "").strip()
    w, _ = tts.speak_text(model, clean, voice=voice)
    w2_list.extend([w, pause])
w2 = torch.cat(w2_list)
c2 = time.perf_counter() - t2
sf.write("outputs/dialogue.wav", w2.numpy(), 24000)

# 4. Task 3: 5-Second Speed Benchmark
text3 = Path("inputs/speed_test.txt").read_text(encoding="utf-8").strip()
sentences = [s.strip() for s in text3.split(".") if s.strip()]
t3 = time.perf_counter()
w3_list, idx = [], 0
while time.perf_counter() - t3 < 5.0:
    w, _ = tts.speak_text(model, sentences[idx % len(sentences)], voice="M2")
    w3_list.append(w)
    idx += 1
c3 = time.perf_counter() - t3
w3 = torch.cat(w3_list)
sf.write("outputs/speed_benchmark.wav", w3.numpy(), 24000)

# 5. Simple Markdown Report with Basic Stats
d1, d2, d3 = len(w1) / 24000, len(w2) / 24000, len(w3) / 24000
report = f"""# ⚡ tiny-voca Speed Benchmark

- **Model Load Time:** {load_t:.2f}s
- **Sample Rate:** 24,000 Hz Mono WAV
- **Official Target:** ~70x Real-Time (4 CPU Threads)

| Task | Audio Length | Time Taken | Speed Multiplier |
| :--- | :--- | :--- | :--- |
| **Short Video Hook** | {d1:.2f}s | {c1:.2f}s | **{d1/c1:.1f}x real-time** |
| **Podcast Dialogue** | {d2:.2f}s | {c2:.2f}s | **{d2/c2:.1f}x real-time** |
| **5s Speed Stress Test** | {d3:.2f}s | {c3:.2f}s | **{d3/c3:.1f}x real-time** |
"""
Path("outputs/speed_report.md").write_text(report, encoding="utf-8")
print(f"Done! Created 3 audio files and outputs/speed_report.md in {c1+c2+c3:.2f}s compute.")

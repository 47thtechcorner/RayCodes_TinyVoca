<div align="center">
  <a href="https://youtu.be/i5aBTc8Fzhg">
    <img src="https://img.youtube.com/vi/i5aBTc8Fzhg/0.jpg" alt="This 4.5MB TTS AI Destroys 2B Giants 70x Faster on CPU! (Tiny-Voca)">
  </a>
  <h3>📺 <a href="https://youtu.be/i5aBTc8Fzhg">Watch the full tutorial on YouTube</a></h3>
</div>

# 🎙️ tiny-voca Local Voiceover Pipeline

A ultra-lightweight, 70x real-time Text-to-Speech (TTS) voice generation tool powered by **tiny-voca** (`n4ze3m/tiny-voca`). Distilled from Alibaba's Qwen3-TTS 1.7B, it synthesizes studio-grade 24 kHz English audio in female (F2) and male (M2) voices completely offline on CPU with zero cloud fees.

> *"A 4.5-million-parameter speech synthesis engine trained for under $10 that outperforms 100M-parameter models and 2-billion-parameter giants on the Open TTS Leaderboard."*

---

## 📊 Production Test Workflows

| Workflow | Capability Tested | Input Artifact | Expected Deliverable |
| :--- | :--- | :--- | :--- |
| **High-Energy Social Hook** | Synthesizes rapid speech at accelerated pace with zero clipping | Punchy short-form script hook for mobile video feeds | Crisp 24 kHz high-energy male narration track |
| **Dual-Host Podcast Dialogue** | Alternates between male and female voices with natural turn pauses | Conversational interview script with distinct speaker tags | Seamless two-character podcast dialogue with clean transitions |
| **5s CPU Speed Stress Test** | Measures continuous throughput and real-time multiplier within a 5-second compute window | Dense multi-sentence passage testing continuous synthesis | Continuous 3-minute audio track with executive performance report |

---

## ⚡ Tech Stack

- **Core Engine:** `tiny-voca` (4.53M parameter neural voice synthesizer)
- **Architecture:** 4-block transformer encoder + FastSpeech 2 duration predictor + source-filter waveform synthesizer
- **Knowledge Distillation:** Pre-trained on 17.6 hours of synthetic speech from Alibaba Qwen3-TTS 1.7B
- **Runtime:** Native Python `tiny_voca` CPU inference engine
- **Phonemizer:** `dizione` (CMU Pronouncing Dictionary)
- **Audio Output:** 24,000 Hz 16-bit Mono PCM WAV

---

## 🚀 Quickstart Guide (Windows PowerShell)

### Step 1: Install Dependencies, Fetch Weights & Set Environment

Run the following command to install the official packages, download model weights from Hugging Face, and set the phonemizer path in one clean block:

```powershell
pip install torch soundfile numpy huggingface_hub git+https://github.com/n4ze3m/dizione git+https://github.com/n4ze3m/tiny-voca
hf download n4ze3m/tiny-voca --local-dir tiny-voca
$env:DIZIONE_DATA = "tiny-voca/phonemizer"
```

### Step 2: Run Production Voiceover Pipeline

Execute the main script to process input scripts and synthesize 24 kHz WAV voiceover files:

```powershell
python main.py
```

---

## 📂 Repository Structure

```text
RayCodes_TinyVoca/
├── inputs/
│   ├── dialogue.txt
│   ├── short_hook.txt
│   └── speed_test.txt
├── outputs/
│   ├── dialogue.wav
│   ├── short_hook.wav
│   ├── speed_benchmark.wav
│   └── speed_report.md
├── main.py
└── README.md
```

---

## 📝 Script Breakdown

- **`main.py`**: Core production pipeline. Invokes `tiny_voca.infer` directly on CPU, manages multi-speaker dialogue sequencing, executes a 5-second throughput stress test, and generates the markdown performance report in `outputs/speed_report.md`.
- **`inputs/short_hook.txt`**: Plain text high-energy hook for automated video narration.
- **`inputs/dialogue.txt`**: Dual-speaker script tagged with `[F2]` and `[M2]` speaker markers.
- **`inputs/speed_test.txt`**: Dense multi-sentence technical passage used for the 5-second CPU speed benchmark.

---

## 🎯 5 Core Use Cases

- ⚡ **Zero-Latency Voice Assistants:** Pair local Ollama LLMs and Whisper STT with tiny-voca for sub-200ms spoken conversational loops on basic laptops.
- 🎙️ **Automated Video Voiceovers:** Batch-generate narration tracks for YouTube Shorts, Reels, and TikToks at 70x real-time speeds.
- 👥 **Multi-Speaker Podcasts & Audiobooks:** Convert Markdown scripts into multi-character audio plays using dynamic F2 and M2 voice tags.
- 🛡️ **Offline Desktop Accessibility:** Provide fast, private screen-reading for local applications without internet or telemetry.
- 📊 **Developer Terminal Alerts:** Trigger spoken audio notifications for build completions, deployment alerts, and CI/CD events.

---

## 🔮 Future Feature Roadmap

- 🎛️ **Interactive Web UI:** Launch a local Streamlit or Gradio dashboard with live sliders for pitch, speed, and audio playback.
- 📜 **Synchronized Subtitles:** Auto-generate word-level `.srt` and `.vtt` caption files from phoneme frame durations.
- 🌍 **Extended Multilingual Phonemization:** Expand lexical coverage for accented terms, scientific acronyms, and homographs.
- 🔄 **OpenAI-Compatible TTS Server:** Wrap the ONNX engine in a lightweight FastAPI server exposing `/v1/audio/speech`.
- 🎧 **WebAssembly Browser Player:** Package `onnxruntime-web` for zero-install client-side speech generation inside web browsers.

---

## 🏷️ Keywords & SEO

`tiny voca` • `tinyvoca tts` • `qwen3 tts` • `qwen voice` • `alibaba tts` • `local tts` • `offline tts` • `ai voice` • `python tts` • `open tts` • `fast tts` • `local assistant` • `english tts` • `tts engine` • `onnx runtime` • `ai audio` • `lightweight ai` • `free tts` • `voice engine` • `elevenlabs alternative` • `tiny-voca` • `tiny TTS` • `small TTS` • `text to speech` • `Alibaba TTS` • `Qwen3 voice` • `Qwen3 distilled` • `Qwen3 TTS model` • `Alibaba AI` • `Qwen3 1.7B` • `CPU voice AI` • `lightweight TTS` • `Pocket TTS` • `Piper TTS` • `local TTS` • `Kokoro TTS`


# Vid2TXT 🎬➡️📝

[![Language](https://img.shields.io/badge/Language-Python%20%7C%20Jupyter-blue)](https://github.com/aeleraqi/Vid2TXT)
[![Stars](https://img.shields.io/github/stars/aeleraqi/Vid2TXT?style=social)](https://github.com/aeleraqi/Vid2TXT/stargazers)

A Python project for extracting text from video content — convert spoken words in any video into structured, searchable text.

## 📖 About

**Vid2TXT** uses speech recognition and audio processing to automatically transcribe video content. Ideal for researchers, journalists, content creators, and educators.

## ✨ Features

- Automatic audio extraction from video files
- Speech-to-text transcription
- Support for multiple video formats (MP4, AVI, MOV, MKV)
- Timestamped output for precise reference
- Export to TXT, CSV, or JSON

## 🚀 Getting Started

```bash
git clone https://github.com/aeleraqi/Vid2TXT.git
cd Vid2TXT
pip install -r requirements.txt
jupyter notebook Vid2TXT.ipynb
```

## 💡 Usage

```python
transcript = transcribe_video("my_video.mp4", language="en-US")
print(transcript)
```

## 🧰 Requirements

- Python 3.8+
- moviepy, SpeechRecognition, pydub, ffmpeg

---
**Author:** [Amr Eleraqi](https://github.com/aeleraqi) — Data Analyst | NLP Specialist | Machine Learning Expert | Educator  
**Affiliation:** Toronto Metropolitan University, Ontario, Canada  
[![ORCID](https://img.shields.io/badge/ORCID-0000--0003--0935--0026-brightgreen)](https://orcid.org/0000-0003-0935-0026) [![GitHub](https://img.shields.io/github/followers/aeleraqi?label=Follow&style=social)](https://github.com/aeleraqi)

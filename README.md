<!-- ---
title: Pixel GArt
emoji: 🌖
colorFrom: red
colorTo: indigo
sdk: gradio
sdk_version: 5.35.0
app_file: app.py
pinned: false
license: mit
short_description: AI tool for turning sketches into pixel art.
--- -->

---
title: Pixel GArt
emoji: 🌖
colorFrom: red
colorTo: indigo
sdk: gradio
sdk_version: 5.35.0
app_file: app.py
pinned: false
license: mit
short_description: AI tool for turning sketches into pixel art.
---

# 🎨 Pixel Art Generator

An AI-based pixel art generator that transforms hand-drawn sketches into pixel-style artworks.

> 🚀 This project uses `Gradio==3.44.4`. Please use this specific version to avoid compatibility issues.

---

## 🌟 Features

- Convert hand‑drawn sketches into pixel‑style images  
- Optional text prompt to guide the generation  
- Real‑time generation progress display  
- Simple and intuitive web UI (built with Gradio)  

---

## 📦 Installation

```bash
git clone [your‑repo‑url]
cd Pixel_GArt
conda create -n pixel_venv python=3.12
conda activate pixel_venv
pip install gradio==3.44.4
pip install -r requirements.txt
pip install torch torchvision opencv-python pillow
pip install git+https://github.com/facebookresearch/segment-anything.git
🛠️ Usage
Upload or draw a sketch

(Optional) Enter a text description

Click the generate button

Wait for the pixel art to appear 🎉

💻 System Requirements
Python 3.10 or 3.12

Conda (recommended)

8 GB RAM or more

Modern browser (Chrome / Firefox / Safari)

CUDA (optional, for GPU acceleration)

⚠️ Notes
Simple line drawings work best

Do not refresh the page during generation

If errors occur, ensure gradio==3.44.4 is installed

🧱 Tech Stack
FastAPI

Gradio

Diffusers

Transformers

PyTorch

Segment Anything

OpenCV, Pillow

📄 License
MIT License

<details> <summary>📘 中文版说明（点击展开）</summary>
🎨 像素画生成器
一个基于 AI 的像素画生成器，可以将手绘草图转换为像素风格的艺术作品。

🚀 本项目使用 Gradio==3.44.4，请确保安装此版本以避免兼容性问题。

🌟 功能特点
将手绘草图转换为像素风格图片

支持文本提示词引导生成

实时显示生成进度

简洁直观的 Web 界面（基于 Gradio）

📦 安装与使用
请参考上方英文步骤执行。

</details> <details> <summary>📙 日本語版の説明（クリックで展開）</summary>
🎨 ピクセルアート ジェネレーター
手描きスケッチをピクセルアートに変換する AI ツールです。

🚀 このプロジェクトは Gradio==3.44.4 を使用しています。必ずこのバージョンをご使用ください。

🌟 特徴
スケッチをピクセルアートに変換

テキストプロンプトにも対応

生成中に進行状況を表示

シンプルで使いやすい Gradio UI

📦 インストール方法
英語版の手順をご参照ください。

</details>
🖼️ 画像の生成例（Sample Outputs）
以下は本ツールで生成されたアートの例です：

<p align="center"> <img src="readme_img/output_1.png" width="45%" /> <img src="readme_img/output_1_snapshot.png" width="45%" /> </p> <p align="center"> <img src="readme_img/output_2.png" width="45%" /> <img src="readme_img/output_2_snapshot.png" width="45%" /> </p> <p align="center"> <img src="readme_img/output_3.png" width="45%" /> <img src="readme_img/output_3_snapshot.png" width="45%" /> </p> <p align="center"> <img src="readme_img/output_4.png" width="45%" /> <img src="readme_img/output_4_snapshot.png" width="45%" /> </p>
Generated art changes based on input sketch and prompt. Simple line art yields better results.
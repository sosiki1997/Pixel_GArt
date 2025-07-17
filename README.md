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

## Introduction

This project is a pixel art generator that leverages Stable Diffusion 1.5 combined with the PixelArtRedmond LoRA to transform hand-drawn sketches into stunning retro-style pixel masterpieces. Designed to unleash creativity, it offers users an easy way to create high-quality pixel art inspired by classic video games.

## 📦 Installation 

### 1. Clone the project

```
git clone git@github.com:sosiki1997/Pixel_GArt.git

cd Pixel_GArt
```

### 2. Create and activate conda environment

```
conda create -n pixel_venv python=3.12

conda activate pixel_venv
```

### 3. Install dependencies

```
pip install gradio==3.44.4

pip install -r requirements.txt

pip install torch torchvision opencv-python pillow

pip install git+https://github.com/facebookresearch/segment-anything.git
```

### 4. Run the server

```
python -m app.main
```

### 5. Open in browser

```
 http://127.0.0.1:7860
```

<details>
  <summary>📖 中文说明（点击展开）</summary>


本项目是一个像素画生成器，结合了 Stable Diffusion 1.5 和 PixelArtRedmond LoRA，能将手绘草图转化为令人惊艳的复古风格像素艺术。旨在释放创意，让用户轻松创作出高品质的像素艺术作品，灵感源自经典电子游戏。

</details>

<details>
  <summary>📖 日本語の説明（クリックで展開）</summary>


本プロジェクトは、Stable Diffusion 1.5 と PixelArtRedmond LoRA を組み合わせて、手描きのスケッチを圧巻のレトロ風ピクセルアートに変換するジェネレーターです。クラシックゲームにインスパイアされた高品質なピクセルアートを手軽に制作できることを目的としています。

</details>

---

## 🖼️ 出力例（生成画像）

<p align="center">
  <img src="./readme_img/output_1_snapshot.png" width="600"/>
  <img src="./readme_img/output_2_snapshot.png" width="600"/>
  <img src="./readme_img/output_3_snapshot.png" width="600"/>
  <img src="./readme_img/output_4_snapshot.png" width="600"/>
</p>

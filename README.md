# 🎨 Pixel Art Generator

An AI-based pixel art generator that transforms hand-drawn sketches into pixel-style artworks.

> 🚀 This project uses `Gradio==3.44.4`. Please use this specific version to avoid compatibility issues.

---

## 🌟 Features

- Convert hand-drawn sketches into pixel-style images
  
- Optional text prompt to guide the generation
  
- Real-time generation progress display
  
- Simple and intuitive web UI (built with Gradio)
  

---

## 📦 Installation

### 1. Clone the project

```bash
git clone [your-repo-url]

cd pixel-art-generator
```

### 2. Create and activate conda environment

```bash
conda create -n pixel_venv python=3.12

conda activate pixel_venv
```

### 3. Install dependencies

```bash
pip install gradio==3.44.4

pip install -r requirements.txt

pip install torch torchvision opencv-python pillow

pip install git+https://github.com/facebookresearch/segment-anything.git
```

### 4. Run the server

```bash
python -m app.main
```

### 5. Open in browser

```
http://localhost:8000
```

---

## 🛠️ Usage

1. Upload or draw a sketch
  
2. (Optional) Enter a text description
  
3. Click the generate button
  
4. Wait for the pixel art to appear 🎉
  

---

## 💻 System Requirements

- Python 3.10 or 3.12
  
- Conda (recommended)
  
- 8GB+ RAM
  
- Modern browser (Chrome / Firefox / Safari)
  
- CUDA (optional, for GPU acceleration)
  

---

## ⚠️ Notes

- Simple line drawings work best
  
- Do not refresh the page during generation
  
- If error occurs, ensure `gradio==3.44.4` is installed
  

---

## 🧱 Tech Stack

- FastAPI
  
- Gradio
  
- Diffusers
  
- Transformers
  
- PyTorch
  
- Segment Anything
  
- OpenCV, Pillow
  

---

## 📄 License

MIT License

---

<details>

<summary>📘 中文版</summary>

# 🎨 Pixel Art Generator

一个基于 AI 的像素画生成器，可以将手绘草图转换为像素风格的艺术作品。

> 🚀 本项目使用 `Gradio==3.44.4`，请确保安装此版本以避免兼容性问题。

---

## 🌟 功能特点

- 将手绘草图转换为像素风格图片
  
- 支持输入文本提示词引导生成
  
- 实时显示生成进度
  
- 简洁直观的 Web 界面（基于 Gradio）
  

---

## 📦 安装步骤

### 1. 克隆项目

```bash
git clone [项目地址]

cd pixel-art-generator
```

### 2. 创建并激活 Conda 环境

```bash
conda create -n pixel_venv python=3.12

conda activate pixel_venv
```

### 3. 安装依赖

```bash
pip install gradio==3.44.4

pip install -r requirements.txt

pip install torch torchvision opencv-python pillow

pip install git+https://github.com/facebookresearch/segment-anything.git
```

### 4. 启动服务器

```bash
python -m app.main
```

### 5. 打开浏览器访问

```
http://localhost:8000
```

---

## 🛠️ 使用步骤

1. 上传或绘制草图
  
2. 输入提示词（可选）
  
3. 点击“生成”按钮
  
4. 等待生成结果 🎉
  

---

## 💻 系统要求

- Python 3.10 或 3.12
  
- Conda（推荐）
  
- 至少 8GB 内存
  
- 现代浏览器（Chrome / Firefox / Safari）
  
- CUDA（可选，用于 GPU 加速）
  

---

## ⚠️ 注意事项

- 建议使用清晰、简洁的线稿
  
- 生成过程中请勿刷新页面
  
- 若出现报错，请检查 Gradio 版本
  

---

## 🧱 技术栈

- FastAPI
  
- Gradio
  
- Diffusers
  
- Transformers
  
- PyTorch
  
- Segment Anything
  
- OpenCV, Pillow
  

---

## 📄 许可证

MIT License

</details>

<details>

<summary>📙 日本語版</summary>

# 🎨 Pixel Art Generator

手描きスケッチをピクセルアートに変換する、AIベースのジェネレーターです。

> 🚀 このプロジェクトは `Gradio==3.44.4` を使用しています。互換性のため、必ずこのバージョンをご使用ください。

---

## 🌟 特徴

- 手描きスケッチをピクセル風の画像に変換
  
- テキストプロンプトによる生成指示が可能
  
- 生成進行状況をリアルタイムで表示
  
- シンプルで使いやすい UI（Gradio ベース）
  

---

## 📦 インストール手順

### 1. プロジェクトをクローン

```bash
git clone [リポジトリURL]

cd pixel-art-generator
```

### 2. Conda 環境を作成・有効化

```bash
conda create -n pixel_venv python=3.12

conda activate pixel_venv
```

### 3. 依存関係のインストール

```bash
pip install gradio==3.44.4

pip install -r requirements.txt

pip install torch torchvision opencv-python pillow

pip install git+https://github.com/facebookresearch/segment-anything.git
```

### 4. サーバーを起動

```bash
python -m app.main
```

### 5. ブラウザでアクセス

```
http://localhost:8000
```

---

## 🛠️ 使い方

1. スケッチをアップロードまたは描画
  
2. 必要に応じてテキストを入力
  
3. 「生成」ボタンをクリック
  
4. 数秒後に結果が表示 🎉
  

---

## 💻 システム要件

- Python 3.10 または 3.12
  
- Conda（推奨）
  
- メモリ 8GB 以上
  
- 最新ブラウザ（Chrome / Firefox / Safari）
  
- CUDA（任意、GPU利用時）
  

---

## ⚠️ 注意事項

- シンプルな線画を推奨
  
- 生成中はページを更新しないでください
  
- エラーが出た場合は Gradio バージョンを確認
  

---

## 🧱 技術スタック

- FastAPI
  
- Gradio
  
- Diffusers
  
- Transformers
  
- PyTorch
  
- Segment Anything
  
- OpenCV, Pillow
  

---

## 📄 ライセンス

MIT License

</details>
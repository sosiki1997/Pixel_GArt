from models.generator import PixelArtGenerator
from interface.gradio_ui import create_gradio_interface

# 初始化生成器和 Gradio 界面
generator = PixelArtGenerator()
interface = create_gradio_interface(generator)

# ✅ 推荐方式：Gradio-only 模式，兼容 Hugging Face Spaces
def launch_app():
    interface.launch()

# --------------------------------------------
# FastAPI + Gradio 挂载方式（仅供保留）
"""
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import webbrowser
import threading

# 初始化 FastAPI 应用（本地或云服务用）
app = FastAPI(title="Pixel Art Generator")

# 配置跨域访问（为未来扩展做准备）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载 Gradio 到 FastAPI 路径 "/"
app = gr.mount_gradio_app(app, interface, path="/")

# 定义 FastAPI 路由（上传草图并生成像素画）
@app.post("/generate")
async def generate_pixel_art(
    sketch: UploadFile = File(...),
    prompt: str = "pixel art style"
):
    try:
        image_data = await sketch.read()
        result = generator.generate(image_data, prompt)
        return {"status": "success", "image": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# ✅ 本地调试用 uvicorn 启动 FastAPI + 自动打开浏览器
if __name__ == "__main__":
    print("正在启动服务器...")
    print("浏览器打开中：http://127.0.0.1:8000")
    threading.Thread(target=lambda: webbrowser.open("http://127.0.0.1:8000")).start()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)
"""
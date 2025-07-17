from models.generator import PixelArtGenerator
from interface.gradio_ui import create_gradio_interface

# 初始化生成器和 Gradio 界面
generator = PixelArtGenerator()
interface = create_gradio_interface(generator)


def launch_app():
    interface.launch()


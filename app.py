# app.py - Hugging Face 和本地都能用的入口

import sys
import os

# 把 app 目录加入路径（方便导入 main）
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "app")))

from main import launch_app

# ✅ 无论是否 __main__ 都调用 launch_app（HF Spaces 也能运行）
launch_app()
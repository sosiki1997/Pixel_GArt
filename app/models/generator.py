import torch
from diffusers import StableDiffusionPipeline
from huggingface_hub import snapshot_download
import gc

class PixelArtGenerator:
    def __init__(self,
                 base_model_repo="runwayml/stable-diffusion-v1-5",
                 base_model_path="./models/stable-diffusion-v1-5",
                 lora_file="./models/my_lora/PixelArtRedmond15V-PixelArt-PIXARFK.safetensors",
                 device=None):
        if device:
            self.device = device
        elif torch.backends.mps.is_available():
            self.device = torch.device("mps")
        elif torch.cuda.is_available():
            self.device = torch.device("cuda")
        else:
            self.device = torch.device("cpu")

        print(f"使用设备: {self.device}")

        # 下载基础模型
        print(f"检查并下载基础模型: {base_model_repo} 到 {base_model_path}")
        snapshot_download(repo_id=base_model_repo, cache_dir=base_model_path, local_dir=base_model_path, local_dir_use_symlinks=False)

        # 加载基础模型
        print("加载基础模型...")
        self.pipe = StableDiffusionPipeline.from_pretrained(
            base_model_path,
            torch_dtype=torch.float16 if self.device.type == "cuda" else torch.float32,
            revision="fp16" if self.device.type == "cuda" else "main",
            local_files_only=True,
        ).to(self.device)

        # 加载LoRA权重
        print(f"加载LoRA权重文件: {lora_file}")
        self.pipe.load_lora_weights(lora_file)

        # 打印 UNet，确认 LoRA 相关模块是否已注入成功
        # print(self.pipe.unet)

        # 优化内存
        self.pipe.enable_attention_slicing()

    def generate(self, prompt, guidance_scale=7.5, num_inference_steps=50, height=384, width=384):
        print(f"生成图像，提示词: {prompt}")
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()

        if self.device.type == "cuda":
            with torch.autocast("cuda"):
                result = self.pipe(
                    prompt,
                    guidance_scale=guidance_scale,
                    num_inference_steps=num_inference_steps,
                    height=height,
                    width=width,
                )
        else:
            result = self.pipe(
                prompt,
                guidance_scale=guidance_scale,
                num_inference_steps=num_inference_steps,
                height=height,
                width=width,
            )

        image = result.images[0]

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()

        return image

if __name__ == "__main__":
    generator = PixelArtGenerator()
    prompt = "pixel art style, cute cat, colorful"
    img = generator.generate(prompt)
    img.save("output.png")
    print("图片已保存为 output.png")





# https://www.blog.pythonlibrary.org/2017/10/17/how-to-watermark-your-photos-with-python/

from PIL import Image
import os

def watermark_with_transparency(
    input_image_path, output_image_path, watermark_image_path, position
):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size

    transparent = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)

    # opacity
    transparent.putalpha(128)
    base_image.paste(transparent, transparent)

    base_image.save(output_image_path)


if __name__ == "__main__":
    img_folder = "images"
    for file in os.listdir(img_folder):
        watermark_with_transparency(
            f"{img_folder}/{file}", f"watermarked_images/wm_{file}.png", "logo.png", position=(0, 0)
        )

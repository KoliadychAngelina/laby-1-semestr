from PIL import Image

def create_blank_image(width: int = 100, height: int = 100) -> str:
    img = Image.new("RGB", (width, height), color="blue")
    img.save("test.png")
    return "Зображення test.png створено успішно"
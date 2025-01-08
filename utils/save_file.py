from uuid import uuid4
from configs.config import IMG_URL
import os

def save_file(file):
    file_name = str(uuid4())
    _, file_extension = os.path.splitext(file.filename)
    img_name = f"{file_name}{file_extension}"
    file.save(f"img/{img_name}")
    return IMG_URL + img_name
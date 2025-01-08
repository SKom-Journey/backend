import os

def delete_file(name: str):
    image_name = os.path.basename(name)
    if os.path.exists(f"img/{image_name}"):
        os.remove(f"img/{image_name}")
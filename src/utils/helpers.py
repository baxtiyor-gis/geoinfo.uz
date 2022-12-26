
from werkzeug.datastructures import FileStorage
from hashlib import sha256


def save_image(image_data: FileStorage, slug,  model):
    name= image_data.filename
    ext = name.rsplit(".")

    pass

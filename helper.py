
from PIL import Image, ImageTk

def get_photo_image(path: str, new_size):

    return ImageTk.PhotoImage(Image.open(path).resize(new_size))



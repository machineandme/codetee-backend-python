from PIL.Image import Image
import random



def random_swap(img: Image):
    w, h = img._size
    for _ in range((w * h) // 10):
        rp = img.getpixel((random.randrange(w), random.randrange(h),))
        img.putpixel((random.randrange(w), random.randrange(h),), rp)

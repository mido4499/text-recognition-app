import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\asmaa.ahmed\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def extract_text(imgFileName):
    img = Image.open(imgFileName)
    img = enhance_image(img)
    return pytesseract.image_to_string(img)


def enhance_image(img: Image.Image):
    # Converting to greyscale
    img.convert('L')




    # Sharpen image
    img = img.filter(ImageFilter.SHARPEN)


    img = img.crop((60, 360, 660, 720))

    return img


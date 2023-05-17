
# import the following libraries
# will convert the image to text string
import pytesseract

# adds image processing capabilities
from PIL import Image

# converts the text to speech
import pyttsx3
from tkinter import filedialog
# translates into the mentioned language
from googletrans import Translator
#Browsing Only Png Files
def image_ocr():
    filename =filedialog.askopenfilename(filetypes=(("jpg files","*.jpg"),("All files","*.*")))
    return filename
def analyze_img():
    # opening an image from the source path
    img = Image.open(image_ocr())
    # describes image format in the output
    print(img)
    # path where the tesseract module is installed
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    # converts the image to result and saves it into result variable
    result = pytesseract.image_to_string(img)
    # write text in a text file and save it to source path
    with open('ocr\output.txt', mode='w') as file:
        file.write(result)
        print("TEXT = ",result)

    p = Translator()
    # translates the text into german language
    k = p.translate(result, dest='hindi')
    print(k)
    engine = pyttsx3.init()

    # an audio will be played which speaks the test if pyttsx3 recognizes it
    engine.say(k)
    engine.runAndWait()
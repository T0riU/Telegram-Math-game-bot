import pyautogui
import cv2
import numpy
from PIL import Image
import keyboard
import time
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# Set the area of the screen to capture (x, y, width, height)
screen_area = (1200, 300, 500, 300)

temp = ""
while True:
    img = pyautogui.screenshot(region=screen_area)
    cvimg = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(cvimg, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    font = cv2.FONT_HERSHEY_SIMPLEX

    text = pytesseract.image_to_string(gray, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789+-*/()=x')
    text = text.replace('\n', ' ')
    text = text.replace('x', '*')
    
    if(temp!=text):
        temp = text
        text = text.split('=')
        try:
            print(text[0],"=" ,text[1])
            print(eval(text[0])==eval(text[1]))
            # cv2.putText(cvimg, eval(text[0])==eval(text[1]), (0,50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        except:
            print("nope")
            # cv2.putText(cvimg, "nope", (0,50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        
        # cv2.imshow("Image", cvimg)

        time.sleep(1)
        # keyboard.wait('z')
        print("->")

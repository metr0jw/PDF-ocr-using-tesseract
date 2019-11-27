from PIL import Image
import pytesseract
from googletrans import Translator
import sys
from pdf2image import convert_from_path
import os


# Define translator
translator = Translator()

# PDF file name
PDF_file = "kingBook-ch1to10.pdf"
#pages = convert_from_path(PDF_file, poppler_path="D:/jiw00n/poppler/bin", dpi=500)
image_counter = 1

# PDF to PNG
"""
for page in pages:
    filename = "page_" + str(image_counter) + ".jpg"
    # page.save(filename, 'JPEG')
    image_counter = image_counter + 1
"""
print("page finish")
filelimit = 336

# PNG images to text
for i in range(1, filelimit + 1):
    strNum = str(i)
    strNum = strNum.rjust(3, '0')

    outfile = "knk_text/knk_page_" + strNum + ".txt"
    outfile_trans = "knk_translated/knk_page_trans_" + strNum + ".txt"
    f = open(outfile, "w", encoding='utf8')
    f_trans = open(outfile_trans, "w", encoding='utf8')
    filename = "pngs/kingBook-ch1to10-" + strNum + ".png"
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
    text = text.replace('-\n', '')
    f.write(text)
    f.close()

    # if text is null
    if(text == ''):
        f_trans.write('')
        f_trans.close()
        continue
    text_trans = translator.translate(text, src='en', dest='ko')
    f_trans.write(text_trans.text)
    f_trans.close()
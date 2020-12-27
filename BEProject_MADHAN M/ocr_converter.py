import os
import cv2
import pytesseract
import PyPDF2

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\God\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

# DIR = "E:/PyCharm/PythonInternshipBestEnlist/day16_project/"
# DIR_IMAGES = "images/"
# input_files = [DIR + DIR_IMAGES + "my_temp.PNG",
#                DIR + DIR_IMAGES + "temp1.png",
#                DIR + DIR_IMAGES + "temp2.png",
#                DIR + DIR_IMAGES + "classdia.PNG"]


def convert_To_PDF(input_files):
    # Creating pdffilemerger object
    pdfMerger = PyPDF2.PdfFileMerger()

    for file in input_files:
        # Creating image object
        image = cv2.imread(file)

        # Converting the image to ocr pdf
        result = pytesseract.image_to_pdf_or_hocr(image, lang='eng')

        # Writing the ocr converted result to a temp.pdf file
        with open("temp.pdf", 'wb') as current_page_file:
            current_page_file.write(bytearray(result))

        # Appending the temp.pdf file to pdfmerger object
        pdfMerger.append(PyPDF2.PdfFileReader('temp.pdf'), 'rb')

    # Deleting temp.pdf file
    os.remove('temp.pdf')

    # Saving merged pdf object as pdf file
    output_file_location = "output/my_output.pdf"
    output_file = open(output_file_location, 'wb')
    pdfMerger.write(output_file)
    output_file.close()
    pdfMerger.close()
    return os.path.abspath(output_file_location)

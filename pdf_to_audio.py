#написати програму що конвертує PDF файл у аудіо-файл

import PyPDF3
import pyttsx3
import pdfplumber

#вказуємо директорію файлу який ми хочемо конвертувати
file = 'd:/OTHER/University/3 курс/2 семестр/Тренінг-курс 1/test.pdf'

#створюємо об'єкт файлу для PDF файлу та об'єкт читання PDF
book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)

#знаходимо загальну кількість сторінок
pages = pdfReader.numPages

#витягаємо текст з PDF файлу
#використовуємо цикл для того щоб перебрати всі сторінки
finalText = ""
with pdfplumber.open(file) as pdf:
    for i in range(0, pages): 
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text

#зберігаємо результат
engine = pyttsx3.init()
engine.save_to_file(finalText, 'd:/OTHER/University/3 курс/2 семестр/Тренінг-курс 1/test.mp3')
engine.runAndWait()

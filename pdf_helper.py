import PyPDF2
import re
import pdftotext
from PIL import Image
from pytesseract import pytesseract


CHARS_TO_REMOVE = "\"',./[]{}-_:;!”“✡0123456789"


def read_file(file_name):
    file = open(file_name, 'rb')

    full_text = ''
    last_word = ''

    reader = PyPDF2.PdfFileReader(file)

    for i, page in enumerate(reader.pages):
        if i < 3:
            continue
        page_text = page.extractText().split('\n')
        first_line = page_text[0].split(' ')
        if first_line[0] == last_word:
            continue
        else:
            print(page_text[0], i)
            last_word = first_line[0]
        # for line in page_text:
            # print(line[0])
        #     check = re.findall('.*[0-9]:[0-9].*', line)
        #     if line[-1] != ' ':
        #         line += ' '
        #     if len(check) > 0:
        #         continue
        #     else:
        #         overlap = set(line) & set(CHARS_TO_REMOVE)
        #         if len(overlap) > 0:
        #             for char in overlap:
        #                 line = line.replace(char, '')
        #
        #         full_text += line
        #
        # print(full_text)



def other():
    img = Image.open('test.png')
    text = pytesseract.image_to_string(img)
    print(text)


if __name__ == '__main__':
    read_file('bible.pdf')

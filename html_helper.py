import PyPDF2
import re
import pdftotext
from PIL import Image
from pytesseract import pytesseract
import os
from tqdm import tqdm

DIRECTORY = 'html/'

def load_data():
    all_data = ''

    for file in tqdm(os.listdir(DIRECTORY), desc='Combining'):
        file = DIRECTORY + file
        with open(file, 'r', encoding='UTF-8') as in_file:
            data = ' '.join(in_file.readlines())
            data = re.sub(r'<span class=.*?</span>', '', data)
            data = re.sub(r'<a.*?</a>', '', data)
            divs = re.findall(r'<div class=\'mt\'.*?>(.*?) </div>', data)
            divs.extend(re.findall(r'<div class=\'mt2\'.*?>(.*?) </div>', data))
            divs.extend(re.findall(r'<div class=\'ip\'.*?> (.*?) </div>', data))
            divs.extend(re.findall(r'<div class=\'s\'.*?> (.*?) </div>', data))
            divs.extend(re.findall(r'<div class=\'p\'.*?> (.*?) </div>', data))

        all_data += ' '.join(divs)

    return all_data


if __name__ == '__main__':
    data = load_data()
    print(data)

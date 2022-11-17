import unicodedata
import re
import os
from tqdm import tqdm

DIRECTORY = 'html/'


def load_data(dir_ext):
    all_data = []

    i = 0

    directory = DIRECTORY + dir_ext + '/'

    for file in tqdm(os.listdir(directory), desc='Combining'):
        i += 1
        file = directory + file
        divs = []
        with open(file, 'r', encoding='UTF-8') as in_file:
            data = ' '.join(in_file.readlines())
            data = unicodedata.normalize('NFC', data)
            data = re.sub(r'<span class=.*?</span>', '', data)
            data = re.sub(r'<a.*?</a>', '', data)
            data = data.replace(u'\xa0', u' ')
            check_divs = re.findall(r'<div class=\'mt\'.*?>(.*?) </div>', data)
            check_divs.extend(re.findall(r'<div class=\'mt2\'.*?>(.*?) </div>', data))
            # print(data)
            check_divs.extend(re.findall(r'<div class=\'ip\'>(.*)', data))

            if len(check_divs) > 0:
                full = ' '.join(check_divs)
                full = re.sub(r'[\,,@,#,$,%,^,&,*,(,),\[,\],\',\",;,:,“,”,‘,’]', '', full)
                full = re.sub(' +', ' ', full).strip()
                full = re.split('[\.,\?,!,\n]', str(full))
                all_data.extend(full)

            divs.extend(re.findall(r'<div class=\'[p,s]\'.*?>(.*?) </div>', data))

        full_data = ' '.join(divs)
        full_data = re.sub(r'[\,,@,#,$,%,^,&,*,(,),\[,\],\',\",;,:,“,”,‘,’]', '', full_data)
        full_data = re.sub(' +', ' ', full_data).strip()
        full_data = re.split('[\.,\?,!,\n]', str(full_data))

        all_data.extend(full_data)

        clean = []
        for row2 in all_data:
            if len(row2) >= 1:
                clean.append(row2)

        if i > 0:
            break

    return clean


if __name__ == '__main__':
    datar = load_data('train')
    for row in datar:
        print('||||', row)

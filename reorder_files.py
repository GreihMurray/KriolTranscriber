import os
from tqdm import tqdm

ORDERS = ['GEN', 'EXO', 'LEV', 'NUM', 'DEU', 'JOS', 'JDG', 'RUT', '1SA', '2SA', '1KI', '2KI', '1CH', '2CH', 'EZR',
          'NEH', 'EST', 'JOB', 'PSA', 'PRO', 'ECC', 'SNG', 'ISA', 'JER', 'LAM', 'EZK', 'DAN', 'HOS', 'JOL', 'AMO',
          'OBA', 'JON', 'MIC', 'NAM', 'HAB', 'ZEP', 'HAG', 'ZEC', 'MAL', 'MAT', 'MRK', 'LUK', 'JHN', 'ACT', 'ROM',
          '1CO', '2CO', 'GAL', 'EPH', 'PHP', 'COL', '1TH', '2TH', '1TI', '2TI', 'TIT', 'PHM', 'HEB', 'JAS', '1PE',
          '2PE', '1JN', '2JN', '3JN', 'JUD', 'REV']

directory = 'html'

for file in tqdm(os.listdir(directory), desc='Combining'):
    try:
        old_f = 'html/' + file
        f = directory + '/' + str(ORDERS.index(file[:3])) + '_' + file
        os.rename(old_f, f)
        print(f)
    except ValueError:
        print(file, '||||||||||||||||||')

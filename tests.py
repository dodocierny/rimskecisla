import rimske_cisla
from csv import reader


def test_conversion_2_rome():
    '''Otestuje prevod čísiel z arabských na rímske.
    Porovná výsledky z datasetom, kde je správny prevod čísiel
    od 1 do 3999 z arabských do rímskych.'''
    error_counter = 0

    with open('dataset.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            # v 0 máme arabské číslo a v 1 máme príslušné rímske číslo
            converted = rimske_cisla.arabic_2_rome(int(row[0]))
            if converted != row[1]:
                error_counter += 1
                print(f'Vstup: {row[0]} '
                      f'je: {rimske_cisla.arabic_2_rome(int(row[0]))} '
                      f'a má byť: {row[1]}')

    print(f'\nKONVERZIA Z ARABSKÝCH NA RÍMSKE')
    print(f'CELKOVO CHÝB: {error_counter}')


def test_conversion_2_arabic():
    '''Otestuje prevod čísiel z arabských na rímske.
    Porovná výsledky z datasetom, kde je správny prevod čísiel
    od 1 do 3999 z rímskych na arabské čísla.'''
    error_counter = 0

    for i in range(rimske_cisla._MAX_ARABIC_NUMBER):
        number = i + 1
        rome = rimske_cisla.arabic_2_rome(number)
        arabic = rimske_cisla.rome_2_arabic(rome)

        if arabic != number:
            error_counter += 1
            print(f'Vstup: {rome} '
                  f'je: {arabic} '
                  f'a má byť: {number}')

    print(f'\nKONVERZIA Z RÍMSKYCH NA ARABSKÉ')
    print(f'CELKOVO CHÝB: {error_counter}')

test_conversion_2_rome()
test_conversion_2_arabic()
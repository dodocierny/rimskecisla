'''Modul pre prevod medzi rímskymi a arabskými číslami a opačne.'''

# #########################################################################
# POMOCNÉ PREMENNÉ A KONŠTANTY
# #########################################################################

# štandardne min a max číslo zapísateľné v rímskych čísliciach podľa
# známych pravidiel - zároveň definuje rozsah, s ktorým algoritmus počíta
_MIN_ARABIC_NUMBER = 1
_MAX_ARABIC_NUMBER = 3999

# slovník pre prevod z arabských na rímske čísla, obsahuje všetko čo sa
# priamo prevedie tak, ako je uvedené v slovníku
_ARABIC_2_ROME = {
    1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII',
    8: 'VIII', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
    100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
}

# základy používane na prevod z arabských na rímske čísla
_BASE_ROME = [1000, 900, 500, 400, 100, 90, 50, 40, 10]
_BASE_ARABIC = ['M', 'D', 'C', 'L', 'X']


# #########################################################################
# HLAVNÉ METÓDY
# #########################################################################
def arabic_2_rome(number:int) -> str:
    '''Prevedie arabské číslo na rímske. Pozná čísla od 1 do 3999.'''

    # Rimania vyjadrovali maximálne 3999 štandardne, potom to už robili rôzne
    # http://www.converter.cz/prevody/rimska-cisla.htm
    number = int(number)
    if number < 0 or number > 3999:
        raise ValueError('Toto nie je číslo, ktoré by som vedel previesť.')

    result = ''
    # prejdem základy a postupne ich spracovávam
    # to čo som spracoval odčítam a ďalej už ide len zvyšok po odčítaní
    # základ je minimálne 10, čísla menšie prevediem už priamo zo slovníka
    # ak mi po nejakom prevode ostane nula, rovno skončím
    # (číslo je napr. 10, 50, 60, ... vždy násobky desiatich)
    for base in _BASE_ROME:
        if number >= base:
            occurrence = number // base # počet výskytov čísla v základe
            result += occurrence * _ARABIC_2_ROME[base] # pripočítam k výsledku
            number -= occurrence * base # spracované odčítam od vstupu
            if number == 0:
                return result

    result += _ARABIC_2_ROME[number] # tu mám číslo menšie ako 10 (min. základ)
    return result

# TODO skontrolovať vstupnú hodnotu či je spracovateľná
def rome_2_arabic(number:str) -> int:
    '''Prevedie rímske číslo na arabské. Pozná čísla od 1 do 3999.'''

    keys = list(_ARABIC_2_ROME.keys())
    vals = list(_ARABIC_2_ROME.values())
    digits = list(number)
    result = 0

    while True:

        # ak už mám zadané číslo priamo v slovníku tak vrátim ho a končím
        current_number = ''.join(digits)
        if current_number in vals:
            return result + keys[vals.index(current_number)]

        # vyberiem si aktuálne číslo a nasledujúce
        # podľa toho sa potrebujem rozhodnúť
        # spracujem vždy jedno alebo dve čísla naraz, nikdy viac
        current_value = keys[vals.index(digits[0])]
        next_value = keys[vals.index(digits[1])]

        # aktuálne je väčšie alebo rovnaké ako ďalšie - pridám k výsledku
        if current_value >= next_value:
            result += current_value
            digits.pop(0)   # zmažem spracované
        # aktuálne je menšie ako ďalšie - odčítam ich a pridám k výsledku
        # spracoval som naraz dve čísla
        else:
            result += next_value - current_value
            digits.pop(0)   # zmažem spracované
            digits.pop(0)   # zmažem spracované

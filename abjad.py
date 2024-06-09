# ابجد هوز حطی کلمن سعفص قرشت ثخذ ضظغ

def abjad_func(word:str) -> int:
    numbers_dict= {'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز':7, 'ح': 8, 'ط': 9, 'ی': 10,
                   'ک': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100,
                   'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000,
                   'پ': 2, 'چ': 3, 'گ': 20, 'ژ': 7, 'آ': 1}
    n = 0
    for char in word:
        if char == '\n':
            continue
        n += numbers_dict[char]
    return n

# zat ol rieh
# if you want to use "base.py" turn this part off:
while True:
    word = input('Enter a word: ')
    if word == 'stop':
        break
    print(abjad_func(word))
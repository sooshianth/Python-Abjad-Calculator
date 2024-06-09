from abjad import abjad_func
import chardet

def main(infilename, outfilename):
    with open(infilename, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    res_dict = {}
    with open(infilename, 'r', encoding=encoding) as infile, open(outfilename, 'w', encoding='utf8') as outfile:
        for word in infile:
            word = word
            if word:
                if abjad_func(word) not in res_dict.keys():
                    res_dict[abjad_func(word)] = word
                else:
                    res_dict[abjad_func(word)] += f' {word}'
        for k in sorted(res_dict.keys()):
            outfile.write(f'{k} : {res_dict[k]} \n')



main('words.txt', 'natige.txt')




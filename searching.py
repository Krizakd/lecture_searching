import json
import os

# from lecture_searching.generators import unordered_sequence

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name,klic):
    with open(file_name,"r") as soubor:
        data=json.load(soubor)
        s=data[klic]
        return s

def linear_search(sekvence, cislo):
    count = 0
    seznam = []
    slovnik = {}
    for poradi, i in enumerate(sekvence):
        if i == cislo:
            count += 1
            seznam.append(poradi)
            slovnik["positions"] = seznam
            slovnik["count"] = count
    return slovnik

def binary_search(sekvence, cislo):
    prava = len(sekvence) -1
    leva = 0
    while leva <= prava:
        stred = (leva + prava) // 2
        if sekvence[stred] == cislo:
            return stred
        elif sekvence[stred] < cislo:
            leva = stred + 1
        else:
            prava = stred -1






def main():
    # seqential=read_data("sequential.json","unordered_numbers")
    seqential = read_data("sequential.json", "ordered_numbers")

    s=binary_search(seqential, 2)
    print(s)








if __name__ == '__main__':
    main()
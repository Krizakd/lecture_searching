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
    for poradi, i in enumerate(sekvence):
        if i == cislo:
            count += 1
            seznam.append(poradi)
    return count, seznam


def main():
    seqential=read_data("sequential.json","unordered_numbers")
    pocet, poradi=linear_search(seqential, 0)
    print(pocet)
    print(poradi)







if __name__ == '__main__':
    main()
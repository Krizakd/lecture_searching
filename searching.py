import json
import os

from lecture_searching.generators import unordered_sequence

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name,klic):
    with open(file_name,"r") as soubor:
        data=json.load(soubor)
        s=data[klic]
        return s




def main():
    seqential=read_data("sequential.json","unordered_numbers")
    print(seqential)


if __name__ == '__main__':
    main()
# Extraindo arquivos de dados e Metadados
#
# coding: utf-8

import zipfile
import sys
import os

def main(path):
    if not os.path.exists(path):
        print("Arquivo {} não existe".format(path))
        sys.exit(-1)
    else:
        print(path)
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        zfile.close()
        print("Arquivos extraídos")

if __name__ == "__main__":
    main(sys.argv[1])

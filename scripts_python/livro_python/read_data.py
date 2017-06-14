#coding: utf-8
import os

def read_meta_data(path):
    data = open(path, "rt")
    meta_data = []
    for line in data:
        line_data = line.split('\t')
        meta_data.append((line_data[0], line_data[1], line_data[2]))
    data.close()
    return meta_data

def main():
    print(read_meta_data('data/meta-data/Instituicao.txt'))

if __name__ == "__main__":
   main()

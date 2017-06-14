#coding: utf-8
import os
import platform as hw

def get_os():
    os = hw.system()
    machine = hw.machine()
    hostname = hw.node()
    platform = hw.platform()
    print("Operation System: " + os + "\n"
          "Machine: " + machine + "\n" +
          "Hostname: " + hostname + "\n"
          "Platform: " + platform + "\n")

def read_lines(filename):
    _file = open(os.path.join("/etc/", filename), "rt")
    data = _file.read().split("\n")
    _file.close()
    return data

def read_metadata(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            values = column.split(":")
            nome = values[0]
            senha = values[1]
            uid = values[2]
            gid = values[3]
            comment = values[4]
            home = values[5]
            shell = values[6]
            metadata.append((nome, senha, uid, gid, comment, home, shell))
    return metadata

def main():
    get_os()
    meta = {}
    for meta_data_file in os.listdir("/etc/"):
        if meta_data_file == 'passwd':
            meta[meta_data_file] = read_metadata(meta_data_file)
    
    for key, val in meta.items():
        print("Entidade {}".format(key))
        print("Attributes: ")
        for col in val:
            if col[6] == '/bin/bash':
                print("Nome: " + col[0] + "\n" +
                    "Senha: " + col[1] + "\n" +
                    "UID: " + col[2] + "\n" +
                    "GID: " + col[3] + "\n" +
                    "Comment: " + col[4] + "\n" +
                    "Home: " + col[5] + "\n" +
                    "Shell: " + col[6] + "\n")

if __name__ == "__main__":
    main()

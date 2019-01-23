import os
import sys
from random import *
import shutil


def main():
    files = os.listdir()
    for file in files:
        
        if os.path.isdir(file):
            print("Ignoring directory " + file)
            continue # ignore dirs
        elif file == sys.argv[0]:
            print("Ignoring myself " + file)
            continue # ignore self

        # ver se tem . e definir o nome do directorio
        index = file.rfind(".")
        if index != -1:
            ext = file[index + 1:]
        else:
            ext = "unknown"

        # criar a pasta
        try:
            os.mkdir(ext)
        except FileExistsError:
            pass

        # entrar
        os.chdir(ext)
        
        files_in_folder = os.listdir()
        
        # se o ficheiro tiver mesmo nome arranjar outro
        dest_file = file
        while dest_file in files_in_folder:
            dest_file = randint(1, 100000) + file

        # mover e sair 
        shutil.move("../" + file, "./" + dest_file)
        os.chdir("..")

        print("File: " + file + " moved to: " + ext + "/" + dest_file)
        

if __name__ == '__main__':
    main()
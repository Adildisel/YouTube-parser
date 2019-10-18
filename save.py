from multiprocessing import Pool
from main import *

def main():
    helper_save = Helper()

    file_name_list = ['',]

    with Pool(40) as p:
        p.map(helper_save.make_all, file_name_list)


if __name__ == "__main__":
    main()
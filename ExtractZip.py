__author__ = 'paranjay'
import sys
import zipfile
import os

FINAL_FILE_PATH = '/home/paranjay/Downloads/CSE1223/project01/final.txt'

"""
# extract zip
# extract the zips within the main zip
# delete the zip files.
# run through all the folders
    keep going in till you find a Project01.java
    open the file and add it to final.txt
    print this folder is done
"""


def extract_zip(filename):
    fh = zipfile.ZipFile('../' + filename, 'r')
    fh.extractall()


def get_current_dir_file_list():
    return [f for f in os.listdir('.') if os.path.isfile(f)]


def get_current_dir_list():
    return [f for f in os.listdir('.')]


def get_code_from_file(code_file):
    f = open(code_file, 'r')
    code = f.read()
    f.close()
    return code


def post_code_into_final_file(name, code):
    if not os.path.exists(FINAL_FILE_PATH):
        f = open(FINAL_FILE_PATH, 'a')
    else:
        f = open(FINAL_FILE_PATH, 'a')
    f.write('AUTHOR' + '\n')
    f.write(name + '\n')
    f.write('CODE' + '\n')
    f.write(code + '\n')
    f.write('-----------' + '\n')
    f.close()


def copy_code_to_final(student_name):
    while True:
        please_break = False
        files = get_current_dir_list()
        if len(files) == 0:
            please_break = True

        for file_name in files:
            if os.path.isdir(file_name):
                os.chdir(file_name)
            elif os.path.isfile(file_name) and file_name.endswith('.java'):
                post_code_into_final_file(student_name, get_code_from_file(file_name))
                print file_name
                please_break = True

        if please_break:
            break


def run():
    os.chdir('current')
    zip_file_name = sys.argv[1]
    extract_zip(zip_file_name)
    dir_items = get_current_dir_file_list()

    for dir_item in dir_items:
        if zipfile.is_zipfile(dir_item) and dir_item != zip_file_name:
            student_name = dir_item[18:dir_item.index('-', 18) - 1]
            if not os.path.exists(student_name):
                os.makedirs(student_name)
            current_dir = os.getcwd()

            os.chdir(student_name)
            extract_zip(dir_item)
            copy_code_to_final(student_name)
            os.chdir(current_dir)

run()
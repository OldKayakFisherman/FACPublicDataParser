import urllib.request
import os.path
import shutil
from config import Settings
from zipfile import ZipFile
from parsers import *
from data import DataImport

settings = Settings()


def extract_files():
    with ZipFile(os.path.join(settings.get_output_dir(), settings.get_zip_file()), 'r') \
            as target_zip:
        target_zip.extractall(settings.get_output_dir())


def download_file():

    zipfile = urllib.request.urlopen(settings.get_zip_url())
    with open(os.path.join(settings.get_output_dir(), settings.get_zip_file()), 'wb') as output:
        output.write(zipfile.read())


def clean_environment():

    if os.path.isfile(os.path.join(settings.get_output_dir(), settings.get_zip_file())):
        os.remove(os.path.join(settings.get_output_dir(), settings.get_zip_file()))

    if os.path.isdir(os.path.join(settings.get_output_dir(), settings.get_zip_dir())):
        shutil.rmtree(os.path.join(settings.get_output_dir(), settings.get_zip_dir()))


def parseFiles():
    general_records = GeneralParser().parse()
    DataImport().import_general(general_records)

if __name__ == '__main__':


    if settings.get_refresh_files():
        print("refreshing files")
        clean_environment()
        download_file()
        extract_files()

    parseFiles()

    print("complete")


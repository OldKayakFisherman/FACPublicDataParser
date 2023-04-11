import csv
from config import Settings
import os.path
import sys

csv.field_size_limit(sys.maxsize)


class GeneralParser:

    def __init__(self):
        pass

    def parse(self):

        settings = Settings()

        general_text = os.path.join(settings.get_output_dir(), 'general.txt')

        with open(general_text, encoding="windows-1252") as csvfile:
            rdr = csv.reader(csvfile, delimiter='|')
            for row in rdr:
                print(row[0])


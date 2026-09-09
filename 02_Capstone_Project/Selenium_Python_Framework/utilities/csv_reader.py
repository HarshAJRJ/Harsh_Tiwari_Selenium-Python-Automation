import csv
import os


class CSVReader:

    @staticmethod
    def read_data(file_name):

        base_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        file_path = os.path.join(base_dir, "data", file_name)

        with open(file_path, mode="r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            return list(reader)
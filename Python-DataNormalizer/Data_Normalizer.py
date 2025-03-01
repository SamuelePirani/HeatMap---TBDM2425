import os

import pandas as pd


class DataNormalizer:
    def __init__(self, rootFolder):
        self.rootFolder = rootFolder

    def read_data(self):
        csv_files = []
        for subdir, dirs, files in os.walk(self.rootFolder):
            for file in files:
                if file.endswith(".csv"):
                    file_path = os.path.join(subdir, file)
                    csv_files.append(file_path)
        return csv_files

    def write_data(self, data_files):
        for path_csv in data_files:
            df = pd.read_csv(path_csv)
            id_num = os.path.basename(os.path.dirname(path_csv))
            if not self.check_column(df, id_num):
                df.insert(0, id_num, id_num)
                df.to_csv(path_csv, index=False)
                print(f"Document: [{path_csv}] - Operation Success")
            else:
                print(f"Document: [{path_csv}] - Already normalized")

    def check_column(self, file, id_num):
        if id_num in file.columns:
            return True
        return False

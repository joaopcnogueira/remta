import pandas as pd

class DataImport:

    @staticmethod
    def read_tsv(path: str):
        df = pd.read_csv(path, sep='\t')

        return df

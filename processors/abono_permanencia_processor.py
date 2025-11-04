import pandas as pd
from base_processor import BaseProcessor
from utils.constants import SEPREM_RATE

class AbonoPermanenciaProcessor(BaseProcessor):
    def filter_data(self, data :pd.Dataframe) -> pd.DataFrame:
        print(data)
        return data

    def calculate(self, data: pd.DataFrame) -> pd.DataFrame:
        print(data)
        return data

    def validate(self, data: pd.DataFrame) -> pd.DataFrame:
        print(data)
        return data

    def export_to_xlsx(self, data: pd.DataFrame, output_file: str) -> None:
        print('file exported')


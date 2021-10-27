import pandas as pd
from daipecore.pandas.dataframe.PandasDataFrameShowMethodInterface import PandasDataFrameShowMethodInterface


class PandasDataFrameShowMethod(PandasDataFrameShowMethodInterface):
    def show(self, df: pd.DataFrame):
        print(df.head())

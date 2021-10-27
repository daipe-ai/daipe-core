from abc import ABC, abstractmethod
import pandas as pd


class PandasDataFrameShowMethodInterface(ABC):
    @abstractmethod
    def show(self, df: pd.DataFrame):
        pass

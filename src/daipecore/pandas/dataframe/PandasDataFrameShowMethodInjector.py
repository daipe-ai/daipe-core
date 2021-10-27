from daipecore.pandas.dataframe.PandasDataFrameShowMethodInterface import PandasDataFrameShowMethodInterface


class PandasDataFrameShowMethodInjector:
    def __init__(self, data_frame_show: PandasDataFrameShowMethodInterface):
        self.__data_frame_show = data_frame_show

    def get(self):
        return self.__data_frame_show

#data cleaning
from datacollectionservice import DataCollectionService

import pandas as pd

#import retrieved data from data collection service

data_collection = DataCollectionService()

micro_view_data = data_collection.retrieve_data(data_source='datasource/BTCUSDT-klines-1h-2026-01-01_2026-07-16.csv')
macro_view_data = data_collection.retrieve_data(data_source='datasource/BTCUSDT-klines-4h-2026-01-01_2026-07-16.csv')

#import pandas as pd

micro_view_df = pd.DataFrame(micro_view_data)
macro_view_df = pd.DataFrame(macro_view_data)


def get_data_shape():
    #check shapes of the dataset

    micro_shape = micro_view_df.shape
    macro_shape = macro_view_df.shape

    return micro_shape, macro_shape


def get_data_info():
    return micro_view_df.info(), macro_view_df.info()


def find_duplicates():
    total_micro_duplicate_rows = micro_view_df.duplicated().sum()

    total_macro_duplicate_rows = macro_view_df.duplicated().sum()

    micro_duplicate_rows = micro_view_df[micro_view_df.duplicated()]
    macro_duplicate_rows = macro_view_df[macro_view_df.duplicated()]

    return total_micro_duplicate_rows, micro_duplicate_rows, total_macro_duplicate_rows, macro_duplicate_rows


def get_data_types():
    return micro_view_df.dtype, macro_view_df.dtype


def check_null_values():
    null_micros = micro_view_df.isnull().sum()
    null_macros = macro_view_df.isnull().sum()

    null_micro_view_rows = micro_view_df[micro_view_df.isnull()]
    null_macro_view_rows = macro_view_df[macro_view_df.isnull()]

    return null_micros, null_micro_view_rows, null_macros, null_macro_view_rows








#identify data source
#retrieve data from data source

#import pandas to read csv data source file
import pandas as pd

class DataCollectionService:

    @staticmethod
    def retrieve_data(data_source):
        retrieved_data = pd.read_csv(data_source)
        return retrieved_data
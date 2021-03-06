"""This module takes take of transforming raw .csv files to a clean Pandas DataFrame."""


from logger import logger
import pandas as pd


class CreateEventData:
    """
    Contains all methods and attributes to transform and combine raw .csv files to a Pandas dataframe,
    ready for insertion in the Cassandra database.
    """
    def __init__(self, csv_path_list: list):
        self.csv_path_list = csv_path_list
        self.data_types = {'artist': str,
                           'firstName': str,
                           'gender': str,
                           'itemInSession': int,
                           'lastName': str,
                           'length': float,
                           'level': str,
                           'location': str,
                           'sessionId': int,
                           'song': str,
                           'userId': int}
        self.target_columns = ['artist', 'firstName', 'gender', 'itemInSession', 'lastName', 'length',
                               'level', 'location', 'sessionId', 'song', 'userId', 'page']

    def data_pipeline(self) -> pd.DataFrame:
        """
        - transforms each .csv file to a Pandas DataFrame
        - check if the target columns are present in the dataframe and returns only the records where songs are played
        - converts the data to the correct data types
        - appends all dataframes and returns a single dataframe
        """
        logger.info("Data pipeline started...")

        return_df = pd.DataFrame(columns=self.target_columns[:-1])

        for idx, csv_file in enumerate(self.csv_path_list, start=1):
            temp_df = self.csv_to_df(csv_file)
            temp_df = self.assert_target_columns(temp_df)

            return_df = return_df.append(temp_df, ignore_index=True)
            logger.debug(f"Processed {idx} / {len(self.csv_path_list)} .csv files")

        try:
            return_df = return_df.astype(self.data_types)
        except Exception:
            logger.exception("ERROR while casting columns to a specific type")
        else:
            return return_df

    @staticmethod
    def csv_to_df(file_path: str) -> pd.DataFrame:
        """
        Returns a Pandas dataframe based on a file path containing a .csv file.
        """
        try:
            df = pd.read_csv(file_path)
        except Exception:
            logger.exception(f"ERROR while reading in {file_path}")
        else:
            return df

    def assert_target_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Assert whether the target columns are present in the dataframe, and return only the records where songs
        were played.
        """
        df_columns_low = [x.lower() for x in df.columns]
        target_columns_low = [x.lower() for x in self.target_columns]
        found_cols = [x for x in target_columns_low if x in df_columns_low]

        try:
            sorted(found_cols) == sorted(target_columns_low)
        except AssertionError:
            logger.exception(f"ERROR the target columns and df columns do not match")
        else:
            return df.loc[df['page'] == 'NextSong', self.target_columns[:-1]]

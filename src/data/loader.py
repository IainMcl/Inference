import pandas as pd
import os
import shutil
from settings import BASE_DIR
from .format_converter import FormatConverter

# def load_data(data_file):
    # """
        # Read in the data. Takes the input data file name provided and reads 
        # into the data folder.
        # :param: data_file (str) file name/ path to input data MUST be either an
            # excel or csv file.
    # """
    # # Get file type
    # ext = os.path.splitext(data_file)[1]
    # print(ext)
    # formater = FormatConverter(data_file)
    # formater.excel_to_csv()

class Data(FormatConverter):
    def __init__(self, data_file):
        self.data_file = data_file
        self.file_name = os.path.basename(data_file)
        if not os.path.isfile(data_file):
            raise ValueError(f"Input file path not valid. The file {self.file_name}"
                    + f" can not be found in the current directory or at {self.data_file}.")
        self.format = os.path.splitext(data_file)[1]
        if self.format != ".xlsx" and self.format != ".csv":
            raise ValueError("Input file is not either a .csv or .xlsx." + 
                    f" File supplied {self.file_name}.")
        super().__init__(data_file)

    def load_data(self):
        """
            Load the data (data_file) in to the working folder /data/.
        """
        os.chdir(BASE_DIR)
        shutil.copy(self.data_file, os.path.join(BASE_DIR,
            f"/data/{self.file_name}")) 

    def clear(self):
        """
            Clears the current file from the data folder.
            For confidential data this should be done as soon as no longer 
            needed.
            :return: Returns 0 for success making sure that the loaded file has 
                been removed. Returns 1 if the file has not been removed.
        """
        os.remove(os.path.join(BASE_DIR, f"data/{self.file_name}"))
        if os.path.isfile(os.path.join(BASE_DIR, f"data/{self.file_name}")):
            return 1
        else:
            return 0

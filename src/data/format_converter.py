import pandas as pd
import os
import shutil
from settings import BASE_DIR 

class FormatConverter(object):
    """
        Allows for data to be converted between types (excel, csv) and storage
        locations.
        Working data files are stored in the /data/ folder. Temporary data is 
        stored in the /data/temp/ folder. 
    """
    def __init__(self, f_name):
        self.f_name = f_name
        self.ext_split = os.path.splitext(f_name)

    def excel_to_csv(self): 
        """
            Takes the input file name of the excel formated file and converts 
            the sheet to a csv file.
            The input data should be in the 'data/' folder and the output will 
            be placed in the 'data/temp' folder.
            Input data to this should be a .xlsx file.
        """
        if self.ext_split[1] != '.xlsx':
            raise ValueError("Input file is not .xlsx format.")
        no_ext = os.path.splitext(self.f_name)[0]
        read_file = pd.read_excel(os.path.join(BASE_DIR, f"data/{self.f_name}"))
        out_file_path = os.path.join(BASE_DIR, f"data/temp/{no_ext}.csv")
        read_file.to_csv(out_file_path, index=None, header=True)
        return out_file_path        

    def cvs_to_excel(self):
        """
           Takes the csv file from the '/data/temp folder and converts to a 
           .xlsx file back in the original 'data/' folder.
        """
        csv_file = os.path.join(BASE_DIR, f"data/temp/{self.ext_split[0]}.csv")
        if not os.path.isfile(csv_file):
            raise ValueError(f"""
                Trying to convert a file that dosen't exist. 
                {csv_file} can not be found.
                """)
        read_file = pd.read_csv(csv_file)
        out_file_path = os.path.join(BASE_DIR, f"data/{self.f_name}.xlsx") 
        read_file.to_exel(out_file_path)
        return out_file_path
    
    def data_to_temp(self):
        if os.path.isfile(os.path.join(BASE_DIR, f'data/{self.f_name}')):
            shutil.move(os.path.join(BASE_DIR, f'data/{self.f_name}'),
                os.path.join(BASE_DIR, f'data/temp/{self.f_name}'))
        else:
            raise ValueError(f"File not found in data folder: {self.f_name}")

    def temp_to_data(self):
        if os.path.isfile(os.path.join(BASE_DIR, f'data/temp/{self.f_name}')):
            shutil.move(os.path.join(BASE_DIR, f'data/temp/{self.f_name}'),
                os.path.join(BASE_DIR, f'data/{self.f_name}'))
        else:
            raise ValueError(f"File not found in data/temp folder: {self.f_name}")

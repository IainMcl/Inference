import os 
import sys
import argparse
from gui.gui import GUI

def main():
    os.environ.setdefault("INFERENCE_SETTINGS_MODULE", "settings")
    arg_list = ["read", "test"]
    parser = argparse.ArgumentParser(prog="manage.py", description="Inference:\
            a tool to infer missing data from its context")
    parser.add_argument("-d", "--data", help="File name of the data file stored in data/",
            type=str, action="store", default=False)
    parser.add_argument("-u", "--upload", help="Add this to upload data through the gui",
            action="store_true")
    parser.add_argument("-t", "--test", help="Runs all tests. For develpment use only", 
            action="store_true")
    args = parser.parse_args()
    if not args.data and args.upload:
        # start gui uploader
        gui = GUI()
    if args.data:
        # start some work with the data
        pass

if __name__ == "__main__":
    main()


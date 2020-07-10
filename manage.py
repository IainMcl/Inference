import os 
import sys
import argparse

def main():
    os.environ.setdefault("INFERENCE_SETTINGS_MODULE", "settings")
    arg_list = ["read", "test"]
    # use_string = ""/ 
            # "usage python manage.py command ...\n"/
            # "Inference: A tool to infer missing data from the datas context\n"/
            # "Options"/
            # "   command"/
            # "       read    read in a given data file"/
            # "       test    run system tests (development puorposes only)"
    # args = sys.argv[1:]
    # if len(args) == 0 or args[0] not in arg_list:
        # print(use_string)
        # return
    # if args[0] == arg_list[0]:
    parser = argparse.ArgumentParser(prog="manage.py", description="Inference:\
            a tool to infer missing data from its context")
    parser.add_option("test", help="Runs all tests. For develpment use only")
    args = parser.parse_args()

if __name__ == "__main__":
    main()


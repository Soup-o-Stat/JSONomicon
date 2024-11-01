import json
import argparse
import re
import sys
import time

ver="0.0.2"

def print_hello_message():
    print("       #  #######   ######   #    #                                                       ")
    time.sleep(0.2)
    print("       #  #     #   #   ##   ##   #                                                       ")
    time.sleep(0.2)
    print("       #  #         #   ##   ###  #  #######  #     #     #     #######  #######  #     #")
    time.sleep(0.2)
    print("      ##  #######  ##    #  ## ## #  #     #  ##   ##     #     #        #     #  ##    # ")
    time.sleep(0.2)
    print(" #    ##       ##  ##    #  ##  ###  #     #  # # # #     #     #        #     #  # ### # ")
    time.sleep(0.2)
    print(" #    ##  #    ##  ##    #  ##   ##  #     #  #  #  #     #     #        #     #  #    ## ")
    time.sleep(0.2)
    print(" #######  #######  #######  ##    #  #######  #     #     #     #######  #######  #     # ")
    time.sleep(0.2)
    print("Created by Soup-o-Stat")
    print()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_path", type=str)
    return parser.parse_args()

def read_input_file(input_file_path):
    with open(input_file_path, "r", encoding="utf-8") as file:
        return file.read()

def remove_comments(input_data):
    return re.sub(r'\{\-\s*.*?\s*\-\}', '', input_data, flags=re.DOTALL)

def parse_dict(input_data):
    #TODO сделать обработку словарей
    pass

def to_json(input_data):
    #TODO упаковка в json файл
    pass

def parse_this_bullshit(input_data):
    output_data = remove_comments(input_data)
    return output_data

def main():
    args = parse_args()
    try:
        input_data = read_input_file(args.input_file_path)
        json_data = parse_this_bullshit(input_data)
        print(json_data)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == '__main__':
    print_hello_message()
    main()
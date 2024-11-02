import json
import argparse
import re
import sys
import time

ver = "1.0"

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
    parser.add_argument("input_file_path", type=str, help="Path to the input file with configuration text")
    return parser.parse_args()

def read_input_file(input_file_path):
    with open(input_file_path, "r", encoding="utf-8") as file:
        return file.read()

def remove_comments(input_data):
    return re.sub(r'\{\-\s*.*?\s*\-\}', '', input_data, flags=re.DOTALL)

def parse_globals(input_data):
    globals_dict = {}
    matches = re.findall(r'global\s+([a-zA-Z][_a-zA-Z0-9]*)\s*=\s*("[^"]*"|\d+|true|false)', input_data)
    for name, value in matches:
        if value.isdigit():
            globals_dict[name] = int(value)
        elif value == "true":
            globals_dict[name] = True
        elif value == "false":
            globals_dict[name] = False
        else:
            globals_dict[name] = value.strip('"')
    return globals_dict

def parse_dict(input_data, globals_dict):
    output = {}
    dicts = re.findall(r'(\w+)\s*:\s*\(\[([^]]+)\]\)', input_data)

    for key, content in dicts:
        items = {}
        for item in re.findall(r'([a-zA-Z][_a-zA-Z0-9]*)\s*:\s*("[^"]*"|\d+|true|false|#\{[a-zA-Z][_a-zA-Z0-9]*\})',
                               content):
            item_key, item_value = item
            if item_value.startswith("#{") and item_value.endswith("}"):
                var_name = item_value[2:-1]
                item_value = globals_dict.get(var_name, None)
            elif item_value == "true":
                item_value = True
            elif item_value == "false":
                item_value = False
            elif item_value.isdigit():
                item_value = int(item_value)
            else:
                item_value = item_value.strip('"')
            items[item_key] = item_value
        output[key] = items

    return output

def main():
    args = parse_args()
    try:
        input_data = read_input_file(args.input_file_path)
        input_data = remove_comments(input_data)

        globals_dict = parse_globals(input_data)
        json_data = parse_dict(input_data, globals_dict)

        print(json.dumps(json_data, indent=4))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == '__main__':
    print_hello_message()
    main()
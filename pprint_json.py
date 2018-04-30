import json
import argparse
import sys

def load_data(filepath):
    json_content = None
    with open(filepath, 'r') as json_file:
        json_content = json.load(json_file)
        return json_content

def pretty_print_json(json_content):
    json.dump(json_content, sys.stdout, ensure_ascii=False, indent=4)

def add_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    return parser.parse_args()


if __name__ == '__main__':
    args = add_argument_parser
    json_content = load_data(args.filepath)
    if not json_content:
        print ("Unable to open file %s" % args.filepath)
    else:
        pretty_print_json(json_content)


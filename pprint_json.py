import json
import argparse
import sys

def load_data(filepath):
    try:
        file = open(filepath, 'r')
        json_content = json.load(f)
        file.close()
    except IOError:
        json_content = False
    finally:
        return json_content

def pretty_print_json(json_content):
    json.dump(json_content, sys.stdout, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    args = parser.parse_args()
    json_content = load_data(args.filepath)
    if not json_content:
        print ("Unable to open file %s" % args.filepath)
    else:
        pretty_print_json(json_content)


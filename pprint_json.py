import json
import argparse
import sys

def load_data(filepath):
    try:
        f = open(filepath, 'r')
        data = json.load(f)
        f.close()
    except Exception:
        data = False
    finally:
        return data

def pretty_print_json(data):
    json.dump(data, sys.stdout, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    args = parser.parse_args()
    data = load_data(args.filepath)
    if not data:
        print ("Unable to open file %s" % args.filepath)
    else:
        pretty_print_json(data)


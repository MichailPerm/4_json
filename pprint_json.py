import json
import argparse
import sys


def load_data(filepath):
    try:
        json_content = None
        with open(filepath, "r") as file:
            json_content = json.load(file)
            return json_content
    except json.decoder.JSONDecodeError:
        print("File {} does not contain json data.".format(filepath))
    except IOError:
        print("Unable to read file {}.".format(filepath))


def pretty_print_json(json_content):
    json.dump(json_content, sys.stdout, indent=4, ensure_ascii=False)


def create_args_parser(args):
    parser = argparse.ArgumentParser()
    for arg in args:
        parser.add_argument(arg)
    return parser


if __name__ == "__main__":
    parser = create_args_parser(["filepath"])
    args = parser.parse_args()
    json_content = load_data(args.filepath)
    if not json_content:
        sys.exit()
    else:
        pretty_print_json(json_content)

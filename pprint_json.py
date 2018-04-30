import json
import argparse
import sys


def load_data(filepath):
    json_content = None
    with open(filepath, "r") as file:
        json_content = json.load(file)
        return json_content


def pretty_print_json(json_content):
    json.dump(json_content, sys.stdout, indent=4, ensure_ascii=False)


def create_args_parser(argument):
    parser = argparse.ArgumentParser()
    parser.add_argument(argument)
    return parser.parse_args()


if __name__ == "__main__":
    args = create_args_parser("filepath")
    try:
        json_content = load_data(args.filepath)
    except json.decoder.JSONDecodeError:
        print("File {} does not contain json data.".format(args.filepath))
    except IOError:
        print("Unable to read file {}.".format(args.filepath))
    else:
        if not json_content:
            sys.exit()
        else:
            pretty_print_json(json_content)

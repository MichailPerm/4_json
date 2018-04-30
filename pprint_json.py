import json
import argparse
import sys


def load_data(filepath):
    with open(filepath, "r") as file:
        json_content = json.load(file)
        return json_content


def pretty_print_json(json_content):
    json.dump(json_content, sys.stdout, indent=4, ensure_ascii=False)


def create_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    return parser.parse_args()


if __name__ == "__main__":
    args = create_args_parser()
    try:
        json_content = load_data(args.filepath)
    except json.decoder.JSONDecodeError:
        print("File {} does not contain json data.".format(args.filepath))
    except IOError:
        print("Unable to read file {}.".format(args.filepath))
    else:
        if not json_content:
            sys.exit("Program finishd it's work, becasue of None json data.")
        else:
            pretty_print_json(json_content)

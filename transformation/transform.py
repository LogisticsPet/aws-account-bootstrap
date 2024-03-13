import json
import os
import argparse


def replace_with_fn_sub(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, str) and '${' in value:
                obj[key] = {"Fn::Sub": value}
            else:
                replace_with_fn_sub(value)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            if isinstance(item, str) and '${' in item:
                obj[i] = {"Fn::Sub": item}
            else:
                replace_with_fn_sub(item)
    return obj


def process_json(input_json):
    return replace_with_fn_sub(input_json)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-dir", help="Input directory containing JSON files", required=True)
    parser.add_argument("-o", "--output-dir", help="Output directory to store processed JSON files", required=True)
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.json'):
            input_file_path = os.path.join(input_dir, file_name)
            output_file_path = os.path.join(output_dir, file_name)

            with open(input_file_path, 'r') as f:
                input_json = json.load(f)

            content = process_json(input_json)

            with open(output_file_path, 'w') as f:
                json.dump(content, f, indent=2)

            print(f"Processed: {input_file_path} -> {output_file_path}")

    print("JSON transformation complete.")


if __name__ == "__main__":
    main()

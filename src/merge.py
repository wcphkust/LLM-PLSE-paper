import os
import json

def collect_json_files(directory):
    # Recursively collect all JSON files in the given directory and its subdirectories
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if not "application_labeled" in file:
                continue
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def merge_json_files(json_files):
    merged_data = {}
    for json_file in json_files:
        print(json_file)
        with open(json_file, 'r') as file:
            data = json.load(file)
            merged_data.update(data)
    return merged_data

def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage
directory = "/Users/xiangqian/Documents/Research/Workspace/LLM/LLM-PLSE-paper/src"
output_file = "merged_data.json"

json_files = collect_json_files(directory)
merged_data = merge_json_files(json_files)
save_to_json(merged_data, output_file)

print(f"Merged {len(json_files)} JSON files and saved to {output_file}")
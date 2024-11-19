import os
import json
from openai import *


def get_application_labeling_prompt(title: str, abstract: str):
    # read the content from prompt_application.txt
    with open("prompt_application.txt", "r") as file:
        prompt_application = file.read()
    return f"{prompt_application}\n\n" \
           f"Here is the title and abstract of a paper:\n\n" \
           f"Title: {title}\n\n" \
           f"Abstract: {abstract}\n\n" \
           f"Now please list the keywords that you think best describe the paper in one line and separate them with commas."



def collect_json_files(directory):
    # Recursively collect all JSON files in the given directory and its subdirectories
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files


def get_openai_response(prompt, key):
    client = OpenAI(api_key=key)
    try:
        model_input = [
            {
                "role": "system",
                "content": "You are good at catergozing papers and assign the keywords to them.",
            },
            {"role": "user", "content": prompt},
        ]
        response = client.chat.completions.create(
            model="gpt-4o-mini", messages=model_input, temperature=0.0
        )
        output = response.choices[0].message.content
        return output
    except Exception as e:
        return f"An error occurred: {e}"


def pre_process_json_files(json_files):
    matching_items = {}

    for json_file in json_files:
        with open(json_file, 'r') as file:
            data = json.load(file)
            for title, details in data.items():
                if details.get('type', '') == "software":
                    continue

                abstract = details.get('abstract', '').lower()
                if ('code' in abstract.replace("our code", "") or 'program' in abstract.replace("our code", "")) and \
                    (' llm' in abstract or ' large language model' in abstract):
                    details['venue'] = json_file.split("/")[-1].split(".")[0]
                    matching_items[title] = details
    return matching_items


def label_json_files(matching_items):
    labeled_data = {}
    cnt = 0

    for title, details in matching_items.items():
        cnt += 1
        if 0 <= cnt:
            prompt = get_application_labeling_prompt(title, details['abstract'])
            k = os.environ.get("OPENAI_API_KEY").split(":")[0]
            response = get_openai_response(prompt, k)
            details['keywords'] = [keyword.strip().lower() for keyword in response.split(",")]
            print(f"Title: {title}\nKeywords: {details['keywords']}\n")
            if not "unrelated" in details['keywords']:
                labeled_data[title] = details
            print(response)
        

    # dump labled data to a json file
    save_to_json(labeled_data, "application_labeled_items.json")
        

def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage
directory = "../absdata"
output_file = "sample.json"

# json_files = collect_json_files(directory)
# matching_items = pre_process_json_files(json_files)
# save_to_json(matching_items, output_file)

# print(len(matching_items))

# print(f"Processed {len(json_files)} JSON files and saved matching items to {output_file}")

# load from output_file
with open(directory + "/sample/" + output_file, 'r') as file:
    matching_items = json.load(file)

# print(matching_items)

label_json_files(matching_items)
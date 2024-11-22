import os
import json
import re
import pandas as pd

def collect_json_files(directory):
    """Recursively collects all JSON files from a directory."""
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def extract_titles_and_links(json_files):
    """Extracts the title and link of each paper from JSON files."""
    papers = []

    # Path to the uploaded README.md file
    file_path = '../README.md'

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Regex pattern to match titles and links
    pattern = r"- (.*?)\.\s.*\[\[Link\]\]\((.*?)\)"

    # Find all matches
    matches = re.findall(pattern, content)

    # Create a DataFrame
    df = pd.DataFrame(matches, columns=["title", "link"])

    # Convert the DataFrame to a list of dictionaries
    papers = df.to_dict(orient="records")
    return papers

def diff_papers(papers):
    updated_dict = {}
    with open('../data/labeldata/labeldata.json', 'r') as file:
        try:
            data = json.load(file)
            for title, details in data.items():
                link = details.get("url", "No Link Available")
                updated_dict[title] = details
                if link == "No Link Available":
                    for paper in papers:
                        if title.lower() == paper["title"].lower():
                            updated_dict[title]["url"] = paper["link"]
                            break
                if link not in papers:
                    print(f"Title: {title}\nLink: {link}\n")
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file: {file}")

    #save updated_dict to a updated_labeldata.json
    with open('../data/labeldata/updated_labeldata.json', 'w') as file:
        json.dump(updated_dict, file, indent=4)

def main():
    input_directory = '../data/labeldata'
    json_files = collect_json_files(input_directory)
    papers = extract_titles_and_links(json_files)

    for paper in papers:
        print(f"Title: {paper['title']}")
        print(f"Link: {paper['link']}\n")

    diff_papers(papers)

if __name__ == "__main__":
    main()
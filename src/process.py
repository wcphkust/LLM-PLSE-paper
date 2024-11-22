import os
import json
from collections import defaultdict

def collect_json_files(directory):
    """Recursively collects all JSON files from a directory."""
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def extract_papers_by_venue(json_files):
    """Extracts and categorizes papers from JSON files by venue."""
    venue_dict = defaultdict(list)
    
    for json_file in json_files:
        with open(json_file, 'r') as f:
            try:
                data = json.load(f)
                for title in data:
                    paper = data[title]
                    venue = paper.get("venue", "Unknown Venue")
                    venue_dict[venue].append({
                        "title": title,
                        "author": paper.get("author", "Unknown Author"),
                        "abstract": paper.get("abstract", "No Abstract Available"),
                        "url": paper.get("url", "No Link Available"),
                        "venue": paper.get("venue"),
                        "labels": paper.get("labels", [])
                    })
            except json.JSONDecodeError:
                print(f"Error decoding JSON in file: {json_file}")
    return venue_dict

def export_papers_to_readme(venue_dict, output_dir):
    """Creates directories for venues, saves papers as markdown files, and generates a README.md."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    title_to_path = {}
    venue_to_path = {}

    label_set = set([])
    
    for venue, papers in venue_dict.items():
        venue_dir = os.path.join(output_dir, venue.replace('/', '_'))
        os.makedirs(venue_dir, exist_ok=True)
        
        readme_path = os.path.join(venue_dir, "README.md")

        with open(readme_path, "w") as readme_file:
            readme_file.write(f"# {venue}\n\n")
            readme_file.write(f"Number of papers: {len(papers)}\n\n")
            
            for idx, paper in enumerate(papers, start=1):
                markdown_filename = f"paper_{idx}.md"
                markdown_path = os.path.join(venue_dir, markdown_filename)
                
                # Save individual paper as a markdown file
                with open(markdown_path, "w") as paper_file:
                    paper_file.write(f"# {paper['title']}\n\n")
                    paper_file.write(f"**Authors**: {paper['author']}\n\n")
                    paper_file.write(f"**Abstract**:\n\n{paper['abstract']}\n\n")
                    paper_file.write(f"**Link**: [Read Paper]({paper['url']})\n\n")

                    labels_with_links = []
                    for label in paper['labels']:
                        labels_with_links.append(f"[{label}](../../labels/{label.replace(' ', '_')}.md)")
                    paper_file.write(f"**Labels**: {', '.join(labels_with_links)}\n")
                
                # Add entry to README.md
                readme_file.write(f"## [{paper['title']}]({markdown_filename})\n")
                readme_file.write(f"- **Authors**: {paper['author']}\n")
                readme_file.write(f"- **Abstract**: {paper['abstract'][:300]}...\n")
                readme_file.write(f"- **Link**: [Read Paper]({paper['url']})\n")
                readme_file.write(f"- **Labels**: {', '.join(paper['labels'])}\n\n")
                label_set = label_set.union(set(paper['labels']))

                title_to_path[paper['title']] = markdown_path
                venue_to_path[venue] = readme_path
    return title_to_path, venue_to_path, label_set

def get_flattened_labels(label_dict):
    flattened_labels = {}
    for label in label_dict:
        flattened_labels[label] = label_dict[label]
        flattened_labels.update(get_flattened_labels(label_dict[label]))
    return flattened_labels

def generate_readme_from_label(label, categories, label_to_papers, title_to_path, venue_to_path, level=1):
    """
    Recursively generates a markdown content listing sub-labels of a given label.

    Args:
        label (str): The starting label.
        categories (dict): The categories dictionary from the JSON.
        level (int): The current header level for markdown.

    Returns:
        str: The markdown content.
    """    
    # The first letter of each word in label is capitalized
    capitalized_label = ' '.join([word.capitalize() for word in label.split()])

    content = f"{'#' * level} {capitalized_label}\n\n"

    flattened_labels = get_flattened_labels(categories)

    subcategories = flattened_labels[label]

    for sub_label in subcategories:
        content += generate_readme_from_label(sub_label, subcategories, label_to_papers, title_to_path, venue_to_path, level + 1) + "\n\n"

    paper_list = []
    if len(subcategories) == 0:
        for paper in label_to_papers[label]:
            paper_list.append(f"- [{paper['title']}]({title_to_path[paper['title']].replace('../data/papers/', '../')}), ([{paper['venue']}]({venue_to_path[paper['venue']].replace('../data/papers/', '../')}))\n")

    sorted_paper_list = sorted(paper_list)
    content += "\n\n".join(sorted_paper_list)
    
    return content


def get_all_labels(label_dict):
    all_labels = set([])
    for label in label_dict:
        all_labels.add(label)
        all_labels = all_labels.union(set(get_all_labels(label_dict[label])))
    return all_labels


def classify_papers_by_label(venue_dict, title_to_path, venue_to_path):
    # read category from ../data/category.json
    with open('../data/category.json', 'r') as f:
        label_category = json.load(f)["categories"]

    label_to_path = {}
    label_paper_dict = {}
    for venue in venue_dict:
        for paper in venue_dict[venue]:
            for label in paper['labels']:
                if label not in label_paper_dict:
                    label_paper_dict[label] = []
                label_paper_dict[label].append(paper)

    output_directory = '../data/papers/labels'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    labels = get_all_labels(label_category)

    for label in labels:
        # Generate the markdown content
        readme_content = generate_readme_from_label(label, label_category, label_paper_dict, title_to_path, venue_to_path)

        # Print or save the result
        print(readme_content)

        # Optionally, save to a markdown file
        output_path = os.path.join(output_directory, f"{label.replace(' ', '_')}.md")
        with open(output_path, 'w') as output_file:
            output_file.write(readme_content)
            label_to_path[label] = output_path
    return label_to_path


def main():
    input_directory = '../data/labeldata'
    output_directory = '../data/papers/venues'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    json_files = collect_json_files(input_directory)
    venue_dict = extract_papers_by_venue(json_files)
    title_to_path, venue_to_path, label_set = export_papers_to_readme(venue_dict, output_directory)

    classify_papers_by_label(venue_dict, title_to_path, venue_to_path)

    print(f"Exported papers to: {output_directory}")
    print(sorted(label_set))
    print(len(title_to_path))

if __name__ == "__main__":
    main()

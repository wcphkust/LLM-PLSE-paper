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
                    paper_file.write(f"**Labels**: {', '.join(paper['labels'])}\n")
                
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

def main():
    input_directory = '../data/labeldata'
    output_directory = '../data/papers'
    
    json_files = collect_json_files(input_directory)
    venue_dict = extract_papers_by_venue(json_files)
    title_to_path, venue_to_path, label_set = export_papers_to_readme(venue_dict, output_directory)

    print(f"Exported papers to: {output_directory}")
    print(sorted(label_set))
    print(len(title_to_path))

if __name__ == "__main__":
    main()

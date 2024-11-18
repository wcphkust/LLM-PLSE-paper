import re
import json

def parse_paper_metadata_with_sections(file_path):
    """
    Parse a Markdown file to extract paper metadata and include titles/subtitles.

    Args:
        file_path (str): Path to the Markdown file.

    Returns:
        list: A list of dictionaries containing paper metadata with section/subsection details.
    """
    heading_pattern = re.compile(r"(#+)\s+(.*)")
    paper_pattern = re.compile(r"(.*?[.?])\s+\((.*?)\s+(\d{4})\)\s+\[\[Link\]\]\((.*?)\)")


    papers = []
    sections = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        # Match headings to track sections and subsections
        heading_match = heading_pattern.match(line.strip())
        if heading_match:
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()

            # Update the section list based on heading level
            while len(sections) >= level:
                sections.pop()
            sections.append(title)

        # Match paper metadata
        elif paper_match := paper_pattern.match(line.strip()):
            title, conference, year, link = paper_match.groups()

            papers.append({
                "title": title.replace("- ", ""),
                "conference": conference,
                "year": int(year),
                "link": link,
                "sections": sections[:]  # Copy of the current sections
            })

        if line.startswith("-") and not (paper_match := paper_pattern.match(line.strip())):
            print(line)
            # break

    return papers

# Parse the file and print the extracted metadata
markdown_file_path = "README.md"  # Replace with the path to your Markdown file
papers_metadata = parse_paper_metadata_with_sections(markdown_file_path)

# Output the result as JSON
# print(json.dumps(papers_metadata, indent=4))

# dump paper_metadata to a json file
with open("paperbase.json", "w") as outfile:
    json.dump(papers_metadata, outfile, indent=4)

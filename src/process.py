import json
import os
import requests
from bs4 import BeautifulSoup
from openai import *

class Parser:
    def __init__(self):
        self.database = {}
        pass


    def parse_from_bib(self, bibpath):
        print(bibpath)
        with open(bibpath, 'r') as file:
            bib_tex = file.read()

        bib_tex = bib_tex.replace("{{", "{").replace("}}", "}").replace("{ ", "{").replace(" }", "}")
        venue_database = {}

        for entry_text in bib_tex.strip().split("\n@")[0:]:
            entry_type, rest = entry_text.split("{", 1)
            entry_dict = {}
            entry_dict["type"] = entry_type.strip("@").strip()  
            key, attributes = rest.split(",", 1)
            attributes = attributes.replace(", \n", ",\n")
            entry_dict["key"] = key.strip() 
            entry_dict["venue"] = bibpath.split("/")[-1].split(".")[0]
            attributes = attributes.rsplit("}", 1)[0]
            for attribute in attributes.split(",\n"):
                if "=" in attribute:
                    k, v = attribute.strip("\n").split("=", 1)
                    k = k.strip().strip("\n").strip().replace("\n", "")
                    v = v.strip().strip("\n").strip("{}").strip('"').strip(" ").strip(",").strip("}").replace("\n", "")\
                        .replace("                  ", " ")
                    entry_dict[k] = v
            if "title" not in entry_dict or "abstract" not in entry_dict:
                continue
            abstract = entry_dict["abstract"]
            if abstract != "":
                venue_database[entry_dict["title"]] = entry_dict

        self.database.update(venue_database)
        return venue_database


    def parse_ndss_html(self, htmlpath):
        with open(htmlpath, "r") as file:
            lines = file.readlines()

        venue_database = {}

        for line in lines:
            if "<a class=\"paper-link-abs\" href=" in line:
                index1 = line.find("<a class=\"paper-link-abs\" href=")
                index2 = line.find("><span")
                weblink = line[index1+32:index2-2]
                print(weblink)

                response = requests.get(weblink)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, "html.parser")
                    if soup:
                        entry_title = soup.find("h1", class_="entry-title").get_text(strip=True)
                        paper_data = soup.find("div", class_="paper-data")

                        author_list_str = paper_data.find("p").get_text(strip=True)
                        abstract = ""
                        for p in paper_data.find_all("p")[2:]:
                            abstract += p.get_text(strip=True)
                        authors = [author.split('(')[0].strip() for author in author_list_str.split(',')]
                        print(entry_title)
                        print(authors)
                        print(abstract)
                        print("\n")

                        venue_database[entry_title] = {
                            "type": "INPROCEEDINGS",
                            "key": "",
                            "author": " and ".join(authors),
                            "booktitle": htmlpath.split("/")[-1].replace(".html", ""),
                            "title": entry_title,
                            "year": htmlpath.split("/")[-1].replace(".html", "").replace("NDSS", "").replace("ndss", ""), 
                            "volume": "",
                            "number": "",
                            "pages": "",
                            "abstract": abstract,
                            "keywords": "",
                            "url": weblink,
                            "doi": "",
                            "ISSN": "",
                            "month": "",
                            "venue": htmlpath.split("/")[-1].replace(".html", "")
                        }
        self.database.update(venue_database)
        return
    

    def parse_acl_html(self, htmlpath, venue, year):
        prefix = str(year) + "." + venue.lower()

        with open(htmlpath, "r") as file:
            lines = file.readlines()

        venue_database = {}

        for line in lines:
            if "href=/" + prefix in line and ".bib" not in line:
                index1 = line.find("href=/")
                s1 = line[index1:]
                index2 = s1.find(">")
                weblink = "https://aclanthology.org/" + s1[6:index2-1]
                print(weblink)

                response = requests.get(weblink)
                title = ""
                venue_name = ""
                authors = []
                year = ""
                month = ""
                id = ""
                abstract = ""
                pdf_link = ""

                if response.status_code == 200:
                    for line in str(BeautifulSoup(response.content, "html.parser")).split("\n"):
                        if line.startswith("%T"):
                            title = line[3:].strip("\n").strip()
                        elif line.startswith("%A"):
                            authors.append(line[3:].strip("\n").strip())
                        elif line.startswith("%S"):
                            venue_name = line[3:].strip("\n").strip()
                        elif line.startswith("%D"):
                            year = line[3:].strip("\n").strip()
                        elif line.startswith("%8"):
                            month = line[3:].strip("\n").strip()
                        elif line.startswith("%F"):
                            id = line[3:].strip("\n").strip()
                        elif line.startswith("%X"):
                            abstract = line[3:].strip("\n").strip()
                        elif line.startswith("%U"):
                            pdf_link = line[3:].strip("\n").strip()
                    venue_database[title] = {
                            "type": "INPROCEEDINGS",
                            "key": id, 
                            "author": " and ".join(authors),
                            "booktitle": htmlpath.split("/")[-1].replace(".html", ""),
                            "title": title,
                            "year": year,
                            "volume": "",
                            "number": "",
                            "pages": "",
                            "abstract": abstract,
                            "keywords": "",
                            "url": pdf_link,
                            "doi": "",
                            "ISSN": "",
                            "month": month,
                            "venue": htmlpath.split("/")[-1].replace(".html", "")
                        }      
        self.database.update(venue_database)
        return


class Classifier:
    def __init__(self, database):
        self.database = database
        pass


    def keyword_match(self):
        matching_dict = {}
        for title in self.database:
            paper = self.database[title]
            if paper.get('type', '') == "software":
                continue
            abstract = paper.get('abstract', '').lower()
            if ('code' in abstract.replace("our code", "") or 'program' in abstract.replace("our code", "")) and \
                ('llm' in abstract or 'large language model' in abstract or 'pretrain' in abstract or 'transformer' in abstract or 'code model' in abstract):
                matching_dict[title] = paper
        return matching_dict
    
    @staticmethod
    def get_openai_response(prompt):
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY").split(":")[0])
        try:
            model_input = [
                {
                    "role": "system",
                    "content": "You are a senior CS researcher and good at categorizing papers.",
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
    
    def relevance_check(self, matching_dict):
        def get_prompt(title, abstract):
            prompt_template = """
            Please check whether a given paper is related to large language models for code. You should carefully read the abstract and title of the paper.
            If the paper concentrates on coding related tasks and leverage large language models, please answer YES. Otherwise, answer NO.
            Here are the title and abstract of the paper:
            [Title]: {title}
            [Abstract]: {abstract}
            Please think step by step and provide a clear explanation before concluding YES or NO.
            The output format is as follows:
            [Explanation]: Your explanation here.
            [Answer]: YES or NO.
            """
            return prompt_template.format(title=title, abstract=abstract)
        
        def parse_output(output):
            print(output)
            answer = output.split("[Answer]: ")[1]
            return answer
        
        related_papers = {}

        for title in matching_dict:
            paper = matching_dict[title]
            abstract = paper.get('abstract', '')
            prompt = get_prompt(title, abstract)
            output = Classifier.get_openai_response(prompt)
            answer = parse_output(output)
            if answer == "YES":
                related_papers[title] = paper
        return related_papers
        
    
    def label_with_llms(self):
        return


    def classify(self):
        matching_dict = classifier.keyword_match()
        print(len(matching_dict))
        
        related_papers = classifier.relevance_check(matching_dict)
        print(len(related_papers))
        
        # dump related papers to json
        with open("related_papers.json", "w") as file:
            json.dump(related_papers, file, indent=4)



if __name__ == "__main__":
    parser = Parser()

    bibs_with_abstract = [
        "../data/rawdata/2024/ICSE2024.bib",
        "../data/rawdata/2024/FSE2024.bib",
        "../data/rawdata/2024/ASE2024.bib",
        "../data/rawdata/2024/ISSTA2024.bib",
        "../data/rawdata/2024/TOSEM2024.bib",
        "../data/rawdata/2024/TSE2024.bib",
        "../data/rawdata/2024/PLDI2024.bib",
        "../data/rawdata/2024/OOPSLA2024.bib",
        "../data/rawdata/2024/S&P2024.bib",

        "../data/rawdata/2023/ICSE2023.bib",
        "../data/rawdata/2023/FSE2023.bib",
        "../data/rawdata/2023/ASE2023.bib",
        "../data/rawdata/2023/ISSTA2023.bib",
        "../data/rawdata/2023/TOSEM2023.bib",
        "../data/rawdata/2023/TSE2023.bib",
        "../data/rawdata/2023/PLDI2023.bib",
        "../data/rawdata/2023/OOPSLA2023.bib",
        "../data/rawdata/2023/S&P2023.bib",   
        "../data/rawdata/2023/USENIXSec2023.bib",
        "../data/rawdata/2023/CCS2023.bib",
    ]

    for bib_with_abstract in bibs_with_abstract:
        parser.parse_from_bib(bib_with_abstract)

    # parser.parse_ndss_html("../data/rawdata/2024/NDSS2024.html")
    # parser.parse_ndss_html("../data/rawdata/2023/NDSS2023.html")

    # parser.parse_acl_html("../data/rawdata/2023/ACL2023.html", "ACL", 2023)
    # parser.parse_acl_html("../data/rawdata/2023/EMNLP2023.html", "EMNLP", 2023)

    # parser.parse_acl_html("../data/rawdata/2024/ACL2024.html", "ACL", 2024)
    # parser.parse_acl_html("../data/rawdata/2024/NAACL2024.html", "NAACL", 2024)

    print(len(parser.database))

    classifier = Classifier(parser.database)
    classifier.classify()
    

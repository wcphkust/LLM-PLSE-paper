import fitz
import re
import json
from access import *
import requests
from bs4 import BeautifulSoup

class Parser:
    def __init__(self):
        # database: (venue, year) -> title -> abstract
        self.database = {}
        pass

    def parse_entry(self, file_path):
        if file_path.endswith("bib"):
            self.parse_from_bib(file_path)
        elif file_path.endswith("ris"):
            self.parse_from_ris_with_link(file_path)
        elif file_path.endswith("pdf"):
            self.parse_proceedings(file_path)
        elif file_path.endswith("html"):
            self.parse_html_file(file_path)
        else:
            print(f"Unknown entry type: {file_path}")


    def parse_from_bib(self, bibpath):
        with open(bibpath, 'r') as file:  # Replace with your file path
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
            attributes = attributes.rsplit("}", 1)[0]
            for attribute in attributes.split(",\n"):
                if "=" in attribute:
                    k, v = attribute.strip("\n").split("=", 1)
                    k = k.strip().strip("\n").strip().replace("\n", "")
                    v = v.strip().strip("\n").strip("{}").strip('"').strip(" ").strip(",").strip("}").replace("\n", "")\
                        .replace("                  ", " ")
                    entry_dict[k] = v
            if "title" not in entry_dict:
                continue
            abstract = entry_dict["abstract"]
            if abstract != "":
                venue_database[entry_dict["title"]] = entry_dict

        absdata_json_path = bibpath.replace(".bib", ".json").replace("rawdata", "absdata")
        with open(absdata_json_path, "w") as file:
            json.dump(venue_database, file, indent=4)
        return venue_database


    def parse_ndss_html(self, htmlpath):
        with open(htmlpath, "r") as file:
            lines = file.readlines()

        venue_database = {}

        for line in lines:
            # print(line)
            if "<a class=\"paper-link-abs\" href=" in line:
                index1 = line.find("<a class=\"paper-link-abs\" href=")
                index2 = line.find("><span")
                weblink = line[index1+32:index2-2]
                print(weblink)

                # read the html content of weblink
                response = requests.get(weblink)
                if response.status_code == 200:
                    # Parse the HTML content using BeautifulSoup
                    soup = BeautifulSoup(response.content, "html.parser")
                    if soup:
                        entry_title = soup.find("h1", class_="entry-title").get_text(strip=True)
                        paper_data = soup.find("div", class_="paper-data")

                        # Extract the author list and abstract
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
                            "month": ""
                        }
        absdata_json_path = htmlpath.replace(".html", ".json").replace("rawdata", "absdata")
        with open(absdata_json_path, "w") as file:
            json.dump(venue_database, file, indent=4)
        return
    
    def parse_acl_html(self, htmlpath, venue, year):
        prefix = str(year) + "." + venue.lower()

        prefix = "2024.findings-emnlp"

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

                # read the html content of weblink
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
                    # Parse the HTML content using BeautifulSoup
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
                            "month": month
                        }
        absdata_json_path = htmlpath.replace(".html", ".json").replace("rawdata", "absdata")
        with open(absdata_json_path, "w") as file:
            json.dump(venue_database, file, indent=4)
        return

    def parse_from_ris_with_link(self, rispath):
        with open(rispath, "r") as file:
            lines = file.readlines()
        for line in lines:
            if line.startswith("UR"):
                pdf_path = line.split(" ")[1].strip()
                self.extract_text_from_pdf(pdf_path)
                break
        return


    def parse_single_pdf_file(self, pdfpath):
        with fitz.open(pdfpath) as pdf:
            text = ""
            for page_num in range(pdf.page_count):
                page = pdf[page_num]
                text += page.get_text()
        # print(text[text.index("ABSTRACT"):text.index("CCS CONCEPTS")])
        return


    def parse_proceedings(self, proceedingspdf):
        with fitz.open(proceedingspdf) as pdf:
            text = ""
            for page_num in range(pdf.page_count):
                page = pdf[page_num]
                text += page.get_text()
        # print(text[text.index("ABSTRACT"):text.index("CCS CONCEPTS")])
        return


    def parse_html_file(self, htmlpath):
        if "NDSS" in htmlpath:
            self.parse_ndss_html(htmlpath)
        if "ACL" in htmlpath or "NAACL" in htmlpath or "EMNLP" in htmlpath:
            self.parse_acl_html(htmlpath)
        return
    

if __name__ == "__main__":
    parser = Parser()

    # bibs_with_abstract = [
    #     "../rawdata/2024/ICSE2024.bib",
    #     "../rawdata/2024/FSE2024.bib",
    #     "../rawdata/2024/ASE2024.bib",
    #     "../rawdata/2024/ISSTA2024.bib",
    #     "../rawdata/2024/TOSEM2024.bib",
    #     "../rawdata/2024/TSE2024.bib",
    #     "../rawdata/2024/PLDI2024.bib",
    #     "../rawdata/2024/OOPSLA2024.bib",
    #     "../rawdata/2024/S&P2024.bib",

    #     "../rawdata/2023/ICSE2023.bib",
    #     "../rawdata/2023/FSE2023.bib",
    #     "../rawdata/2023/ASE2023.bib",
    #     "../rawdata/2023/ISSTA2023.bib",
    #     "../rawdata/2023/TOSEM2023.bib",
    #     "../rawdata/2023/TSE2023.bib",
    #     "../rawdata/2023/PLDI2023.bib",
    #     "../rawdata/2023/OOPSLA2023.bib",
    #     "../rawdata/2023/S&P2023.bib",   
    #     "../rawdata/2023/USENIXSec2023.bib",
    #     "../rawdata/2023/CCS2023.bib",
    # ]

    # for bib_with_abstract in bibs_with_abstract:
    #     parser.parse_entry(bib_with_abstract)

    # parser.parse_entry("../rawdata/2024/NDSS2024.html")
    # parser.parse_entry("../rawdata/2023/NDSS2023.html")

    # parser.parse_acl_html("../rawdata/2023/ACL2023.html", "ACL", 2023)
    # parser.parse_acl_html("../rawdata/2023/EMNLP2023.html", "EMNLP", 2023)

    # parser.parse_acl_html("../rawdata/2024/ACL2024.html", "ACL", 2024)
    # parser.parse_acl_html("../rawdata/2024/NAACL2024.html", "NAACL", 2024)
    # parser.parse_acl_html("../rawdata/2024/EMNLP-findings2024.html", "EMNLP", 2024)
    # parser.parse_acl_html("../rawdata/2024/EMNLP-main2024.html", "EMNLP", 2024)

    parser.parse_entry("../rawdata/sample/sample.bib")
# 2023/09/22 11:32:01  zt
'''
Programe description:
    - Extract all the citation keys from the word document.
    - Find all the citation entries in the Zotero bib lib file and output these
      entries in a seperate bib file.
Reference:
    - Play with word document
      https://dadoverflow.com/2022/01/30/parsing-word-documents-with-python/
    - Create bib files
      https://github.com/sciunto-org/python-bibtexparser/issues/399
'''
import zipfile
import xml.etree.ElementTree as ET
import json
import argparse
import bibtexparser

import sys
import os

def docParser(docFile):
    '''Extract citations from word document
    '''

    doc = zipfile.ZipFile(docFile).read('word/document.xml')
    root = ET.fromstring(doc)

    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    # Find the XML "body" tag
    body = root.find('w:body', ns)
    # Under the body tag, find all the paragraph sections
    p_sections = body.findall('w:p', ns) 

    citeText = []

    # Find all the citation items
    for p in p_sections:
        instrText = p.findall(".//w:instrText",ns)

        for item in instrText:
            text = item.text
            # Put all text to a list
            citeText.append(text)

    citeKeys = extractCitations(citeText)

    return citeKeys

def extractCitations(citeText):
    '''Extract citation-key from the text string
    '''

    text = "".join(citeText)
    items =  text.split('"')
    citeKeys = []

    # Find the index of citation-key
    #iCK = items.index('citation-key')
    indicies = [i for i, item in enumerate(items) if item == "citation-key"]
    
    for i in indicies:
        citeKeys.append(items[i+2])

    # Remove duplicate items
    citeKeys = set(citeKeys)

    return citeKeys

def extractBibfile(citeKeys,bib_file_name):
    '''Export bib file containing all the citation entries from the zotero library
    '''

    bib_lib = bibtexparser.parse_file(bib_file_name)

    export_lib = bibtexparser.parse_string("")
    for entry in bib_lib.entries:
        for key in citeKeys:
            if key == entry.key:
                export_lib.add(entry)
                break

    bibtexparser.write_file("output.bib",export_lib)

    return

def getArgs():
    """Built scripts command line arguments
    """
    parser = argparse.ArgumentParser(
                description = "wordCitationExporter: A utility to extract citaion keys from the word document"
                )

    parser.add_argument(
            '-f',
            '--file',
            type = str,
            help = " Zotero automatic exported better bibtex lib file.",
            required = True
            )

    parser.add_argument(
            '-d',
            '--document',
            type = str,
            help = " Original word document.",
            required = True
            )

    return(parser.parse_args())

def main():
    
    args = getArgs()

    bib_file_name = args.file

    #docFile = "LES-spray-flow-EN-v2-manuscript.docx"
    doc_file = args.document

    citeKeys = docParser(doc_file)

    extractBibfile(citeKeys,bib_file_name)

if __name__ == "__main__":
    main()   


from typing import List
import zipfile
import xml.etree.ElementTree as ET
import json

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

    citations = []

    # Find all the citation items
    for p in p_sections:
        instrText = p.findall(".//w:instrText",ns)

        for item in instrText:
            text = item.text
            # Check whether the instrText is citation
            if "citation-key" in text:
                key = extractCitations(text)
                print(key)

    return

def extractCitations(text):
    '''Extract citation-key from the text string
    '''

    print(text)
    items =  text.split('"')

    # Find the index of citation-key
    iCK = items.index('citation-key')

    citeKey = items[iCK+2]

    return citeKey

def main():
   
    #docFile = sys.args()[1]
    docFile = "LES-spray-flow-EN-v2-manuscript.docx"

    docParser(docFile)

if __name__ == "__main__":
    main()   

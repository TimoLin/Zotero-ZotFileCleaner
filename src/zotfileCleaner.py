# 2023/08/07 16:42:47  zt
"""Zotfile cleaner
Program description:
    -  Find pdf files that are locally stored in Zotero database.
"""

import sys
import os
import bibtexparser
import argparse
from send2trash import send2trash

def bibReader(file_name):
    '''Read the bib library
    Parameters:
        file_name: bib library file name
    Returns:
        bib_lib: database contains all the items
    '''
    bib_lib = bibtexparser.parse_file(file_name)

    return bib_lib

def checkLocalFile(bib_lib, custom_location, flag_empty):
    '''Check pdf files locally stored in Zotero database
    Parameters:
        bib_lib: bib library database
        custom_location: Custom folder defined in Zotfile plugin
        local_files:
    '''
    
    local_files = []
    empty_files = []

    for entry in bib_lib.entries:
        try: 
            if not entry['file'].startswith(custom_location):
                local_files.append(entry)
        except KeyError:
            empty_files.append(entry)

    # Print result
    print("Citation keys of the files in Zotero database: {0}".format(len(local_files)))
    for f in local_files:
        print(" ",f.key)

    if (flag_empty):
        print("-"*45)
        print("Citation keys of items without attachment files: {0}".format(len(empty_files)))
        for f in empty_files:
            print(" ",f.key)

def filterZombieFiles(bib_lib, custom_location, flag_clean=False):
    """Filter these attachment files that have been deleted in Zotero but still
    exist in ZotFile.
    """
    # Get the complete file list in ZotFile `custom location`
    file_list = []
    for root, _, files in os.walk(custom_location):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)

    # Get the complete attachments file list in Zotero library
    lib_file_list = []
    for entry in bib_lib.entries:
        try:
            # In case there are multiple attachments in one entry
            files = entry['file'].split(";")
            for file in files:
                lib_file_list.append(file)
        except KeyError:
            # Empty items
            pass
    
    # Find the files of ZotFile that are not in Zotero library
    file_zombies = list(set(file_list)-set(lib_file_list))
    print("-"*45)
    print("ZotFile zombie files: {0}".format(len(file_zombies)))

    if (flag_clean):
        print("-"*45)
        print("Moving Zombie Files to Trash...")
        for zombie in file_zombies:
            print(" ", zombie)
            send2trash(zombie)

    return

def getArgs():
    """Built scripts command line arguments
    """
    parser = argparse.ArgumentParser(
                description = "ZotFileCleaner: An utility to find pdf files that are locally stored in Zotero database instead of ZotFile custom locations."
                )

    parser.add_argument(
            '-f',
            '--file',
            type = str,
            help = " Zotero automatic exported better bibtex lib file.",
            required = True
            )

    parser.add_argument(
            '-c',
            '--customlocation',
            type = str,
            help = " Custom location defined in ZotFile preferences.",
            required = True
            )

    parser.add_argument(
            '-e',
            '--empty',
            action = 'store_true',
            help = " Print items without any attachment files.",
            required = False
            )

    parser.add_argument(
            '-d',
            '--delete',
            action = 'store_true',
            help = " Clean up the zombie files under ZotFile folder .",
            required = False
            )


    return(parser.parse_args())

def main():

    # rootPath = os.path.abspath(".")
    # bib_file_name = os.path.join(rootPath,"mylib.bib")
    # custom_location = "$HOME/Dropbox/Zotero"

    args = getArgs()

    bib_file_name = args.file
    custom_location = args.customlocation
    flag_empty = args.empty
    flag_clean = args.delete

    bib_lib = bibReader(bib_file_name)
    
    checkLocalFile(bib_lib,custom_location,flag_empty)

    filterZombieFiles(bib_lib, custom_location, flag_clean)

    print("Done!")

if __name__ == "__main__":

    main()

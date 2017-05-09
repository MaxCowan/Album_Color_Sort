# Author: Max Cowan 2017

import subprocess
import csv
import os

#
ALBUM_LIST_FILE = "AOTD_info_list.csv"
# Target resolution for cover downloads
IMG_RES = 600

# Open the csv file with artist and album
with open(ALBUM_LIST_FILE, 'r') as csvfile:

    # Split the file into an array where each line in the file is an element
    # that has two sub elements (artist and album)
    data = [row for row in csv.reader(csvfile.read().splitlines())]

    os.chdir("Cover_Images/")  # Change directory to cover images

    invaidChars = ".,[]{}()!;'*?&@#$%^<>|/\:"  # Characters we don't want in file names

    for entry in data:
        artist = str(entry[0])  # Store artist name
        album = str(entry[1])   # Store album name

        # Delete all invalid characters
        for char in invaidChars:
            if char in artist:
                artist = artist.replace(char, '')
            if char in album:
                album = album.replace(char, '')

        # Delete any quotes
        artist.replace('"', "")
        album.replace('"', "")

        # Generate the SACAD command for the subprocess
        command_string = 'sacad "' + artist + '" "' + album + '" ' + str(IMG_RES) + ' ' + \
                         album.replace(" ", "_") + '.jpg'

        # Initialize the subprocess
        process = subprocess.call(command_string, shell=True)

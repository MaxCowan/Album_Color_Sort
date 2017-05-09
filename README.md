# Album_Color_Sort
A set of Python scripts to download and sort album artwork by color

This specific set of scripts was designed for a friend, Jack Canaday, who has created a massive spreadsheet containing
his analysis on a wide variety of discography as part of his 'Album of the Day' project. To view his work, visit this google sheets link: https://goo.gl/qnNMIz 

## Customization
To adapt this to your own music library, you will need to create a .csv file in the root project folder that emulates the format of the one I have provided (containing all of the album of the day info). This format is simply "artist,album" for every line. Make sure to change the ALBUM_LIST_FILE variable in 'cover_downloader.py' to the name of your csv file. Additionaly, to change the length (in pixels) of the downloaded cover artwork, change the IMG_RES variable to whatever integer resolution youd like (anticipate issues if you choose a very large resolution).

## 1. Dependencies:
* Python 3.X 
* OpenCV 3.X (including NumPy)
* sacad ```pip3 install sacad```

## 2. Instructions for operation:

* i.) Make sure both the 'Cover_Images' and 'Sorted_Cover_Images' folders in the proect are empty
* ii.) Open a terminal or command prompt session
* iii.) Navigate to the 'AlbumColorSort' project folder
* iv.) Run the command ```Python cover_downloader.py```
* v.) Once all album covers (or just some if you wish) have been downloaded, run the command:	```Python sorter.py```
* vi.) Open the 'Sorted_Cover_Images' folder to view the albums sorted by color!


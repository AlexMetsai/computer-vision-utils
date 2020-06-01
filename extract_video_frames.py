'''
Extract the frames of all videos in the current working directory.
A separate folder is created for each video, where frames are extracted.
If "Folder exists" we chose NOT to replace it, but instead display the
"FileExistsError". This will avoid potential loss of files.

Copyright (C) 2019 Alexandros I. Metsai
alexmetsai@gmail.com

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 3
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import cv2, os

if __name__ == '__main__':

    # Continue only if user replies "Yes"
    print("\nThis script will create a separate directory for ALL video"+
      " files in your working dir!! Are you sure you want to continue? (y/n)")
    x = input()
    if (x!='y' and x!='Y'): exit()
    
    # More video formats can be added, if necessary.
    ext = (".mp4", ".mkv", ".avi", ".3gp", ".mov", ".flv")
    
    # Create a separate directory for every video
    # and extract all of its frames inside.
    for file in os.listdir("."):
        if file.endswith(ext):
            print("Processing " + file)
            video_capture = cv2.VideoCapture(file)
            sucess, image = video_capture.read()
            folder_name = file#.replace(".mp4","")# no longer deleting extentions
            os.mkdir(folder_name)                 # Create directory
            count = 1
            success = True
            while success:
                cv2.imwrite(folder_name + "/%d.jpg" % count, image)
                success, image = video_capture.read()   # Read next frame
                count+=1
    
    print("Extraction finished")

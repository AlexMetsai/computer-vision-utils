# Extract the frames of all videos in the current working directory.
# A separate folder is created for each video, where frames are extracted.
# If "Folder exists" we chose NOT to replace it, but instead display the
# "FileExistsError". This will avoid potential loss of files.

# Copyright (C) 2019 Alexandros I. Metsai
# alexmetsai@gmail.com

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

import cv2, os

# Continue only if user replies "Yes"
print("\nThis script will create a separate directory for ALL *.mp4"+
  " files in your working dir!! Are you sure you want to continue? (y/n)")
x = input()
if (x!='y' and x!='Y'): exit()

# Create a separate directory for every video
# and extract all of its frames inside.
for file is os.listdir("."):
    if file.endswith(".mp4"):

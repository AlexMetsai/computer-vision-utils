"""
Extract the frames of all videos in the provided directory.
A separate folder is created for each video, where frames are extracted.
If "Folder exists" we chose NOT to replace it, but instead display the
"FileExistsError". This will avoid potential loss of files.

Copyright (C) 2019 - 2021 Alexandros I. Metsai
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
"""

import os
import cv2


# Supported video formats. More can be added, if necessary.
extensions = (".mp4", ".mkv", ".avi", ".3gp", ".mov", ".flv")


def extract_video_frames(folder, ext=extensions):
    """
    This function extracts the frames of all videos under a given parent
    directory, creating a separate directory for each video.

    :param folder: The parent folder containing the videos
    :param ext: A list with the video extensions to be considered.
    :return None:
    """

    # Create a separate directory for every video
    # and extract all of its frames inside.
    for file in os.listdir(folder):
        if file.endswith(ext):
            print("Processing " + file)
            video_capture = cv2.VideoCapture(os.path.join(folder, file))
            success, image = video_capture.read()
            folder_name = os.path.join(folder, file + "_frames")
            os.mkdir(folder_name)  # Create directory
            count = 1
            success = True
            while success:
                cv2.imwrite(folder_name + "/%d.jpg" % count, image)
                success, image = video_capture.read()  # Read next frame
                count += 1


if __name__ == '__main__':

    # Continue only if user replies "Yes"
    print("\nThis script will create a separate directory for all video" +
          " files under your working directory. Are you sure you want to continue? (y/n)")
    x = input()
    if x not in ['y', 'Y']:
        exit()
    
    working_dir = 'dummy_folder'
    extract_video_frames(working_dir)

    print("Extraction finished")

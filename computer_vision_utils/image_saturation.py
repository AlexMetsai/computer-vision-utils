"""
Search recursively for all images in the current working directory 
and apply saturation, with regard to a user defined threshold.

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

from imageio import imread, imwrite


# Supported image formats. More can be added, if necessary.
extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")


def saturate_images(folder, ext=extensions, threshold=40):
    """
    Find all image bellow the provided directory and apply saturation using a
    threshold value. The original images are replaced.

    :param folder: The provided directory.
    :param ext: Supported image file formats.
    :param threshold: The threshold value. All pixels exceeding this will be saturated.
    :return None: The processed images replace the originals.
    """
    # Find all files bellow the working directory
    # and apply saturation, replacing their originals.
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith(ext):

                # Load image
                im_path = os.path.join(os.path.join(root, f))
                print("Saturating", im_path)
                im = imread(im_path)

                # Cover the case where the image is PNG by converting the image from RGBA to RGB.
                if len(im.shape) > 2 and im.shape[2] == 4:
                    im = cv2.cvtColor(im, cv2.COLOR_BGRA2BGR)

                # Saturate image
                # In the future, I should NOT be lazy and do this in a way more efficient than a triple loop.
                for i in range(im.shape[0]):
                    for j in range(im.shape[1]):
                        for k in range(im.shape[2]):
                            if im[i, j, k] > threshold:
                                im[i, j, j] = 255
                            else:
                                im[i, j, k] = 0

                # Save image
                imwrite(im_path, im)


if __name__ == '__main__':
  
    # Continue only if user replies "Yes".
    print("\nThis script will recursively saturate all images in your" +
          " current working directory. Are you sure you want to continue? (y/n)")
    x = input()
    if x not in ['y', "Y"]:
        exit()
  
    working_dir = 'dummy_folder'
    saturate_images(working_dir)

    print("All images saturated successfully.")

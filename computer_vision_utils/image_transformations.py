"""
Transform all images/frames inside a specific folder.
These transformations include rotations and flips.

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


import numpy as np
import cv2
import os

# Supported image formats. More can be added, if necessary.
extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")


class Flip:
    """
    Container class for flipping collections of images.
    """

    @staticmethod
    def horizontal_flip(folder_name, ext=extensions):
        """

        :param folder_name: The parent folder containing the images.
        :param ext: Supported image file formats.
        :return None: The processed images replace the originals.
        """
        for file in os.listdir(folder_name):
            if file.endswith(ext):
                # read image from disc
                im = cv2.imread(os.path.join(folder_name, file))

                # flip horizontaly
                im = cv2.flip(im, 1)

                # replace the original with the flipped image
                cv2.imwrite(os.path.join(folder_name, file), im)

        print("All images flipped successfully.")

    @staticmethod
    def vertical_flip(folder_name, ext=extensions):
        """

        :param folder_name: The parent folder containing the images.
        :param ext: Supported image file formats.
        :return None: The processed images replace the originals.
        """
        for file in os.listdir(folder_name):
            if file.endswith(ext):
                # read image from disc
                im = cv2.imread(os.path.join(folder_name, file))

                # flip vertically
                im = cv2.flip(im, 0)

                # replace the original with the flipped image
                cv2.imwrite(os.path.join(folder_name, file), im)

        print("All images flipped successfully.")


class Rotate:
    """
    Container class for rotating collections of images.
    """

    @staticmethod
    def rotate_90_degrees(folder_name, k=1, ext=extensions):
        """

        :param folder_name: The parent folder containing the images.
        :param k: The number of rotations, negative values signify negative rotation.
        :param ext: Supported image file formats.
        :return None: The processed images replace the originals.
        """
        for file in os.listdir(folder_name):
            if file.endswith(ext):
                # read image from disc
                im = cv2.imread(os.path.join(folder_name, file))

                # rotate by 90 degrees
                im = np.rot90(im, k)

                # replace the original wth the rotated image
                cv2.imwrite(os.path.join(folder_name, file), im)

        print("All images rotated successfully.")

    @staticmethod
    def rotate_180_degrees(folder_name, ext=extensions):
        """

        :param folder_name: The parent folder containing the images.
        :param ext: Supported image file formats.
        :return None: The processed images replace the originals.
        """
        for file in os.listdir(folder_name):
            if file.endswith(ext):
                # read image from disc
                im = cv2.imread(os.path.join(folder_name, file))

                # rotate by 180 degrees
                im = np.rot90(im)
                im = np.rot90(im)

                # replace the original with the rotated image
                cv2.imwrite(os.path.join(folder_name, file), im)

        print("All images rotated successfully.")


if __name__ == "__main__":
    folder = '../dummy'
    Flip.horizontal_flip(folder)
    Flip.vertical_flip(folder)
    Rotate.rotate_90_degrees(folder)
    Rotate.rotate_180_degrees(folder)

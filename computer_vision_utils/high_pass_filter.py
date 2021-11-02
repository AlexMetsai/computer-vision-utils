"""
Search recursively for all images and
pass them through a high pass filter.

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

from scipy import ndimage
from imageio import imread, imwrite


def high_pass_filter(image):
    """
    In order to make a highpass filter, a low pass filtered
    instance is subtracted from the original image. A gaussian
    filter "blurs" the original and acts as the low pass unit.
    :param image:
    :return highpass_image:
    """

    lowpass_image = ndimage.gaussian_filter(image, 3)
    highpass_image = image - lowpass_image
    return highpass_image


# Supported image formats. More can be added, if necessary.
extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")


def high_pass(folder, ext=extensions):
    """
    Find all images bellow the provided directory and pass
    them through a high pass filter, replacing their originals.

    :param folder: The provided directory.
    :param ext: Supported image file formats.
    :return None: The processed images replace the originals.
    """

    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith(ext):
                # load image
                im_path = os.path.join(os.path.join(root, f))
                im = imread(im_path)

                # apply the high pass filter
                filtered_im = high_pass_filter(im)

                # Save image
                imwrite(im_path, filtered_im)


if __name__ == '__main__':

    # Continue only if user replies "Yes"
    print("\nThis script will recursively manipulate all images under your" +
          " current working directory. Are you sure you want to continue? (y/n)")
    x = input()
    if x not in ['y', 'Y']:
        exit()

    working_dir = 'dummy_folder'
    high_pass(working_dir)

    print("All images processed successfully.")

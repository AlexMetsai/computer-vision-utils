"""
Convert all images current working dir to BGR.
If images are already in BGR, they will be converted to RGB.

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
import numpy as np

from imageio import imsave, imread


extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")


def rgb2bgr(im):
    bgr = np.zeros(im.shape, dtype=int)

    bgr[:, :, :] = im[:, :, :]
    bgr[:, :, 0] = im[:, :, 2]
    bgr[:, :, 1] = im[:, :, 1]
    bgr[:, :, 2] = im[:, :, 0]

    return bgr


def bgr2rgb_folder(folder, ext=extensions):
    
    # Find all files bellow the working directory and convert 
    # them to BGR, replacing their originals.
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith(ext):
                
                # load image
                im_path = os.path.join(os.path.join(root, f))
                print("Resizing " + im_path)
                im = imread(im_path)
                
                # RGB to BGR
                bgr_im = rgb2bgr(im)
                
                # Save image
                imsave(im_path, bgr_im)
                
    print("Resized all frames successfully.")


if __name__ == '__main__':
    pass

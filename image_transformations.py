# Transform all images/frames inside a specific fodler.
# These transformations include rotations and flips.

# Copyright (C) 2019 Alexandros I. Metsai
# alexmetsai@gmail.com

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

import numpy as np
import cv2
import os

def rotate_90_degrees(folder_name, k=1):
  
  for file in os.listdir(folder_name):
    
    # read image from disc
    im = cv2.imread(folder_name + "/" + file)
    
    # rotate by 90 degrees
    # k is the number of rotations.
    # pass k = -1 for negative rotation
    im = np.rot90(im, k)
    
    # replace the original wth the rotated image
    cv2.imwrite(folder_name + "/" + file, im)
    
    print("All frames rotated successfully.")

def rotate_180_degrees(folder_name):
  
  for file in os.listdir(folder_name):
    
    # read image from disc
    im = cv2.imread(folder_name + "/" + file)
    
    # rotate by 180 degrees
    im = np.rot90(im)
    im = np.rot90(im)
    
    # replace the original wth the rotated image
    cv2.imwrite(folder_name + "/" + file, im)
    
    print("All frames rotated successfully.")

def horizontal_flip(folder_name):
  # TODO
  for file in os.listdir(folder_name):
    
    # read image from disc
    im = cv2.imread(folder_name + "/" + file)


if __name__ == "__main__":
  pass

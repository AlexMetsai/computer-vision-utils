# Search recursively for all images and
# pass them through a high pass filter.

# Copyright (C) 2019 Alexandros I. Metsai
# alexmetsai@gmail.com

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

from scipy import ndimage
from scipy.misc import imsave, imread

def high_pass(im):
    # In order to make a highpass filter, a low pass filtered
    # instance is subtracted from the original image. A gaussian
    # filter "blurs" the original and acts as the low pass unit.
    lowpass_im = ndimage.gaussian_filter(im,3)
    highpass_im = im - lowpass_im
    return(highpass_im)

if __name__ == '__main__':
  
  # Continue only if user replies "Yes"
  print("\nThis script will recursively manipulate all images under your"+
  	" current working directory. Are you sure you want to continue? (y/n)")
  x= input()
  if (x!='y' and x!="Y"): exit()
  
  # Find all files bellow the working directory and pass them  
  # through a high pass filter, replacing their originals.

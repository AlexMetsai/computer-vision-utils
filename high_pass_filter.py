# Search recursively for all images and
# pass them through a high pass filter.

# Copyright (C) 2019 Alexandros I. Metsai
# alexmetsai@gmail.com

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
  for root, dirs, files in os.walk("."):
    for f in files:
      if f.endswith(".jpg"):
        # load image
        im_path = os.path.relpath(os.path.join(root, f), ".")
        print("Filtering " + im_path)
        im = imread(im_path)
        
        # apply the high pass filter
        filtered_im = high_pass(im)
        
        # Save image
        imsave(im_path, filtered_im)
print("All images processed successfully.")

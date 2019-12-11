'''
Search recursively for all images in the current working directory 
and apply saturation, with regard to a user defined threshold.

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

import os
from scipy.misc import imsave, imread

# Define saturation threshold
THRESHOLD = 40
# You can use other or a number of formats. To do
# so, create a list, example: [".jpg", ".png"]
ext = ".jpg" 

if __name__ == '__main__':
  
  # Continue only if user replies "Yes"
  print("\nThis script will recursively saturate all images in your"+
  	" current working directory. Are you sure you want to continue? (y/n)")
  x= input()
  if (x!='y' and x!="Y"): exit()
  
  # Find all files bellow the working directory
  # and apply saturation, replacing their originals.
  for root, dirs, files in os.walk("."):
    for f in files:
      if f.endswith(ext):
        
        # load image

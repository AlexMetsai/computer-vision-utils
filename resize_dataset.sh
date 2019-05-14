# Resize all images to the specified size.
# The data directory is hardcoded to avoid a possible
# catastrophe by running the script in an inappropriate way.
# There is no need for a hash-bang #! specifying the shell's
# type, the script will work for most standard shells.
#
# Copyright (C) 2019 Alexandros I. Metsai
# alexmetsai@gmail.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

SIZE="256x256"

# The bang '!' argument is used to ignore aspect ratio
# and therefore force resizing to the specified size.

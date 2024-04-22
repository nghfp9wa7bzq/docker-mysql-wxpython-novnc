#!/bin/bash

#    Copyright (C) 2024  nghfp9wa7bzq@gmail.com

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Build and/or install wxPython

cd /app/wxp_build/
source /venv/bin/activate
pip install -U six wheel setuptools

FILE=./wxPython-4.2.1-cp39-cp39-linux_x86_64.whl
if [ ! -f "$FILE" ]; then
    # Wheel does not exist.
    pip download wxPython
    pip wheel -v wxPython-*.tar.gz  2>&1 | tee build.log
fi

pip install wxPython-*.whl

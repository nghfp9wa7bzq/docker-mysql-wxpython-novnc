#    Copyright (C) 2023  https://github.com/bandi13 andras [at] drfekete [dot] net

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

# fix for clipboard being passed through
vncconfig -nowin &

if ls /opt/startup_scripts/*.sh 1> /dev/null 2>&1; then
  for f in /opt/startup_scripts/*.sh; do
    bash "$f" -H || (echo "Error with $f: $?" >> /var/log/x11vnc_entrypoint.log)
  done
fi
/usr/bin/fluxbox

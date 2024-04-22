#!/bin/bash

#    Copyright (C) 2023  https://github.com/bandi13 andras [at] drfekete [dot] net
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

OUR_IP=$(hostname -i)

# start VNC server (Uses VNC_PASSWD Docker ENV variable)
# This is created more securely without ENV, before this script runs
#mkdir -p $HOME/.vnc && echo "$VNC_PASSWD" | vncpasswd -f > $HOME/.vnc/passwd
# Remove potential lock files created from a previously stopped session
rm -rf /tmp/.X*
vncserver :0 -localhost no -nolisten -rfbauth $HOME/.vnc/passwd -xstartup /opt/x11vnc_entrypoint.sh
# start noVNC web server
/opt/noVNC/utils/novnc_proxy --vnc localhost:5900 --listen 5901 &

echo -e "\n\n------------------ VNC environment started ------------------"
echo -e "\nVNCSERVER started on DISPLAY= $DISPLAY \n\t=> connect via VNC viewer with $OUR_IP:5900"
echo -e "\nnoVNC HTML client started:\n\t=> connect via http://$OUR_IP:5901/?password=*****\n"

if [ -z "$1" ]; then
  tail -f /dev/null
else
  # unknown option ==> call command
  echo -e "\n\n------------------ EXECUTE COMMAND ------------------"
  echo "Executing command: '$@'"
  exec $@
fi

# syntax=docker/dockerfile:1.4

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

FROM python:3.11-bookworm AS runner

# Install OS-level dependencies for wxPyton
RUN set -eux; \
  apt-get update; \
  apt-get install -y --no-install-recommends \
    dpkg-dev \
    build-essential \
    python3-dev \
    freeglut3-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    libgstreamer-plugins-base1.0-dev \
    libgtk-3-dev libjpeg-dev \
    libnotify-dev \
    libpng-dev \
    libsdl2-dev \
    libsm-dev \
    libtiff-dev \
    libwebkit2gtk-4.0-dev \
    libxtst-dev \
  ; \
  rm -rf /var/lib/apt/lists/*

# Create the virtual environment
RUN python -m pip install --upgrade pip && pip install wheel
RUN pip install virtualenv
RUN python3 -m virtualenv /venv
ENV PATH=/venv/bin:$PATH

# Install Python dependencies
RUN mkdir -p /app/wxp_build
COPY wxp_build/ /app/wxp_build/
RUN bash /app/wxp_build/build.sh

WORKDIR /app
COPY requirements.txt .
# Make sure pip is up-to-date inside virtualenv
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# ----------
# VNC setup

# Have to declare args here and
# in the compose.yaml under service / service_name / build / args
# Also add the secrets.
ARG VNC_PASSWD_FILE
ARG DOCKER_ROOT_PASSWD_FILE
ARG DOCKER_USER_UID
ARG DOCKER_USER_NAME
ARG DOCKER_USER_PASSWD_FILE

# These ports need to be published explicitly too!
# for the VNC connection
EXPOSE 5900
# for the browser VNC client
EXPOSE 5901

# Make sure the dependencies are met
ENV APT_INSTALL_PRE="apt -o Acquire::ForceIPv4=true update && DEBIAN_FRONTEND=noninteractive apt -o Acquire::ForceIPv4=true install -y --no-install-recommends"
ENV APT_INSTALL_POST="&& apt clean -y && rm -rf /var/lib/apt/lists/*"
# Make sure the dependencies are met
RUN eval ${APT_INSTALL_PRE} tigervnc-standalone-server tigervnc-common tigervnc-tools fluxbox eterm xterm \
    git net-tools python3 python3-numpy ca-certificates scrot sudo ${APT_INSTALL_POST}

# Install VNC. Requires net-tools, python and python-numpy
RUN git clone --branch v1.4.0 --single-branch https://github.com/novnc/noVNC.git /opt/noVNC
RUN git clone --branch v0.11.0 --single-branch https://github.com/novnc/websockify.git /opt/noVNC/utils/websockify
RUN ln -s /opt/noVNC/vnc.html /opt/noVNC/index.html

# Add menu entries to the container
RUN echo "?package(bash):needs=\"X11\" section=\"DockerCustom\" title=\"Xterm\" command=\"xterm -ls -bg black -fg white\"" >> /usr/share/menu/custom-docker && update-menus

# Set timezone to UTC
RUN ln -snf /usr/share/zoneinfo/UTC /etc/localtime && echo UTC > /etc/timezone

# Add in a health status
HEALTHCHECK --start-period=10s CMD bash -c "if [ \"`pidof -x Xtigervnc | wc -l`\" == "1" ]; then exit 0; else exit 1; fi"

# Add in non-root user
RUN useradd -m -s /bin/bash -d /home/${DOCKER_USER_NAME} -g users -G sudo -u ${DOCKER_USER_UID} ${DOCKER_USER_NAME}
#RUN chown -R ${DOCKER_USER_NAME}:users /home/${DOCKER_USER_NAME} && chown ${DOCKER_USER_NAME}:users /opt
RUN chown ${DOCKER_USER_NAME}:users /opt
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN --mount=type=secret,required=true,id=frontend-root-password echo 'root:'$(cat $DOCKER_ROOT_PASSWD_FILE) | chpasswd
RUN --mount=type=secret,required=true,id=frontend-user-password echo ${DOCKER_USER_NAME}':'$(cat $DOCKER_USER_PASSWD_FILE) | chpasswd

# Create and save VNC password for docker user
RUN --mount=type=secret,required=true,id=vnc-password mkdir -p /home/${DOCKER_USER_NAME}/.vnc \
    && cat $VNC_PASSWD_FILE | vncpasswd -f > /home/${DOCKER_USER_NAME}/.vnc/passwd
RUN chown -R ${DOCKER_USER_NAME}:users /home/${DOCKER_USER_NAME}/.vnc

USER ${DOCKER_USER_NAME}

# Copy various files to their respective places
COPY --chown=${DOCKER_USER_NAME}:users container_startup.sh /opt/container_startup.sh
COPY --chown=${DOCKER_USER_NAME}:users x11vnc_entrypoint.sh /opt/x11vnc_entrypoint.sh

# Add execute permission
RUN chmod u+x /opt/container_startup.sh
RUN chmod u+x /opt/x11vnc_entrypoint.sh

# Subsequent images can put their scripts to run at startup here
RUN mkdir /opt/startup_scripts

ENTRYPOINT ["/opt/container_startup.sh"]

# Add command to be executed in bash, after VNC is up
# CMD [""]
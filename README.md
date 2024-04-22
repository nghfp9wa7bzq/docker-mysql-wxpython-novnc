# docker-mysql-wxpython-novnc  
A Docker project allowing GUI application development with wxPython.  
It has two containers:  
1. MySQL server  
2. VNC and noVNC server with Python + wxPython (inside virtualenv)  
  
### How to use  
  
1. [Install Docker.](https://docs.docker.com/get-docker/)  
2. Download this project.  
3. (Extract project folder and)  
Open a terminal and go into the project folder:  
`cd /path/to/project`  
4. The passwords for the install are stored in the `secrets` folder.  
This folder is NOT included in this repo.  
You have to create it, with the following files, each with only a password inside:  
   - db_root_password.txt  
   - db_user_password.txt  
   - frontend_root_password.txt  
   - frontend_user_password.txt  
   - vnc_password.txt
5. Open Docker Desktop / Settings / Resources / File sharing  
and add the project folder to Virtual file shares.  
This is needed to properly mount / bind the password files to the containers.   
6. Build containers:  
`docker compose build`  
(To build containers from scratch:  
`docker compose build --no-cache`)  
7. Run containers in the background:  
`docker compose up -d`  
8. Connect to noNVC with a web browser:  
`localhost:5901`  
(You can find the password in the `secrets` folder.)  
  
### Inside noVNC  
  
1. Open a terminal window from the menu.  
   (Right click / Applications / Shells / Bash)  
2. You should be in the app (or project) folder  
and see e.g. the following prompt:  
`docker@e0edfddbe17c:/app$`  
3. Run the start_app.sh:  
`bash start_app.sh`  
  
#### Caveats  
  
1. The app should autoconnect to the MySQL server with the settings found in the `db/settings.py`.  
If the connection fails, compare the `setting.py` DATABASE_HOST with the names from:  
`docker ps`  
(Both containers should be running and listed.)  
2. Security in general should be carefully investigated.  
e.g. change to MySQL sha passwords  
3. The MySQL container has a script with the docker user password,  
that doesn't get deleted after the build process...  
4. The app, or rather wxPython [throws a Segmentation Fault](https://github.com/wxWidgets/Phoenix/issues/2455) with Python 3.12, when exiting.  
Using 3.11 for now.  
  
### TODO  
  
1. Security  
2. Build a wxpython wheel and use that to install it.  
(Reduces the build time.)
3. Use separate container for noVNC.  
  
### History  
  
This was a small project to learn Docker and wxPython.  
I have spent around 40 hours on the former and 10 on the latter.  
Both had / have bad quality documentation.  
Sure, there is a reference, but basic usage concepts are not explained. :(  
e.g. How Docker has two types of mounts, one for the build process, one to use after the container is already built.  
OR How wxPython sizers work - layout fundamentals...  
I would not recommend using wxPython.  
By now, it seems to be a dead project.  
Just look at its github page...  
  
### Links  
  
[Dockerfile reference](https://docs.docker.com/reference/dockerfile)  
[Dockerfile: From Start to Optimized (DockerCon 2023) - YouTube](https://www.youtube.com/watch?v=saSJa9YVroA)  
[Explore Docker's Container Image Repository | Docker Hub](https://hub.docker.com)  
[mysql - Official Image | Docker Hub](https://hub.docker.com/_/mysql)  
[adminer - Official Image | Docker Hub](https://hub.docker.com/_/adminer)  
[python - Official Image | Docker Hub](https://hub.docker.com/_/python)  
[Overview of wxPython | wxPython](https://wxpython.org/pages/overview/)  
[Building wxPython for Linux via Pip | wxPython](https://wxpython.org/blog/2017-08-17-builds-for-linux-with-pip/index.html)  
[wxPython demo - HUGE help!](https://extras.wxpython.org/wxPython4/extras/4.2.1/)  
[LearnSizers1 - wxPyWiki (Layout manager)](https://wiki.wxpython.org/LearnSizers1)  
[virtualenv](https://virtualenv.pypa.io/en/latest/)  
[gui-docker - noVNC project](https://github.com/bandi13/gui-docker)  
[theasp/novnc - Docker Image | Docker Hub](https://hub.docker.com/r/theasp/novnc)  
[x11docker](https://github.com/mviereck/x11docker)  

### Credits  
  
Parts of the Dockerfile content comes from the docs and from official image codes.  
Using the [Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/sakila-introduction.html).  
Parts of the wxPython code comes from the demo projects.  
The noVNC part comes from the gui-docker repo.  
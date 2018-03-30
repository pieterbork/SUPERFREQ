# SUPERFREQ
2017/2018 CU Boulder Team SUPERFREQ Repository

Below you will find a wide range of documentation

## Major Supported Systems

###### Linux Family: Debian(Raspbian)/Fedora/Arch

###### Windows

###### macOS

## HackRF Installation alongside using Flask

The goal was to make building and deploying this application as easy as possible, and only using a pentoo installation to use gnuradio was getting to be a pain...so we decided to go with docker.


1. See Building the Docker Image [System_Here] Sections for Installing Docker on your respective system

2. Download Docker Files: `git clone https://github.com/pieterbork/docker-superfreq.git`
   
   a) Local Install: `sudo docker build -t superfreq:latest .`

   b) The install location for the docker image can be found in variable (usually in /dev on Linux machines)
   
   c) To see the image run: `docker images --all`

   d) For more information see: https://docs.docker.com/engine/reference/commandline/images/#filtering
   
3. Run the docker container: `sudo docker run --name sf -it --privileged -p 80:5000 -v /dev/bus/usb:/dev/bus/usb superfreq bash`
   
   a) If it already exists, remove it and run again: `sudo docker rm sf` 

4. First, plug in the hackrf run `hackrf_info` - you should see information about your hackrf board.

   a) Now you're ready to collect some data!

Right now Wifi, Zigbee, and Bluetooth scanning are implemented with various libraries.

There is an example app in the directory: SUPERFREQ/src/hackrf/SDR_Testing/

After navigating to this directory, just run `python app.py` and visit `127.0.0.1` in your browser.

Check `/tmp/out_frames` and you may see some decoded Wifi metadata information. 

###### If you wish to run solely in the terminal use alias inside docker container `sfterm`

## Python Code Development

Please run the following command on any Debian/Ubuntu system to ensure your work environment is clean: `sudo apt-get install python-pip python-dev`


###### Building the Docker Image on Raspbian

To develop for this project on Raspbian the following steps must be taken

1. Download the docker image: curl -sSL https://get.docker.com | sh
   - Debugging error issue: N: Skipping acquire of configured file 'edge/binary-i386/Packages' as repository 'https://download.docker.com/linux/debian stretch InRelease' doesn't support architecture 'i386'
     - Solution: cd `/etc/apt/sources.list.d/docker.list` and change the docker.list file to: "deb [arch=amd64] https://download.docker.com/linux/debian stretch edge" the important thing here is to change arch to `amd64`
2. Install the docker image
   - Run `sudo apt-get update`
   - Run `sudo apt-get install docker-ce`
3. Check install
   - `sudo docker run hello-world`

#Add Pieter's stuff here

To find information on the docker-image

Sources: https://docs.docker.com/install/linux/docker-ce/debian/#install-docker-ce-1

###### Python Library Dependencies on Debian/Ubuntu

In doing this project, we felt the need to document Python Libraries that are not included into a default Python installation. Thus, our project includes:

1. Flask 
   - Installed by: `pip install flask`
2. Matplotlib
   - Installed by: `python2.7 -m pip install -U matplotlib` or `sudo apt-get install python-matplotlib`
3. SQLITE
   - Installed by: `sudo apt-get install sqlite3 libsqlite3-dev`


If you are running into errors, try the below troubleshooting:

- Check you have the latest version of Pip installed
   - CMD: First run: `pip --version` 
     - If < 9.0.1 (as of 02/13/2018) run: `pip install --upgrade pip`
   - Else follow the below troubleshooting steps
     - Run: `python -m pip install --upgrade pip setuptools wheel`

###### TO FIX

Terminal Development
1. Fixing Pie Chart coloring in Raspbian distributions

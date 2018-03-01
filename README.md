# SUPERFREQ
2017/2018 CU Boulder Team SUPERFREQ Repository

Below you will find a wide range of documentation

## HackRF Code Development

The goal was to make building and deploying this application as easy as possible, and only using a pentoo installation to use gnuradio was getting to be a pain...so we decided to go with docker.

Integration is still in progress, but here's the basics of getting set up.

1. Install docker (easily available from most package managers)

2. Obtain a copy of the gnuradio:latest docker image by either
   
   a) Building gnuradio:latest using [this](https://github.com/pieterbork/docker-gnuradio) Dockerfile (This takes a decent amount of time).
   
   b) Pulling from a docker repository (currently only Pieter's computer).
   
3. Build the [docker-superfreq image](https://github.com/pieterbork/docker-superfreq)
   
Using the docker run commands given in the docker-superfreq documentation, you should end up with a bash shell inside of the superfreq docker container. 

Let's test some things, and then we'll run some actual code!

First, plug in the hackrf run `hackrf_info` - you should see information about your hackrf board.

If you see errors complaining about connecting to X servers, you probably aren't passing your display through which I explain in the docker-supfreq docs.

Next, cd your way to `SUPERFREQ/src/hackrf/SDR_Testing/` and try running `python wifi_rx_rftap_nogrc.py`.

If you see a gray box appear with no information and things printing out in your terminal - that's awesome!

Check `/tmp/out_frames` and you may see some decoded Wifi metadata information. 

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
1. Handling Keyboard interrupts in main app
2. Fixing Pie Chart coloring

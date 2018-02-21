# SUPERFREQ
2017/2018 CU Boulder Team SUPERFREQ Repository

Below you will find a wide range of documentation

## HackRF Code Development

###### HackRF Library Dependencies on ???? 

## Python Code Development

Please run the following command on any Debian/Ubuntu system to ensure your work environment is clean: `sudo apt-get install python-pip python-dev`

###### Python Library Dependencies on Debian/Ubuntu

In doing this project, we felt the need to document Python Libraries that are not included into a default Python installation. Thus, our project includes:

1. Flask 
   - Installed by: `pip install flask`
2. Matplotlib
   - Installed by: `python2.7 -m pip install -U matplotlib` or `sudo apt-get install python-matplotlib`


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
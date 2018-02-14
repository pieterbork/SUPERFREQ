# SUPERFREQ
2017/2018 CU Boulder Team SUPERFREQ Repository

Below you will find a wide range of documentation

## HackRF Code Development

###### HackRF Library Dependencies on ???? 

## Python Code Development

###### Python Library Dependencies on Debian/Ubuntu

In doing this project, we felt the need to document Python Libraries that are not included into a default Python installation. Thus, our project includes:

1. Flask 
   - Installed by: `pip install flask`


If you are running into errors, try the below troubleshooting:

- Check you have the latest version of Pip installed
   - CMD: First run: `pip --version` 
     - If < 9.0.1 (as of 02/13/2018) run: `pip install --upgrade pip`
   - Else follow the below troubleshooting steps
     - Run: `python -m pip install --upgrade pip setuptools wheel`
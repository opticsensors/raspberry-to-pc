# `rpi_connectivity`
This repository contains the code necessary to send the data acquired using a DATAQ Instruments DAQ to a cloud service (Google Drive, OneDrive, ...) using a Raspberry Pi.

## Setup Raspberry Pi
To copy files to cloud (tried only with google drive) we have to install first:

```
sudo apt install rclone
```

We create a virtual python enviroment for executing the code:
```
python3 -m venv ~/py_env           # to create venv
source ~/py_env/bin/activate      # to activate venv
deactivate                         # to exit venv
```

Install pandas (and numpy):
```
pip install pandas
```

Install custom package for controlling DATAQ systems:

```shell
git clone https://github.com/opticsensors/daq_connectivity.git
cd daq_connectivity
pip install .     # this is run in the repo directory
```

Install code for copying files to google drive:
```shell
cd ..
git clone https://github.com/opticsensors/raspberry-to-pc.git
```


## Getting started

Run the script x.py to congifure username and password and check if id is working correctly!
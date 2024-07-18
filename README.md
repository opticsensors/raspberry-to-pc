# `rpi_connectivity`
This repository contains the code necessary to send the data acquired using a DATAQ Instruments DAQ to a cloud service (Google Drive, OneDrive, ...) using a Raspberry Pi.

## Getting started

Run the following command for clonning the repository from GitHub:

```shell
git clone https://github.com/opticsensors/raspberry-to-pc.git
```

Then, in the Raspberry Pi terminal run the following commands:

1. Make sure  you have the latest version of pip and PyPA’s build installed:
   ```shell
   python3 pip install --upgrade pip
   python3 pip install --upgrade build
   ```

3. Install additional packages using `clone`:
    ```shell
    git clone https://github.com/opticsensors/daq_connectivity.git
    python3 pip install .     # run this in the repo directory
    ```


## draft notes
pip install cannot be done directly on the rpi, we need to create a virtual env (note that sudo pip install or sudo python file.py cannot be used in venv):
```
python3 -m venv ~/daq_env  # only the first time
source ~/daq_env/bin/activate
deactivate   # only to exit venv
```

I had to do this cmd in order to pip install numpy and pandas:
```
sudo apt-get install libopenblas-dev
```

In order to push and pull from one of my repos via ssh in my rpi I had to create a fine grained token and do this:

```
git clone https://opticsensors:<MYTOKEN>@github.com/opticsensors/daq_connectivity.git 
git remote set-url origin https://opticsensors:<MYTOKEN>@github.com/opticsensors/daq_connectivity.git
```

To copy files to cloud (tried only with google drive) we have to install first:

```
sudo apt install rclone
```

To launch a python script on startup for raspberrypi we have to do:
```
sudo contrab -e
```

We edit the file to add the following line:
```
reboot python3 /home/pi/Desktop/.../file.py
```

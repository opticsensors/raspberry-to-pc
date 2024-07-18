import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import csv
import os
import datetime
import time
import daq_connectivity as daq 

output_mode = 'binary'
binary_method = 1
repeat_length = 25

path_to_save = "C:\\Users\\eduard.almar\\OneDrive - EURECAT\\Escritorio\\proyectos\\7. Suricata\\repo\\daq_connectivity\\logger"
date_name = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.')
file_path = os.path.join(path_to_save, f'{date_name}.csv')

usb = daq.Daq_serial(channels=[0,], voltage_ranges=[0.2,], dec=15,deca=3, srate=6000, output_mode=output_mode)
usb.config_daq()

# Initialize empty lists to store data
x_vals = []
ch1_data = []
# ch2_data = []
# ch3_data = []
# ch4_data = []

def process_data(frame):
    values = usb.collect_data(binary_method)
    if values:
        x_vals.append(float(frame))
        ch1_data.append(values[0])
        # ch2_data.append(values[1])
        # ch3_data.append(values[2])
        # ch4_data.append(values[3])
        print(f'Time: {time.time()}, Val 1: {values[0]}') #, Val 2: {values[2]}, Val 3: {values[3]}')


# Create a function to update the plot
def update_plot(frame):
    process_data(frame)
    plt.cla()
    plt.plot(x_vals, ch1_data, label='Val 1')
    # plt.plot(x_vals, ch2_data, label='Val 2')
    # plt.plot(x_vals, ch3_data, label='Val 3')
    # plt.plot(x_vals, ch4_data, label='Val 4')
    plt.xlabel('Time')
    plt.ylabel('Sensor Values')
    plt.legend()

    if frame>repeat_length:
        lim = plt.xlim(frame-repeat_length, frame)
    else:
        lim = plt.xlim(0,repeat_length)

# Create a function to save data to a CSV file when the plot window is closed
def on_close(event):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Time', 'Val1', 'Val2', 'Val3', 'Val4'])
        for x, s1, s2, s3, s4 in zip(x_vals, ch1_data, ): #ch2_data, ch3_data, ch4_data):
            writer.writerow([x, s1, s2, s3, s4])

# Register the callback function for when the plot window is closed
fig, ax = plt.subplots()
fig.canvas.mpl_connect('close_event', on_close)

ani = FuncAnimation(fig, update_plot, interval=100, blit=False)
plt.show()
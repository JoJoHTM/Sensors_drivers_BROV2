## Python script to launch all the sensors drivers publisher ##
# Subprocess is use in python code to interact with the command shell.
# Here, the attribut "run" launch the command in the shell and wait for the end of the command.
import subprocess   

# colcon is use to build all the packets after. The packet sensor_interface is use to make an bridge between the messages of the probe and ROS
# The other packages use sensor_interface to have access to the value and publish them


## TODO: Add the battery code the same way the other sensor codes have. i.e. just include sensor_battery here 
subprocess.run("colcon build --packages-select sensor_interfaces sensor_thermometer sensor_barometer sensor_oxygen sensor_salinity",shell=True)
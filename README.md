# Sensor for Blue ROV2

Sensor-drivers and connection to ROS2 architecture [ROS2 Galactic](https://docs.ros.org/en/ros2_documentation/galactic/index.html).

This is a continuation of a previous groups code for developing sensors to work underwater with the BlueRobotics BlueROV-2.
Link to the original code: https://github.com/NathanLec/Sensors_drivers_BROV2

## Use

For a quick use, paste these commands
More details for each command come after

	cd dev_ws/
	git clone https://github.com/JoJoHTM/Sensors_drivers_BROV2
	sudo mv -v Sensors_drivers_BROV2/src/* src/
	sudo rm -r Sensors_drivers_BROV2/src/
	sudo mv -v Sensors_drivers_BROV2/*  .
	python3 init.py
	. install/setup.bash
	ros2 launch launch/sensor.launch.py

Go in the dev_ws/ folder
Import all the files with the command

	git clone https://github.com/JoJoHTM/Sensors_drivers_BROV2

Move the content of the src file if you already have one in the folder

	sudo mv -v Sensors_drivers_BROV2/src/* src/
	sudo rm -r Sensors_drivers_BROV2/src/
	sudo mv -v Sensors_drivers_BROV2/*  .

Build all the packages with init.py

	python3 init.py
	
Source the setup files

	. install/setup.bash
	
Launch the publishers

	ros2 launch launch/sensor.launch.py



To remove all of the files, go in dev_ws/ and paste this command

	sudo rm -r launch/ src/sensor_* README.md LICENSE Sensors_drivers_BROV2/
	
## Documentation on code

A lot of the comments made in the files of "sensor_thermometer" folder can be applied to the 
code for the other sensors. Because of this the comments for the temperature code is more
detailed than for the other sensors.

## Battery code

There have been some issues regarding the hardware for battery sensing, hence the code not 
being finished. Though it may not be finished, a lot of the setup is fixed. 
What mainly needs to be done is fill in the code in "battery_data_publisher_node.py", as
well as making necessary adjustments in "init.py" and launch file. 

## Sensor suite

Sensors used in this project:

* Barometer: Blue Robotics BAR30
* Thermometer: Blue Robotics Celsius Fast-Response
* Dissolved Oxygen probe: Atlas Scientific
* Connductivity probe: Atlas Scientific

## Barometer

Heavily based on the MS5837 library mentioned under [Libraries](#libraries).
Remember to enable I2C on the Raspberry Pi and connect on the correct pins!

## Thermometer

Heavily based on the TSYS01 library mentioned under [Libraries](#libraries).
Remember to enable I2C on the Raspberry Pi and connect on the correct pins!

## Disolve Oxygen

Based on a new library, called DOATLAS01, which was created with an heavily base on the TSYS01 library mentioned under [Libraries](#libraries).
Remember to enable I2C on the Raspberry Pi and connect on the correct pins!

## Conductivity

Based on a new library, called CATLAS01, which was created with an heavily base on the TSYS01 library mentioned under [Libraries](#libraries).
Remember to enable I2C on the Raspberry Pi and connect on the correct pins!

## Libraries

* [BlueRobotics MS5837 Python Library](https://github.com/bluerobotics/ms5837-python)
* [BlueRobotics TSYS01 Python Library](https://github.com/bluerobotics/tsys01-python)

## License
[MIT](https://choosealicense.com/licenses/mit/)
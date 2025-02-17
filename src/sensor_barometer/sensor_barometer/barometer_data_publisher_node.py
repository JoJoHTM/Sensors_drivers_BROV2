from rclpy.node import Node

# ms5837 needed in order to utilize the BlueRobotics MS5837 Python Library which must be installed
from sensor_barometer import ms5837
from sensor_interfaces.msg import Barometer
import time
import  re, uuid

class BarometerDataPublisher(Node):
    # Initializer 
    def __init__(self):
        super().__init__('BarometerDataPublisher')
        self.publisher_ = self.create_publisher(Barometer, 'barometer_data', 10)    # Creates a publisher over the topic barometer_data
        read_period = 2  # Does a reading every 2 seconds
        self.timer = self.create_timer(read_period, self.barometer_read_and_publish)

        self.sensor = ms5837.MS5837_30BA()
        # self.sensor.setFluidDensity() # Configuring fluid density for fresh or saltwater. Defaulting to fresh water
        if not self.sensor.init():
            # If sensor can not be detected
            print("Sensor could not be initialized")
            exit(1)

    def barometer_read_and_publish(self):
        # Custom barometer message to publish. Can be found in the sensor_interfaces.
        msg = Barometer()

        # Adding a way to read the time 
        tim = time.localtime()
        msg.local_time =  time.strftime("%H:%M",tim)

        # Getting the mac address of the system
        msg.mac = ':'.join(re.findall('..','%012x' % uuid.getnode()))


        # Reading barometer and loading data into custom message
        if self.sensor.read():
                msg.depth                   = self.sensor.depth()                               # Depth in meters using the fluid density (kg/m^3) configured by setFluidDensity()
                msg.pressure_mbar           = self.sensor.pressure()                            # Default is mbar (no arguments)
                msg.pressure_psi            = self.sensor.pressure(ms5837.UNITS_psi)            # Request psi
        else:
                print("Sensor read failed!")
                exit(1)

        # Publishing message and logging data sent over the topic /barometer_data
        self.publisher_.publish(msg)
        self.get_logger().info('Mac: %s  Depth: %0.2f m\tP: %0.1f mbar  %0.3f psi  %s' % (msg.mac,
                                                                                          msg.depth, 
                                                                                          msg.pressure_mbar, 
                                                                                          msg.pressure_psi,
                                                                                          msg.local_time))

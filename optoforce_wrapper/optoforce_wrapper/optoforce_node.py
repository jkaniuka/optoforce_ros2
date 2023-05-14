import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor, ParameterType
from ast import literal_eval
from geometry_msgs.msg import WrenchStamped
import random
#from optoforce import OptoForce16 as OptoForce


class OptoforcePublisher(Node):

    def __init__(self):
        super().__init__('optoforce_node')
        self.declare_parameter('sensor_serial_numbers', descriptor = ParameterDescriptor(type = ParameterType.PARAMETER_STRING_ARRAY))
        self.declare_parameter('port', descriptor = ParameterDescriptor(type = ParameterType.PARAMETER_STRING_ARRAY))
        self.declare_parameter('speed', descriptor = ParameterDescriptor(type = ParameterType.PARAMETER_INTEGER_ARRAY))
        self.declare_parameter('filter', descriptor = ParameterDescriptor(type = ParameterType.PARAMETER_INTEGER_ARRAY))
        self.declare_parameter('zero', descriptor = ParameterDescriptor(type = ParameterType.PARAMETER_BOOL_ARRAY))
        self.declare_parameter('scale', descriptor = ParameterDescriptor(type = ParameterType.PARAMETER_STRING))

        self.sensor_serial_numbers = self.get_parameter('sensor_serial_numbers').get_parameter_value().string_array_value
        self.port = self.get_parameter('port').get_parameter_value().string_array_value
        self.speed = self.get_parameter('speed').get_parameter_value().integer_array_value
        self.filter = self.get_parameter('filter').get_parameter_value().integer_array_value
        self.zero = self.get_parameter('zero').get_parameter_value().bool_array_value
        self.scale = literal_eval(self.get_parameter('scale').get_parameter_value().string_value)

        self.sensors = ["A", "B"] 
        self.pubs = []

        for i in range(len(self.sensor_serial_numbers)):
            #self.sensors.append(OptoForce(port = self.port[i], speed_hz=self.speed[i], filter_hz=self.filter[i], zero=self.zero[i]))
            self.pubs.append(self.create_publisher(WrenchStamped, 'optoforce_' + self.sensor_serial_numbers[i], 10))

        #timer_period = 1/max(self.speed)  # seconds
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.handle_sensors)

        
    

    def handle_sensors(self):
        
        try:
            for idx, sensor in enumerate(self.sensors):
                msg = WrenchStamped()
                msg.header.stamp = self.get_clock().now().to_msg()
                msg.header.frame_id = 'frame_' + self.sensor_serial_numbers[idx]
                #measurement = sensor.read(only_latest_data=True)
                measurement = [random.uniform(1.0, 100.0), random.uniform(1.0, 100.0), random.uniform(1.0, 100.0)]
                msg.wrench.force.x = measurement[0] / self.scale[idx][0]
                msg.wrench.force.y = measurement[1] / self.scale[idx][1]
                msg.wrench.force.z = measurement[2] / self.scale[idx][2]
                print(msg)
                self.pubs[idx].publish(msg)
        except:
            pass
        finally:
            # for sensor in self.sensors:
            #     sensor.close()
            pass




def main(args=None):
    rclpy.init(args=args)

    optoforce_publisher = OptoforcePublisher()

    rclpy.spin(optoforce_publisher)

    optoforce_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

SERIAL_PORT = "/dev/ttyUSB0"
BAUD = 115200

class MotorBridge(Node):
    def __init__(self):
        super().__init__('motor_bridge')

        self.declare_parameter('port', SERIAL_PORT)
        self.declare_parameter('baud', BAUD)

        port = self.get_parameter('port').value
        baud = int(self.get_parameter('baud').value)

        self.get_logger().info(f"Opening serial: {port} @ {baud}")
        self.ser = serial.Serial(port, baud, timeout=0.1)
        time.sleep(2.0)  # Arduino reset sonras? bekleme

        # /motor_cmd topic: "F", "B", "S", "0".."9"
        self.sub = self.create_subscription(String, '/motor_cmd', self.cb, 10)

    def cb(self, msg: String):
        data = (msg.data or "").strip()
        if not data:
            return

        # Sadece izinli komutlar? geçir
        allowed = set(list("FBS0123456789"))
        if any(ch not in allowed for ch in data):
            self.get_logger().warn(f"Rejected cmd: {data}")
            return

        # Arduino tek karakter bekliyor: ilk karakteri yolla
        cmd = data[0].encode('ascii', errors='ignore')
        self.ser.write(cmd)
        self.get_logger().info(f"Sent serial cmd: {data[0]}")

def main():
    rclpy.init()
    node = MotorBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            node.ser.write(b'S')
            node.ser.close()
        except Exception:
            pass
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

import sys
import termios
import tty

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

HELP = """
Tuşlar:
  w: ileri (F)
  s: geri (B)
  x: stop (S)
  0-9: hız seviyesi
  q: çıkış
"""

def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

class KeyPub(Node):
    def __init__(self):
        super().__init__('keyboard_pub')
        self.pub = self.create_publisher(String, '/motor_cmd', 10)
        self.get_logger().info(HELP)

    def send(self, s: str):
        msg = String()
        msg.data = s
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = KeyPub()
    try:
        while rclpy.ok():
            ch = getch()
            if ch == 'q':
                node.send('S')
                break
            elif ch == 'w':
                node.send('F')
            elif ch == 's':
                node.send('B')
            elif ch == 'x':
                node.send('S')
            elif ch.isdigit():
                node.send(ch)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

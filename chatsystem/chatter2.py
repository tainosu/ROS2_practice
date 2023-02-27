import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor

from std_msgs.msg import String

class ChatPublisher2(Node):

    def __init__(self):
        super().__init__('chat_publisher_2')
        self.publisher_ = self.create_publisher(String, '/chatter2', 10)
        timer_period = 0.5  #0.5秒周期
        self.create_timer(
            timer_period,
            self.timer_callback,
        )
        self.chat_str = ""

    def timer_callback(self):
        msg = String()
        self.chat_str = input()
        msg.data = self.chat_str 
        self.publisher_.publish(msg)
        self.get_logger().info(f'{msg.data} を送信しました。')

class ChatSubscriber2(Node):

    def __init__(self):
        super().__init__('chat_subscriber_2')
        self.create_subscription(
            String,
            '/chatter1_after',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'{msg.data} を受信しました。')

def main(args=None):
    rclpy.init(args=args)
    chat_publisher_2 = ChatPublisher2()
    chat_subscriber_2 = ChatSubscriber2()

    #1プロセスで複数ノードを動かす
    exec = MultiThreadedExecutor()
    chat_publisher_2 = ChatPublisher2()
    chat_subscriber_2 = ChatSubscriber2()
    exec.add_node(chat_publisher_2)
    exec.add_node(chat_subscriber_2)
    exec.spin()
    exec.shutdown()

    chat_publisher_2.destroy_node()
    chat_subscriber_2.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

#juman/knpを使いやすくしたライブラリ
from icdpyknp import KNP
from rich.console import Console

class Bunsetsu(Node):

    def __init__(self): 
        super().__init__('bunsetsu')
        self.publisher_ = self.create_publisher(String, '/chatter1_after', 10)
        self.subscription = self.create_subscription(String, '/chatter1_before', self.callback, 10)
        self.chat_str = ""

    def callback(self, msg):
        msg_before = msg.data
        console = Console()
        knp = KNP()
        result = knp.parse(msg_before)

        def order(result_list):
            for tok in result_list:
                if tok == result_list[-1]:
                    append_str = tok.midasi + "ね。"
                else:
                    append_str = tok.midasi + "ね、"
                self.chat_str += append_str

        order(result.bnst_list())
        msg.data = self.chat_str
        self.publisher_.publish(msg)
     
        self.chat_str = ""

def main(args=None):
    rclpy.init(args=args)
    bunsetsu = Bunsetsu()
    rclpy.spin(bunsetsu)
    bunsetsu.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

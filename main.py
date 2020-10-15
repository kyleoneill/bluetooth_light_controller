from dotenv import load_dotenv
import os
import controller
load_dotenv()

# sudo gatttool -b {address} --char-write-req -a 0x0015 -n 3305020000ff00ffae54000000000000000000ce


def main():
    strip_controller = controller.Controller(os.getenv("MAC_ADDRESS"))
    strip_controller.change_color((255, 0, 0))


main()

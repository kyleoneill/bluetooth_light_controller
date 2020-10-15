import os

handle = 21
handle_hex = "0x{:04x}".format(handle)


class Controller:
    def __init__(self, address):
        self.address = address

    def change_color(self, rgb):
        r, g, b = rgb
        assert 0 <= r <= 255
        assert 0 <= g <= 255
        assert 0 <= b <= 255
        assert ((r + g + b) == 255)
        hex_str = get_rgb_hex(r, g, b)
        write_data(self.address, hex_str)
        print(f"Changed color to {rgb}")


def get_rgb_hex(r, g, b):
    sig = (3*16 + 1) ^ r ^ g ^ b
    bins = [51, 5, 2, r, g, b, 0, 255, 174, 84, 0, 0, 0, 0, 0, 0, 0, 0, 0, sig]
    bins_str = map(int_to_hex, bins)
    return "".join(bins_str)


def int_to_hex(int_v):
    h = hex(int_v).replace("0x", "")
    while len(h) < 2:
        h = "0" + h
    return h


def write_data(address, data):
    cmd = f"gatttool -b {address} --char-write-req -a {handle_hex} -n {data}"
    print(cmd)
    os.system(cmd)
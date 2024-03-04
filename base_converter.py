"""
Mostly used, so I can convert my Spotify ID's from Base62 (with lowercase first) to Unicode
"""

HEX = "0123456789abcdef"
BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
BASE62_aA = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
UNICODE = "".join([chr(index) for index in range(0x110000)])
ASCII = UNICODE[:0x100]


def convert(data: (int, str), base: str = BASE62_aA):
    """
    Converts anything from int to anything and backwards.
    """
    if type(data) == str:
        result = 0
        for index in range(len(data)):
            result += base.index(data[index]) * len(base) ** (len(data) - index - 1)
        return result
    elif type(data) == int:
        result = ""
        while data > 0:
            result += base[data % len(base)]
            data = data // len(base)
        return result[::-1]


def convert_bin(data: (int, str)):
    return convert(data, "01")


def convert_hex(data: (int, str)):
    return convert(data.lower() if type(data) == str else data, HEX)

def convert_text(data: (int, str)):
    return convert(data, UNICODE)


def convert_spotify_to_unicode(data: str):
    return convert(convert(data, BASE62_aA), ASCII)

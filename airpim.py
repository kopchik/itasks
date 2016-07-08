#!/usr/bin/env python3

# Hypotesis: this an email or an URL
# ... And in airpim.com domain, probably...
# Clue: list(map(bin,map(ord,"airpim.com")))!


def decode(data, bits=7):
    # remove whitespaces
    lines = data.split()
    stream = "".join(lines)

    # very basic input validation
    assert (len(stream) % bits) == 0, \
        "data len is not multiple of %s" % bits

    result = []
    for ptr in range(0, len(stream), bits):
        chunk = stream[ptr:ptr + bits]
        num = int(chunk, base=2)
        result.append(chr(num))
    return "".join(result)


if __name__ == '__main__':
    data = """1101001110001111101001100100110000111110011110011011
            001001100000110001011011010000001100001110100111100
            101110000110100111011010101110110001111011111101101"""
    print(decode(data))
    print("and here is my contact:", 'LkAuZWFpY21nc21ybGVleG8=\n')

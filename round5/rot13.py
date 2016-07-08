#!/usr/bin/env python3

def rot13(s, base=13):
    """
    Encodes and decodes strings with ROT-13 (https://en.wikipedia.org/wiki/ROT13).

    Arguments:
      s -- string to encode/decode.
      base -- number of shifts to perform

    Returns:
      string representing encoded/decoded data.
    """
    decoded = []
    for c in s:
        newcode = ord(c) - ord('a') + base
        wrapped = newcode % 26 + ord('a')
        decoded.append(wrapped)
    # map integers to chars in ascii-table and form the string
    return "".join(map(chr, decoded))


def rot13_clever(s, base=13):
    """ Same as rot13, but in a short and obscure way. """
    return "".join(chr((ord(c) - ord('a') + base) % 26 + ord('a')) for c in s)


if __name__ == '__main__':
    encoded = "rkgerzr"
    decoded = "extreme"
    print(rot13_clever(encoded))

    # some basic tests
    assert rot13(encoded) == decoded, "ROT-13 decoding failed"
    assert rot13(decoded) == encoded, "ROT-13 encoding failed"

#!/usr/bin/env python3

def num_bits(num):
  bitsum = 0
  while num:
    bitsum += num % 2
    num //= 2
  return bitsum


def get_parity_table(bits):
  table = {}
  for x in range(2**bits):
    table[x] = num_bits(x)
  return table


def parity(num, table, bits):
  res = 0
  mask = 2**bits -1
  while num:
    res += (table[num & mask])
    num = (num >> bits)
    print("res", res)
  return res % 2


if __name__ == '__main__':
  table = get_parity_table(bits=4)
  print(table)
  print(parity(10001, table, bits=4))


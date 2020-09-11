#!/usr/bin/python

import sys

r = ['rock']
p = ['paper']
s = ['scissors']
rps = [r,p,s]

def rock_paper_scissors(n):
  if n <= 0:
      return [[]]
  elif n == 1:
      return rps
  else:
      return [result + rps[x] for result in rock_paper_scissors(n-1) for x in range(3)]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

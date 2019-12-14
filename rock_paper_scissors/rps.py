#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  result = []
  temp = []

  def rps_rec(n):
    if n == 0:
      nonlocal result
      result.append(temp[:])
      return
    
    plays = ['rock', 'paper', 'scissors']

    for play in plays:
      temp.append(play)
      rps_rec(n - 1)
      temp.pop()
  
  rps_rec(n)

  return result


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
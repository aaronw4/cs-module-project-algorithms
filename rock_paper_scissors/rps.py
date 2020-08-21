#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here

  def RPS_helper(n, arr=[[]]):
    count = n

    if count == 0:
      return arr
    else:
      new_arr = []
      for i in range(0, len(arr)):
        new_arr.append(arr[i] + ['rock'])
        new_arr.append(arr[i] + ['paper'])
        new_arr.append(arr[i] + ['scissors'])

      count -= 1

      return RPS_helper(count, new_arr)

  return RPS_helper(n)
  
  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
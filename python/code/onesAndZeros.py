'''
ONES AND ZEROS

from Codewars by user4386369

Given an array of ones and zeroes, convert the equivalent binary value to an integer.
Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:
  Testing: [0, 0, 0, 1] ==> 1
  Testing: [0, 0, 1, 0] ==> 2
  Testing: [0, 1, 0, 1] ==> 5
  Testing: [1, 0, 0, 1] ==> 9
  Testing: [0, 0, 1, 0] ==> 2
  Testing: [0, 1, 1, 0] ==> 6
  Testing: [1, 1, 1, 1] ==> 15
  Testing: [1, 0, 1, 1] ==> 11
'''

#soluttion
def binary_array_to_number(binArr):
  """Given an array of ones and zeroes, convert the equivalent binary value to an integer."""
  numArr = "".join(map(str,binArr))
  return int(numArr,2)

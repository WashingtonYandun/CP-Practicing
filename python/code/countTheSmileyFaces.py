'''
From Codewars by St3f4n @St3f4n

Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

  Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
  A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
  Every smiling face must have a smiling mouth that should be marked with either ) or D
  No additional characters are allowed except for those mentioned.

  Valid smiley face examples: :) :D ;-D :~)
  Invalid smiley faces: ;( :> :} :]

Example:

  countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
  countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
  countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
  
Note
  In case of an empty array return 0. You will not be tested with invalid input (input will always be an array).
  Order of the face (eyes, nose, mouth) elements will always be the same.
'''


#second solution (first solution refactored)
def count_smileys(arr):
  """count valid smileys from an array, better reading"""
  count = 0
  eyes = ":;"
  noses = "-~"
  smiles = ")D"
  for i in arr:
      if len(list(i)) > 2:
          if i[0] in eyes and i[1] in noses and i[2] in smiles:
              count += 1
      else:
          if i[0] in eyes and i[1] in smiles:
              count += 1
  return count
  
  
  #first solution
def count_smileys(arr):
  """count valid smileys from an array"""
  c = 0
  for i in arr:
      if len(list(i)) > 2:
          if i[0] in [":",";"] and i[1] in ["-","~"] and i[2] in [")","D"]:
              c += 1
      else:
          if i[0] in [":",";"] and i[1] in [")","D"]:
              c += 1
  return c

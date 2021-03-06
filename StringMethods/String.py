
'''
Useful String methods in Python
raw strings --> print(r'hello world') to not use escape sequence
string[n:m] to slice string from n to m - 1
the in, or operator
.upper() --> capitalize
.lower() --> lower case the string 
.isupper() --> check whether a string is capitalize
.islower() --> check whether a string is all lower cased
.isalpha() --> check whether a string contains all alphabets or not
.isalnum() --> check whether a string contains only alphabets and numbers
.isdecimal() --> check whether a string contains only decimal or numerical value
.startswith('args') --> check whether a string starts with 'args'
.endswith('args') --> check whether a string ends with 'args'
.join('arg1') return a single string value by concatenating all the string in the list arg1
.split('delim') return a list of each string value of the original string according to the delim value argument
.rjust(n) --> return a padded version of the string value by n space in front of string value
.ljust(n) --> similar to rjust() but to the left
  
'''
string = "Yes, indeed. It is called College. Where the transitory lands of the exhausted students converge. In venturing north, the pilgrims discover the truth of the old words. The GPA fades, and the homework goes unsolved. When the link of graduation is threatened, the bell tolls, unearthing the old lords of success from their graves. Wikipedia, saint of knowledge. Caffeine's sleepless legion, the one-nighters. And the reclusive lord of the drunk capital, Alcohol, the giant. Only in truth, the lords will barely do good, and the unhealthy will rise. Nameless accursed students, unfit even to be a functional part of society. And so it is that the student seeketh jobs."

print(string + '\n')
print(string.lower() + '\n')
print(string.upper() + '\n')
print('Captialized: ' + str (string.upper().isupper())) 
print('Lower cased: ' + str(string.lower().islower()))
print('Is alphabets: ' + str(string.isalpha()))
print('Contained alphabets and letter: ' + str(string.isalnum()))
print(string.strip())

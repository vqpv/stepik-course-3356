import re

s = input()

print(re.split('[^a-z]', s))

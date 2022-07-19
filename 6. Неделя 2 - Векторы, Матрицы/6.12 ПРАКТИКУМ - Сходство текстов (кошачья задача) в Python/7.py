import re

s = input().lower()

print(re.split('[^a-z]', s))

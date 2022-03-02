import re

f = open('akiyo.txt')

pattern = re.compile(r'(\d\.\d)\s+(\d.\d)\s+(\d.\d)\s+(\d|\s)\s+(\d.\d|\s)\s+(\d.\d|\s)\s+(.+)')

for line in f:


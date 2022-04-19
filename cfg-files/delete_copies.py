import os

files = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f.count('copy') > 0]

for f in files:
    os.remove(f)

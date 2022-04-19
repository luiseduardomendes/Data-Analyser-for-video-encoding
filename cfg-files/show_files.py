from os import listdir, path

files = [f for f in listdir('.') if path.isfile(path.join('.', f)) and f[-4:] == '.cfg']

print(files)

for f in files:
    data = open(f,'r' )
    file_content = data.read()
    print(f)
    print(file_content)
    print('*-'*30)

    

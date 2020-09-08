import os
file = 'unknownfiletype.065902'
# Rename a file extension
base = os.path.splitext(file)[0]
new_file = os.rename(file, base + '.txt')

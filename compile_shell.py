import sys
import os
import linecache

file_relative_dir=sys.argv[1]
linenumber=int(sys.argv[2])
setting=sys.argv[3]

while linenumber:
    text=linecache.getline(file_relative_dir,linenumber)
    if 'class' in text:
        escape_index=text.find(' ')
        brackets_index=text.find('(')
        class_name=text[escape_index:brackets_index]
        linecache.clearcache()
        break
    else:
        linenumber-=1

commands=[
    'D:\Anaconda3\python.exe',  # my anaconda dir -> to replace it with yours
    'manim.py',
    file_relative_dir,
    class_name,
    setting
]
os.system(' '.join(commands))






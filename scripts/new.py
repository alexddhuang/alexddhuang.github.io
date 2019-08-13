from sys import argv
from slugify import slugify
import os

title = "New Post"

if len(argv) >= 2:
    title = argv[1]

filename = '_drafts/' + slugify(title) + '.md'
if not os.path.isfile(filename):
    f = open(filename, 'w', encoding='UTF-8')
    f.write('---\ntitle: "' + title + '"\n' + '---\n\n')
    f.close()
    print('Created a new post: ' + filename)
import os
from slugify import slugify

def get_files():
    drafts = os.listdir("_drafts")
    drafts = ["_drafts/" + f for f in drafts]
    posts = os.listdir("_posts")
    posts = ["_posts/" + f for f in posts]
    files = drafts + posts
    files = [f for f in files if f[-3:] == ".md"]
    return files

def collect_tags():
    tags = set()
    files = get_files()
    for f in files:
        fp = open(f, "r", encoding="UTF-8")
        in_front = False
        for line in fp:
            line = line.strip()
            if line == "---":
                if in_front:
                    in_front = False
                else:
                    in_front = True
            elif in_front and line[0:5] == "tags:":
                tags_array = line[5:].strip().split()
                for tag in tags_array:
                    tags.add(tag)
            elif not in_front:
                break
        fp.close()
    return tags

def generate():
    if not os.path.exists("tag/"):
        os.mkdir("tag")

    tags = collect_tags()
    for tag in tags:
        filename = "tag/" + slugify(tag) + ".md"
        if not os.path.isfile(filename):
            print("generate " + filename)
            f = open(filename, 'w', encoding='UTF-8')
            f.write("---\n")
            f.write("layout: tag\n")
            f.write("title: \"Tag: " + tag + "\"\n")
            f.write("tag: " + tag + "\n")
            f.write("---\n")
            f.close() 
       
generate()

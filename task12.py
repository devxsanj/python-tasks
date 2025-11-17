import os

def copyoldcontacts():
    with open("oldcontacts.txt", "rt") as f:
        content = f.read()
    with open("contacts.txt", "a") as xyz:
        xyz.write(content)
        print("success")
        os.remove("oldcontacts.txt")

copyoldcontacts()
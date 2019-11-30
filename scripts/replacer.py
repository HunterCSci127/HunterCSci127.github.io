# Replaces each instance of a specified string in a file with a different specified string
# Created By: Owen Kunhardt

def replace(fileName, old, new):
    file = open(fileName,'r', encoding="utf8")
    filedata = file.read()
    file.close()

    filedata = filedata.replace(old, new)

    file = open(fileName,'w', encoding="utf8")
    file.write(filedata)
    file.close()

def main():
    fileName = input("Enter path of file to change: ")
    old = input("Enter string to be replaced: ")
    new = input("Enter string to be replaced with: ")
    replace(fileName, old, new)

if __name__ == "__main__":
    main()

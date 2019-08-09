import re
import sys

if __name__ == "__main__":
    content = sys.stdin.read()
    for link in re.findall(r"(?<=18reports/).*?(?=\.pdf)", content):
        print(link)

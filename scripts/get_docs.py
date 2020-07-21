import re
import sys

if __name__ == "__main__":
    content = sys.stdin.read()
    year_str = sys.argv[1][-2:]
    for link in re.findall(r"(?<=" + year_str + r"reports/).*?(?=\.pdf)", content):
        sys.stdout.write(f"{link}\n")

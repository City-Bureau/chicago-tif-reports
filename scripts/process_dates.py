import csv
import re
import sys

if __name__ == "__main__":
    tifs = []
    cols = ["name", "creation", "expiration"]
    for row in csv.reader(sys.stdin):
        if len(row) == 3 and all(
            re.search(r"\d{1,2}/\d{1,3}/\d{4}", c) for c in row[1:]
        ):
            tif_row = dict(zip(cols, [r.strip() for r in row]))
            tif_row["name"] = tif_row["name"].replace("X", "").strip()
            tifs.append(tif_row)

    writer = csv.DictWriter(sys.stdout, fieldnames=cols)
    writer.writeheader()
    writer.writerows(tifs)

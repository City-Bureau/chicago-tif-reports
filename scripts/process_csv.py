import csv
import re
import sys


def get_row_cost(row):
    end_str = "".join(row[-2:])
    cost_match = re.search(r"\$.*", end_str)
    if cost_match:
        return cost_match.group().strip()
    return ""


if __name__ == "__main__":
    rows = [r for r in csv.reader(sys.stdin)]
    csv_dict = {
        "name": "",
        "number": re.search(r"(?<=_)\d+(?=_)", sys.argv[1]).group(),
        "year": 2018,
        "extraction_annual": "",
        "extraction_cumulative": "",
        "transfers_in_annual": "",
        "transfers_in_cumulative": "",
        "expenses_annual": "",
        "balance": "",
        "transfers_out": "",
        "distribution": "",
        "city_admin_costs": "",
        "finance_costs": "",
        "bank": "",
        "url": "https://www.chicago.gov/content/dam/city/depts/dcd/tif/18reports/{}.pdf".format(  # noqa
            sys.argv[1]
        ),
    }
    dollar_cols = [
        "extraction_annual",
        "extraction_cumulative",
        "transfers_in_annual",
        "transfers_in_cumulative",
        "expenses_annual",
        "balance",
        "transfers_out",
        "distribution",
        "city_admin_costs",
        "finance_costs",
    ]
    for row in rows:
        if "TIF NAME" in row[0]:
            csv_dict["name"] = (
                re.search(r"(?<=NAME:).*(?=Redevelopment)", "".join(row))
                .group()
                .strip()
            )
        elif "Property Tax Increment" in row[0]:
            csv_dict["extraction_annual"] = row[1]
            csv_dict["extraction_cumulative"] = row[2]
        elif "Transfers from Municipal Sources" in row[0]:
            csv_dict["transfers_in_annual"] = row[1]
            csv_dict["transfers_in_cumulative"] = row[2]
        elif "Total Expenditures/Cash Disbursements" in row[0]:
            csv_dict["expenses_annual"] = row[1]
        elif "Distribution of Surplus" in row[0]:
            # TODO: Asterisks are commonly added here, keep in some way?
            csv_dict["transfers_out"] = row[1]
        elif "Transfers to Municipal" in row[0]:
            csv_dict["distribution"] = row[1]
        elif "FUND BALANCE, END OF REPORTING" in row[0]:
            csv_dict["balance"] = row[1]
        elif "City Staff Costs" in row[0]:
            csv_dict["city_admin_costs"] = get_row_cost(row)
        elif "Financing" in row[1]:
            csv_dict["bank"] = row[0]
            csv_dict["finance_costs"] = get_row_cost(row)

    for col in dollar_cols:
        dollar_val = re.sub(r"[\$\*, ]", "", csv_dict[col])
        if "(" in dollar_val:
            dollar_val = "-" + re.sub(r"[\(\)]", "", dollar_val)
        csv_dict[col] = dollar_val

    writer = csv.DictWriter(sys.stdout, fieldnames=list(csv_dict.keys()))
    writer.writeheader()
    writer.writerow(csv_dict)

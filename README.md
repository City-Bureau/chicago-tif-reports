# Chicago TIF Reports

Data from the Chicago TIF financial audits for the following years:

- [2018](https://www.chicago.gov/city/en/depts/dcd/supp_info/district-annual-reports--2018-.html)
- [2019](https://www.chicago.gov/city/en/depts/dcd/supp_info/district-annual-reports--2019-.html)

To download the data as a CSV file, right click one of these links and choose "Save Link As...":

- [2018 TIF report](https://raw.githubusercontent.com/City-Bureau/chicago-tif-reports/main/output/2018/data.csv)
- [2019 TIF report](https://raw.githubusercontent.com/City-Bureau/chicago-tif-reports/main/output/2019/data.csv)
- [Combined report (all years)](https://raw.githubusercontent.com/City-Bureau/chicago-tif-reports/main/output/data.csv)

## Notes

The 2019 data is incomplete because the following links are currently broken on the city's site:

- https://www.chicago.gov/content/dam/city/depts/dcd/tif/19reports/T_002_41stKingAR19.pdf
- https://www.chicago.gov/content/dam/city/depts/dcd/tif/19reports/T_059_CalumetCermakAR19.pdf
- https://www.chicago.gov/content/dam/city/depts/dcd/tif/19reports/T_122_DrexelAR19.pdf
- https://www.chicago.gov/content/dam/city/depts/dcd/tif/19reports/T_103_LakeCalumetAR19.pdf
- https://www.chicago.gov/content/dam/city/depts/dcd/tif/19reports/T_028_LincolnBelmontAshlandAR19.pdf
- https://www.chicago.gov/content/dam/city/depts/dcd/tif/19reports/T_139_RavenswoodAR19.pdf
- https://www.chicago.gov/content/dam/city/depts/dcd/tif/19reports/T_036_ReadDunningAR19.pdf
- https://www.chicago.gov/content/dam/city/depts/dcd/tif/19reports/T_158_WeedFremontAR19.pdf

## Setup

You'll need [`wget`](https://www.gnu.org/software/wget/wget.html), Python, and [`csvkit`](https://csvkit.readthedocs.io/en/latest/) installed:

```bash
make all
```

from io import BytesIO

import openpyxl

from hl7 import hl7_to_csv, hl7_to_excel


def test_hl7_to_csv():
    with open("tests/data/hl7-1.txt") as f:
        csv_content = hl7_to_csv(hl7_content=f.read())
        assert "MSH;1.1;|" in csv_content
        assert "MSH;2.1;^~\\&" in csv_content
        assert "PID;5.2;Name1" in csv_content
        assert "PID;1.1;Lorem Ipsum" in csv_content


def test_hl7_to_excel():
    with open("tests/data/hl7-1.txt") as f:
        hl7_content = f.read()
        excel_content = hl7_to_excel(hl7_content=hl7_content)

    workbook = openpyxl.load_workbook(BytesIO(excel_content))
    worksheet = workbook.active
    print(hl7_content)
    for row in worksheet.iter_rows(values_only=True):
        print(row)

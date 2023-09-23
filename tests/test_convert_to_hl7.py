from hl7 import csv_to_hl7, excel_to_hl7


def test_convert_to_hl7():
    with open("tests/data/data1.csv") as f:
        hl7_content = csv_to_hl7(csv_content=f.read())
        assert hl7_content.startswith("MSH")
        assert (
            "PID|Lorem Ipsum|Test|HSPTL|^^&12345|John&&Doe^Name1^^^^^L" in hl7_content
        )


def test_excel_to_hl7():
    hl7_content = excel_to_hl7(file_path="tests/data/data1.xlsx")
    assert "MSH|^~\\&" in hl7_content, "MSH segment is missing"
    assert (
        "PID|^~\\&|sdsdee|App|efeffefe|123456789|gtfgfgdfdgf|||43434|||||||||dfdfef4444"
        in hl7_content
    ), "PID segment is missing"

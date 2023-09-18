from hl7 import csv_to_hl7, hl7_to_csv


def test_convert_to_hl7():
    with open("tests/data/data1.csv") as f:
        hl7_content = csv_to_hl7(csv_content=f.read())
        print(hl7_content)
        assert hl7_content.startswith("MSH")
        assert (
            "PID|Lorem Ipsum|Test|HSPTL|^^&12345|John&&Doe^Name1^^^^^L" in hl7_content
        )


def test_hl7_to_csv():
    with open("tests/data/hl7-1.txt") as f:
        csv_content = hl7_to_csv(hl7_content=f.read())
        assert "MSH;1.1;|" in csv_content
        assert "MSH;2.1;^~\&" in csv_content
        assert "PID;5.2;Name1" in csv_content
        assert "PID;1.1;Lorem Ipsum" in csv_content

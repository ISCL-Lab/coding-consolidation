import csv as csv
import openpyxl as opxl

def splitExcel(input_path, output_path):
    # output_folders = []

    for file_path in input_path.glob("*.xlsx"):

        if file_path.name.startswith("~$"): # skip temp excel lock files
            continue

        sub_folder = output_path / file_path.stem
        sub_folder.mkdir(parents=True, exist_ok=True)

        sheets = opxl.load_workbook(file_path, data_only=True)
        for sheet_name in sheets.sheetnames:
            sheet = sheets[sheet_name]
            new_path = sub_folder / f"{sheet_name}.csv"

            with open(new_path, "w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                for row in sheet.iter_rows(values_only=True):
                    writer.writerow(row)

    #     output_folders.append(sub_folder)

    # return output_folders

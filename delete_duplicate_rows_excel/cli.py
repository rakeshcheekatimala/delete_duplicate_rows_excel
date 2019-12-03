import argparse
import readjson
import pandas as pd
from pandas import DataFrame


def main():
    # create argument parser object
    parser = argparse.ArgumentParser(
        description="Delete Duplicate Rows from Excel file")

    parser.add_argument("-json", "--json", type=str, nargs=1,
                        metavar="inputfile", default=None, help="Input Json file")

    # parse the arguments from standard input
    args = parser.parse_args()
    delete_duplicate_rows_from_excel(args.json[0])


def delete_duplicate_rows_from_excel(jsonfile):
    contents = readjson.load_json_data(jsonfile)
    if contents:
        data = pd.read_excel(contents["inputFileName"])
        initialRows = data.__len__()
        initialRows = '\n --- Total Rows {initialRows} before deletion  --- \n'.format(
            initialRows=initialRows)
        print(initialRows)
        df = pd.DataFrame(data)
        duplicateColumns = contents["duplicateColumnNames"].split(",")
        df_duplicates_removed = df.drop_duplicates(
            subset=duplicateColumns, keep=contents["keep"])
        print("\n --- Deleted the Duplicated Rows Based on columnNames in data.json --- \n")
        totalRows = df_duplicates_removed.__len__()
        totalRows = '\n --- Total Rows {totalRows} after deletion  ---- \n'.format(
            totalRows=totalRows)
        print(totalRows)
        print("\n --- File Copying Inprogress ... ---- \n")
        df_duplicates_removed.to_excel(
            contents["outputFileName"], index=bool(contents["index"]))
        print("\n --- File Copied to excel after duplicate rows are deleted ---- \n")
    else:
        print("\n Provide a valid json file ex: data.json from the current directy of json file \n")


if __name__ == "__main__":
    main()

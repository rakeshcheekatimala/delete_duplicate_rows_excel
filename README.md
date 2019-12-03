# Delete Duplicte Rows From Excel

A Python package to delete duplicate based on your columns grouping given in data.json

## Usage

Following query on terminal will provide you the weather details of "delhi" for next 3 days.

```
delete-duplicate-rows-excel -json data.json
```

### Steps to Run the program 
  * Create a data.json as shown below
  ```json
{
	"inputFileName": "/Users/rakeshcheekatimala/Desktop/Learning/ScrapDataExcel/input.xlsx",
	"outputFileName": "/Users/rakeshcheekatimala/Desktop/Learning/ScrapDataExcel/output.xlsx",
	"format": "xslx",
	"duplicateColumnNames": "Company,Postalcode,Mall Name"
}
```

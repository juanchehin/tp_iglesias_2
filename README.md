# TP iglesias

## -----------------------------------------
## Exercises - pandas

1. Use pandas read_excel() to read the EcarSalesByCountryAndYear2.xlsx into a DataFrame, then display the DataFrame
2. Refine the call to read_excel() to read the worksheet tab 'EcarSalesByCountryAndYear into a DataFrame (use the sheet_name parameter)
3. Refine the call used in step #2 to set the index to Country (use the sheet_name and index_col parameters)

## Exercises - openpyxl

4. Use the openpyxl load_workbook() function to load the workbook, assigning the result to a variable called workbook
5. Access the 'Documentation' worksheet tab using workbook[ ]
6. Access and display the value of cell B2 (the data source for the workbook)


## -----------------------------------------
## Transaction for years

### Data load and review

1. Read data from sales.csv into a DataFrame
2. Review the data using head()

### One-dimensional pivot table

3. Summarize sales by product using a pivot table  values='count'  index='product'  aggfunc='sum'

### Two-dimensional pivot table

4. Summarize sales by product and region using a pivot table  values='count'  index='product'  columns='region'  aggfunc='sum'
5. Refine the pivot table to show column and row totals, by adding margins=True

### Pivot chart

6. From the two-dimensional pivot table (excluding the row and column totals), create a stacked horizontal bar chart, using the DataFrame plot() method and these settings:  kind='barh'  stacked=True


## -----------------------------------------
## 

## 

1. 
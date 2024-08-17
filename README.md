# TP iglesias

## -----------------------------------------
## Sales country years

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
## Car adoption

1. Read the file EcarSalesByCountryAndYear.csv into a DataFrame; display the DataFrame
2. Re-read the .csv file into a DataFrame, using the Country as the DataFrame's index; display the DataFrame
3. Calculate the sales growth between the last two years and append this to the DataFrame as a column called 'Growth'
4. If your growth value is in decimal, rescale the growth column to a percentage
5. Round the growth column to 1 decimal place

6. Display the DataFrame sorted by Growth, from high to low
7. Create a new DataFrame called dfRecent, with only columns Sales2021 and Sales2020
8. From dfRecent, use a filter to display only United States and Canada
9. Use dfRecent to display the total sales across countries for 2020 and 2021
10. Calculate and display sales by Continent by Year
11. What was the 2022 vs. 2021 growth in electric car sales, by continent?



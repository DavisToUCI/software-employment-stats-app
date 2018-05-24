import openpyxl
import Info_Sorter

'''This is the list of columns that we'll be using for our spreadsheet
which store info for Annual Mean Wage, Annual Median Wage, Hourly Mean Wage,
and Hourly Median Wage.'''
COLUMN_LIST = ["A", "B", "E", "N", "D", "I"]

'''This stores the rows that we'll be grabbing our information from'''
MIN_NUM = 9
MAX_NUM = 379

#Opens the file and returns a workbook item
def open_file(fileName:str) -> "workbook":
    return openpyxl.load_workbook(fileName)

#Takes in a workbook and returns a worksheet item
def open_sheet(workBook: 'workbook', sheetName: str) -> "sheet":
    return workBook[sheetName]

#Organizes the sheet into a dictionary so we can easily grab information
def organize_sheet(sheet: 'worksheet', column_list: list, min_num: int, max_num: int) -> dict:
    main_dict = dict(dict())
    for number in range(min_num, max_num):
        occupation_index = sheet[column_list[0] + str(number)].value
        main_dict[occupation_index] = dict()
        for column in column_list[1:]: 
            wage_index = sheet[column + '6'].value # C6
            value_str = sheet[column + str(number)].value.strip()
            try:
                value = float(value_str)
                main_dict[occupation_index][wage_index] = float(value_str)
            except:
                del main_dict[occupation_index]
                break
    return main_dict        
            
        

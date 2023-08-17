from enum import Enum, unique

CSV_EXTENSION = '.csv'
JSON_EXTENSION = '.json'
XLS_EXTENSION = '.xls'
XLSX_EXTENSION = '.xlsx'

@unique
class CSVColumnsName(Enum):
    NAME = 'NAME'
    DESCRIPTION = 'DESCRIPTION'
    TYPE = 'TYPE'
    NUMBER='NUMBER'
    APP= 'APP'
    ICON = 'ICON'
    POSITION = 'POSITION'
    URL='URL'
    PARENT='PARENT'

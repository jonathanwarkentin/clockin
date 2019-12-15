from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font
from os import getenv, path


def start_work():
    # set file name from environment variable
    file_name = getenv('TIMESHEET')
    if file_name == "":
        file_name = None
    elif file_name.split('.')[1] != 'xlsx':
        file_name = file_name.split('.')[0] + '.xlsx'

    # start work timing
    print('Starting work...')
    start_time = datetime.now()
    input('Press enter to end work... ')

    # end work timing and calculate hours
    end_time = datetime.now()
    work_duration = end_time - start_time
    hours = round(work_duration.seconds/3600, 2)
    print('Hours: ' + str(hours))
    # get task info
    task = input('Enter task info... ')
    print("Task: " + task)

    # check if inputted file exists
    # if yes, write to that file - assume correct format
    if path.exists(file_name):
        print("Saved work session to existing file: " + file_name)
    # if no, write to new file with default name
    else:
        workbook = Workbook()
        sheet = workbook.active
        bold_font = Font(bold=True)
        sheet["A1"] = "Date"
        sheet["B1"] = "Hours"
        sheet["C1"] = "Task"
        sheet["A1"].font = bold_font
        sheet["B1"].font = bold_font
        sheet["C1"].font = bold_font
        sheet["A2"] = datetime.now().strftime("%x")
        sheet["B2"] = str(hours)
        sheet["C2"] = task
        file_name = "timesheet.xlsx"
        workbook.save(filename=file_name)
        print("Saved work session to new file: " + file_name)


if __name__ == "__main__":
    start_work()

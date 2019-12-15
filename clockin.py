from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font


def start_work():
    print('Starting work...')
    start_time = datetime.now()
    input('Press enter to end work... ')

    end_time = datetime.now()
    work_duration = end_time - start_time
    hours = round(work_duration.seconds/3600, 2)
    print('Hours: ' + str(hours))
    task = input('Enter task info... ')
    print("Task: " + task)

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
    file_name = "test.xlsx"
    workbook.save(filename=file_name)
    print("Saved work session to file: " + file_name)


if __name__ == "__main__":
    start_work()

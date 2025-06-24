from openpyxl import Workbook
from text_parser import extract_data


def create_excel(file_paths):
    wb = Workbook()
    ws = wb.active
    ws.title = "Ride data" # type: ignore
    ws.append(['Pickup Location', 'Dropoff Location', 'Date', 'Fare']) # type: ignore
    for imgPath in file_paths:
        data_list= extract_data(imgPath)
        data_list[3] = "{:.2f}".format(float(data_list[3]))
        ws.append(data_list) # type: ignore

    

    wb.save('ride_data.xlsx')


import time
import requests
import csv
import datetime

LOGIN = '9cocbg'
PASSWORD = 'QJN879'

proxies = {
    'https': f'http://{LOGIN}:{PASSWORD}@195.216.132.9:8000'
}


def checking_updates():

    check_reviews_url = 'https://card.wb.ru/cards/detail?nm=70117598'
    check_orders_url = 'https://product-order-qnt.wildberries.ru/by-nm/?nm=70117598'

    reviews_response = requests.get(check_reviews_url, proxies=proxies).json()
    reviews_amount = reviews_response['data']['products'][0]['feedbacks']

    orders_response = requests.get(check_orders_url).json()
    orders_amount = orders_response[0]['qnt']

    return [reviews_amount, orders_amount]


# def write_updates_to_excel():
#     workbook = xlsxwriter.Workbook('/Users/nikolai/Desktop/checking_updates.xlsx')
#     worksheet = workbook.add_worksheet()
#     worksheet.write(1, 1, 'Hello')
#     worksheet.write(1, 2, 'It is me')
#     worksheet.write(1, 3, 'Today')


def write_updates_to_csv():
    # data = [
    #     ['Покупки', 'Отзывы', 'Время сканирования'],
    #     # [123, 11, 'today'],
    #     # [1232, 111, 'today'],
    #     # [1223, 131, 'today'],
    # ]
    date = datetime.datetime.today()
    data = checking_updates()
    data.append(date.strftime("%Y-%m-%d %H:%M:%S"))
    file_to_write = open('checking_updates.csv', 'a')
    with file_to_write:
        writer = csv.writer(file_to_write)
        writer.writerow(data)


if __name__ == '__main__':
    # checking_updates()
    counter = 0
    while True and counter < 3:
        write_updates_to_csv()
        time.sleep(3)
        counter += 1

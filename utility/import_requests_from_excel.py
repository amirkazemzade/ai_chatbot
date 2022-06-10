import openpyxl
from pathlib import Path
from datasource import Repository


def read_excel(repository: Repository):
    excel = Path('ai_sentences.xlsx')
    work_book = openpyxl.load_workbook(excel)

    sheet = work_book.active
    for i in range(2, sheet.max_row + 1):
        req = sheet[f'B{i}'].value
        repository.insert_request(req)


if __name__ == '__main__':
    read_excel(Repository())

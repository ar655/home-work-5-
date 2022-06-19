
import re


class ValidCarNumber:
    def __init__(self, number):
        self.number = number

    def is_valid(self,):
        self.number = input('Valid number')


valid_number = ValidCarNumber(number='01KG777BAD')

numbers = re.search(r"[0-9A-Z]([0-9]{3})([A-Z]{3})",valid_number.number )

valid_number.is_valid()

try:
    if numbers.end() == len(valid_number.number):
        print(f' Номер валидный!')
    else:
        raise  ValueError
except:
    print(f'Номер не валидный!')



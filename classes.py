class Employee:
    counter = 1

    def __init__(worker, name, address, type, cash_per_hour, cash_per_month, comission, sindicate = False):
        worker.name             = name
        worker.address          = address
        worker.type             = type
        worker.cash_per_hour    = cash_per_hour
        worker.cash_per_month   = cash_per_month
        worker.comission        = comission
        worker.number           = Employee.counter
        worker.sindicate        = sindicate
        Employee.counter        += 1
        worker.selling_amount   = 0
        worker.extra_hours      = 0
        worker.sindicate_tax    = 0

    def time_card_func(worker, total):
        if (worker.type == 'hourly'):
            if (total > 8):
                worker.extra_hours += TimeCard.time_func(worker, total)
                print(f'{worker.name} bateu o ponto e fez um total de {total-8} horas extras.')

            else:
                print(f'{worker.name} bateu o ponto e não fez horas extras.')

        else:
            print(f'{worker.name} bateu o ponto.\n')

    def sells_func(worker, date, value):
        if (worker.type == 'salaried'):
            worker.selling_amount += Sells.value_func(worker, value)
            print(f'{worker.name} realizou uma venda no dia {date} com o valor de {value}.')

        else:
            print(f'{worker.name} não é um assalariado.')

    def service_tax_func(worker, tax):
        if (worker.sindicate):
            worker.sindicate_tax += Sindicate.taxes_func(worker, tax)
            print(f'Uma taxa de {tax} reais será descontada do salário de empregado {worker.name}.')

        else:
            print(f'O empregado {worker.name} não pertence ao sindicato.')

class Sindicate(Employee):
    def taxes_func(worker, tax):
        worker.tax = tax
        return worker.tax

class Sells(Employee):
    def value_func(worker, value):
        worker.value = value
        return worker.value

class TimeCard(Employee):
    def time_func(worker, time):
        worker.time = time
        return (worker.time - 8)
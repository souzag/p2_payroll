from classes import Employee

#Função 1: Adição de um empregado
employee_1 = Employee('Fallen', 'Leader', 'salaried', 50, 8000, 50, True)
employee_2 = Employee('Fer', 'Lurker', 'salaried', 50, 8000, 50)
employee_3 = Employee('Coldzera', 'Awper', 'hourly', 50, 8000, 50)
employee_4 = Employee('Taco', 'Fragger', 'salaried', 50, 8000, 50, True)
employee_5 = Employee('FNX', 'Support', 'salaried', 50, 8000, 50)

#Função 2: Remoção de um empregado
del(employee_5)

#Função 3: Lançar um Cartão de Ponto
employee_4.time_card_func(8)
employee_3.time_card_func(10)
employee_3.time_card_func(11)
employee_3.time_card_func(12)
print(f'O valor total de horas extras do funcionário {employee_3.name} é {employee_3.extra_hours}.\n')

#Função 4: Lançar um Resultado Venda
employee_2.sells_func('05/07/2021', 100)
employee_2.sells_func('06/07/2021', 101)
employee_2.sells_func('07/07/2021', 102)
print(f'O valor total de vendas do funcionário {employee_2.name} é {employee_2.selling_amount}.\n')

#Função 5: Lançar uma taxa de serviço
employee_1.service_tax_func(100)
employee_1.service_tax_func(101)
employee_1.service_tax_func(102)
print(f'O valor total de taxas do funcionário {employee_1.name} é {employee_1.sindicate_tax}.\n')

#Função 6: Alterar detalhes de um empregado
employee_4.type = 'hourly'
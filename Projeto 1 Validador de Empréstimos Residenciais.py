msg_error = 'Digite uma opção valida ...'

while True:
    while True:
        valor_casa = str(input('Valor da casa: ')).strip()
        try:
            valor_casa = float(valor_casa)
            break
        except ValueError:
            print(msg_error)
    while True:
        salario = str(input('Salario do comprador: ')).strip()
        try:
            salario = float(salario)
            break
        except ValueError:
            print(msg_error)
    while True:
        prazo = str(input('Prazo para financiamento: ')).strip()
        try:
            prazo = int(prazo)
            break
        except ValueError:
            print(msg_error)
    salario_30 = salario / 100 * 30
    prestacao = valor_casa 
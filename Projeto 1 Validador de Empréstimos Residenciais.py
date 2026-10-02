msg_error = 'Digite uma opção valida ...'
total_aprovado = total_negativado = 0
while True:
    while True:
        valor_casa = str(input('Valor da casa: R$')).strip()
        try:
            valor_casa = float(valor_casa)
            break
        except ValueError:
            print(msg_error)

    while True:
        salario = str(input('Salario do comprador: R$')).strip()
        try:
            salario = float(salario)
            break
        except ValueError:
            print(msg_error)

    while True:
        prazo = str(input('Prazo para financiamento (anos): ')).strip()
        try:
            prazo = int(prazo)
            if prazo < 30:
                break
            else:
                print(msg_error)
                continue
        except ValueError:
            print(msg_error)

    salario_30 = salario / 100 * 30
    prestacao = valor_casa / (prazo * 12)

    print('')
    if prestacao < salario_30:
        print(f'''Financiamento \033[1;32mAPROVADO\033[m!
30% do seu salario equivale: {salario_30}
Prestação do financiamento: {prestacao}''')
        total_aprovado += 1
    else:
        print(f'''Financiamento \033[1;31mREPROVADO\033[m!
30% do seu salario equivale: {salario_30:.2f}
Prestação do financiamento: {prestacao:.2f}''')
        total_negativado += 1
    continua = ''
    while continua not in 'SsNn':
        continua = str(input('Quer continuar? [S/N]: ')).strip()[0]
        if continua not in 'SsNn':
            print(msg_error)
    if continua in 'Nn':
        break

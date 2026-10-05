msg_error = 'Digite uma opção valida ...'
while True:
    print(f'''[1] Registrar atendimento
[2] Relatório do dia
[3] Sair''')
    escolha_acao = str(input('Sua escolha -> ')).strip()
    try:
        escolha_acao = int(escolha_acao)
        if escolha_acao < 1 or escolha_acao > 3:
            print(msg_error)
            continue

    except ValueError:
        continue
    if escolha_acao == 1:
        while True:
            idade_cliente = str(input('Idade do cliente: '))
            try:
                idade_cliente = int(idade_cliente)
                break
            except ValueError:
                continue
        while True:
            print('''[1] Reparo
[2] Acessórios
[3] Limpeza''')
            escolha_servico = str(input('Sua escolha -> ')).strip()
            if escolha_servico in '123':
                if escolha_servico in '1':
                    while True:
                        try:
                            valor_servico = float(input('Valor do servico'))
                            break


            else:
                continue
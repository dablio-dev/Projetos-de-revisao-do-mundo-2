msg_error = 'Digite uma opção valida ...'
max_reparo = max_acessorio = max_limpeza = faturamento = contador_idade = menor_idade =0
mais_procurado = 'Nenhum serviço foi registrado'

print('-' * 50)
print(' ATENDIMENTO AUTOMATIZADO '.center(50, ' '))
while True:
    print('-' * 50)
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
        print(msg_error)
        continue
    if escolha_acao == 1:
        while True:
            idade_cliente = str(input('Idade do cliente: '))
            try:
                idade_cliente = int(idade_cliente)
                if idade_cliente < 1 or idade_cliente > 130:
                    print(msg_error)
                else:
                    contador_idade += 1
                    if contador_idade == 1 or idade_cliente < menor_idade:
                        menor_idade = idade_cliente
                    break
            except ValueError:
                print(msg_error)
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
                            valor_servico = float(input('Valor do serviço: R$ '))
                            max_reparo += 1
                            faturamento += valor_servico
                            break
                        except ValueError:
                            print(msg_error)
                            continue
                elif escolha_servico in '2':
                    while True:
                        try:
                            valor_acessorio = float(input('Valor do acessório: R$ '))
                            max_acessorio += 1
                            faturamento += valor_acessorio
                            break
                        except ValueError:
                            print(msg_error)
                            continue
                else:
                    while True:
                        try:
                            valor_limpeza = float(input('Valor da limpeza: R$ '))
                            max_limpeza += 1
                            faturamento += valor_limpeza
                            break
                        except ValueError:
                            print(msg_error)
                            continue
            else:
                print(msg_error)
                continue
            break
        if max_reparo > max_limpeza and max_reparo > max_acessorio:
            mais_procurado = 'Reparo'
        elif max_limpeza > max_reparo and max_limpeza > max_acessorio:
            mais_procurado = 'Limpeza'
        elif max_acessorio > max_reparo and max_acessorio > max_limpeza:
            mais_procurado = 'Acessório'
        else:
            if max_reparo == max_limpeza == max_acessorio:
                mais_procurado = 'Demanda iguais para todos os serviços'
            elif max_acessorio == max_reparo:
                mais_procurado = 'Acessórios e reparos'
            elif max_acessorio == max_limpeza:
                mais_procurado = 'Acessórios e limpeza'
            else:
                mais_procurado = 'Reparos e limpeza'
    elif escolha_acao == 2:
        if max_acessorio <= 0 and max_limpeza <= 0 and max_reparo <= 0:
            print('Nenhuma ordem de serviço registrada, por favor digite ( 1 ) e registre uma agora ...')
        else:
            print('-' * 50)
            print(' RELATÓRIO DO DIA '.center(50, ' '))
            print('-' * 50)
            print(f'''Faturamento total: R${faturamento:.2f}
Serviço mais buscado: {mais_procurado}
Menor idade cadastrada: {menor_idade} anos''')
    else:
        break
print('Fim do programa, volte sempre')



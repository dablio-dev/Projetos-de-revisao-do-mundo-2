total_vendas_desc = faturamento_liquido = total_vendas_juros = total_preco_normal = total_vendas = meta_faturamento = 0
valor_venda = forma_pagamento= 0

while True:
    try:
        meta_faturamento = float(input('Meta de faturamento: R$ '))
        break
    except ValueError:
        print('Digite um valor valido...')
        continue

ja_exibida = False
while True:
    print('-' * 50)
    while True:
        try:
            valor_venda = float(input('Valor da venda: R$ '))
            break
        except ValueError:
            print('Digite um valor valido...')
            continue
    if valor_venda == 0:
        break

    while True:
        try:
            print(' FORMA DE PAGAMENTO '.center(50, '-'))
            forma_pagamento = int(input('[1] Dinheiro / Pix (-10%) | [2] Debito (Preço normal)'
                                        '\n[3] Credito até 2x (Preço normal) | [4] Credito  3x ou mais (+20 juros)'
                                        '\nSua escolha: '))
            total_vendas += 1
            break
        except ValueError:
            continue

    if forma_pagamento == 1:
        dinheiro_pix = valor_venda - (valor_venda / 100 * 10)
        total_vendas_desc += 1
        faturamento_liquido += dinheiro_pix
    elif forma_pagamento == 4:
        credito_3x = valor_venda + (valor_venda / 100 * 20)
        total_vendas_juros += 1
        faturamento_liquido += valor_venda
    else:
        total_preco_normal += 1
        sem_acrescimo = valor_venda
        faturamento_liquido += valor_venda
    if faturamento_liquido >= meta_faturamento and ja_exibida == False:
        print('-' * 50)
        ja_exibida = True
        print(f'\033[1;32mMETA DE R${meta_faturamento:.2f} ATINGIDA\033[m')

porcentagem_meta = faturamento_liquido / meta_faturamento * 100

print('-' * 50)
print('FECHAMENTO DE CAIXA'.center(50, ' '))
print('-' * 50)

print(f'''Total de vendas: {total_vendas}
Faturamento liquido: R$ {faturamento_liquido:.2f}
Porcentagem da meta atingida: {porcentagem_meta:.1f}%
Vendas com desconto: {total_vendas_desc} | Vendas com juros: {total_vendas_juros}''')

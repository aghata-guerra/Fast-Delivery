#Fast Delivery

sistema = True

while sistema == True:
    print('==============================')
    print('1 - Cadastrar Nova Entrega')
    print('2 - Calcular Valor do Frete')
    print('3 - Listar Entregas')
    print('4 - Alterar Status')
    print('5 - Sair')
    print('==============================')
    escolhaMenu = int(input('Digite sua escolha: '))
   
    if escolhaMenu == 1:
        idPedido = int(input('Digite o ID: '))
        nomeCliente = input('Digite o seu Nome: ')
        status = 'Pendente'
        pedido = [idPedido, nomeCliente, status]
        
    elif escolhaMenu == 2:
        pesoPacote = float(input("Digite o peso do pacote: (KG)"))
        distancia = float(input("Digite a distancia: (KM)"))

        def calcularFrete():
            taxaBase = 10
            taxaKm = 1.50 * distancia
            taxaPeso = 0 
            if pesoPacote > 5:
                taxaPeso = 15
                
            return (taxaPeso + taxaBase + taxaKm)
    
        print(f"A sua taxa de entrega é: {calcularFrete()}")
        
    elif escolhaMenu == 3:
        print('====== Suas Entregas ======')
        print(f'ID: {idPedido}\nNome: {nomeCliente}\nDistância: {distancia}\nValor do Frete: {calcularFrete()}\nStatus: {status}')
    elif escolhaMenu == 4:
        print('====== Status do seu Pedido ======')
        buscadorId = input('Digite o seu ID: ')
        print('----------------------------------')
        print('Digite 1 para pedido entregue')
        print('Digite 2 para pedido a caminho')
        statusPedido = int(input('Escolha o status do Pedido: '))
        if statusPedido == 1:
            status = 'Entregue'
            print(status)
        elif statusPedido == 2:
            status = 'Pendente'
            print(status)
    elif escolhaMenu == 5:
        sistema = False
        print('Saindo do Menu')
    else:
        print('Escolha apenas entre 1 - 5')

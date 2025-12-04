**🚚 Fast Delivery**

Um sistema simples em Python para gerenciamento de entregas, permitindo cadastrar pedidos, calcular o valor do frete, listar informações e atualizar o status da entrega.
O programa funciona em modo de menu interativo via terminal.

**📌 Funcionalidades**

**Cadastrar Nova Entrega**
Permite registrar um pedido com ID, nome do cliente e status inicial Pendente.

<img width="857" height="406" alt="Captura de tela Fast Delivery" src="https://github.com/user-attachments/assets/e2248249-2c2a-4d24-a676-563c68b6730c" />


**Calcular Valor do Frete**
O frete é calculado com base em:

Taxa base: R$ 10,00
Distância (km): R$ 1,50 por km
Peso acima de 5 kg: taxa adicional de R$ 15,00

**Listar Entregas**
Exibe informações como:

ID do pedido, Nome do cliente, Distância, Valor do frete e Status.

**Alterar Status da Entrega**
Possibilidade de definir como:

Entregue ou Pendente.

**▶️ Como Executar**

1 - Certifique-se de ter o Python 3 instalado.

2 - Salve o arquivo do código como:
fast_delivery.py

3 - Execute no terminal:
python fast_delivery.py

**📁 Estrutura Geral do Código**

O sistema utiliza um loop while para exibir o menu principal e executar ações conforme a escolha do usuário.
Também possui uma função interna (calcularFrete) responsável pelo cálculo do valor total da entrega.

print("Obrigada!")

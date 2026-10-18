🧮sistema de Desconto Pogressivo:

Esse projeto apresenta um teste em um sistema de desconto, utilizando "If, "Else" e mais. Ajuda a entender o desconto de acordo com o total do valor inserido.

⌨️Utilizados:

* Python
* GitHub

▶️Executar: 
1. Tenha o Python instalado;
2. Abra a pasta do projeto no VS Code;
3. Abra o arquivo app.py.;
4. Execute utilizando:
   
📍valor_compra = float(input("Digite o valor total da compra: R$ "))

5. Para os "se..."
   
📍if valor_compra < 200:
    percentual_desconto = 0.05
📍elif valor_compra < 300:
    percentual_desconto = 0.10
📍else:
    percentual_desconto = 0.15

📍valor_desconto = valor_compra * percentual_desconto

📍valor_final = valor_compra - valor_desconto

6. Resultados na tela:

📍print("\n--- Resumo da compra ---")
📍print(f"Valor da compra: R$ {valor_compra:.2f}")
📍print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
📍print(f"Valor total a pagar: R$ {valor_final:.2f}")
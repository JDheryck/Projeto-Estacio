# Funções básicas (soma, subtração, multiplicação, divisão)label_titulo_basica = tk.Label(ababasica, text="Funções Básicas")label_titulo_basica.pack()label_a_soma = tk.Label(aba_basica, text="Valor de a:")label_a_soma.pack()entrada_a_soma = tk.Entry(aba_basica)entrada_a_soma.pack()label_b_soma = tk.Label(aba_basica, text="Valor de b:")label_b_soma.pack()entrada_b_soma = tk.Entry(aba_basica)entrada_b_soma.pack()botao_somar = tk.Button(aba_basica, text="Somar", command=lambda: soma_interface(entrada_a_soma, entrada_b_soma))botao_somar.pack()label_resultado_soma = tk.Label(aba_basica, text="Resultado:")label_resultado_soma.pack()

# ... (interfaces para as outras funções básicas: subtração, multiplicação, divisão)
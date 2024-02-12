palavra_secreta = 'GITHUB'
letras_certas = ''

tentativas = 0


while True:
    
    letra_digitada = input('Digite uma letra --> ')
    letra_digitada = letra_digitada.upper()  
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
      
        
    if letra_digitada in palavra_secreta:
        letras_certas += letra_digitada
    
    # Se não criarmos uma variável 'palavra_formada' aqui, ele vai ficar 
    # ordenando na vertical as letras
    palavra_formada = ''
    for letra_s in palavra_secreta:
        if letra_s in letras_certas:
            palavra_formada += letra_s
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print(f'PARABÉNS. Formou a palavra --> {palavra_secreta}')
        print(f'Você precisou de {tentativas} tentativas!')
        break


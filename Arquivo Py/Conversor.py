while True:
    print('O que você quer converter?')
    print('1) Medidas de Comprimento')
    print('2) Medidas de Peso')
    print('3) Conversão de Moedas')
    print('4) Medidas de Capacidades')
    print('5) Medidas De Tempo')
    escolha3 = int(input('Digite o número correspondente a sua opcão: '))
    if escolha3 == 1:
        print('1) Km para m')
        print('2) Km para cm')
        print('3) M para km')
        print('4) M para cm')
        print('5) Cm para m')
        print('6) Cm para km') 

    if escolha3 == 2:
        print('1) Kg para g')
        print('2) Kg para mg')
        print('3) G para kg')
        print('4) G para mg')
        print('5) Mg para kg')
        print('6) Mg para g')

    if escolha3 == 3:
        print('1) Real para dólar americano')
        print('2) Real para euro')
        print('3) Real para libra')
        print('4) Dólar americano para real')
        print('5) Dólar americano para euro')
        print('6) Dólar americano para libra')
        print('7) Euro para real')
        print('8) Euro para dólar americano')
        print('9) Euro para libra')
        print('10) Libra para real')
        print('11) Libra para dólar americano')
        print('12) Libra para euro')

    if escolha3 == 4:
        print('1) Quilolitro para litro')
        print('2) Quilolitro para mililitro')
        print('3) Litro para quilolitro')
        print('4) Litro para mililitro')
        print('5) Mililitro para quilolitro')
        print('6) Mililitro para litro')

    if escolha3 == 5:
        print('1) Hora para minuto')
        print('2) Hora para segundo')
        print('3) Minuto para hora')
        print('4) Minuto para segundo')
        print('5) Segundo para hora')
        print('6) Segundo para minuto')

    escolha = int(input('Digite o número correspondente a sua conversão: '))
    if escolha == 0:
        print('Obrigado por usar o programa!')
        break
    escolha2 = float(input('Digite a quantidade da unidade que você deseja converter: ').replace(',', '.'))

    if escolha3 == 1:
        if escolha == 1:
            resultado = escolha2 * 1000
            print(f'A conversão de {escolha2}km para metros fica: {resultado:.2f}m')

        if escolha == 2:
            resultado = escolha2 * 100000
            print(f'A conversão de {escolha2}km para centimetros fica: {resultado:.2f}cm')

        if escolha == 3:
            resultado = escolha2 / 1000
            print(f'A conversão de {escolha2}m para quilometros fica: {resultado:.2f}km')

        if escolha == 4:
            resultado = escolha2 * 100
            print(f'A conversão de {escolha2}m para centimetros fica: {resultado:.2f}cm')

        if escolha == 5:
            resultado = escolha2 / 100
            print(f'A conversão de {escolha2}cm para metros fica: {resultado:.2f}m')

        if escolha == 6:
            resultado = escolha2 / 100000
            print(f'A conversão de {escolha2}cm para quilometros fica: {resultado:.2f}km')


    if escolha3 == 2:
        if escolha == 1:
            resultado = escolha2 * 1000
            print(f'A conversão de {escolha2}kg para gramas fica: {resultado:.2f}g')

        if escolha == 2:
            resultado = escolha2 * 1000000
            print(f'A conversão de {escolha2}kg para miligramas fica: {resultado:.2f}mg')

        if escolha == 3:
            resultado = escolha2 / 1000
            print(f'A conversão de {escolha2}g para quilogramas fica: {resultado:.2f}kg')

        if escolha == 4:
            resultado = escolha2 * 1000
            print(f'A conversão de {escolha2}g para miligramas fica: {resultado:.2f}mg')

        if escolha == 5:
            resultado = escolha2 / 1000000
            print(f'A conversão de {escolha2}mg para quilogramas fica: {resultado:.2f}kg')

        if escolha == 6:
            resultado = escolha2 / 1000
            print(f'A conversão de {escolha2}mg para gramas fica: {resultado:.2f}g')

    
    if escolha3 == 3:
        if escolha == 1:
            resultado = escolha2 * 0.20
            print(f'A conversão de {escolha2} reais para dólar americano fica: {resultado:.2f} dólares')

        if escolha == 2:
            resultado = escolha2 * 0.19
            print(f'A conversão de {escolha2} reais para euros fica: {resultado:.2f} euros')

        if escolha == 3:
            resultado = escolha2 * 0.16
            print(f'A conversão de {escolha2} reais para libras esterlinas fica: {resultado:.2f} libras')

        if escolha == 4:
            resultado = escolha2 * 4.97
            print(f'A conversão de {escolha2} dólares americanos para reais fica: {resultado:.2f} reais')

        if escolha == 5:
            resultado = escolha2 * 0.93
            print(f'A conversão de {escolha2} dólares americanos para euros fica: {resultado:.2f} euros')

        if escolha == 6:
            resultado = escolha2 * 0.79
            print(f'A conversão de {escolha2} dólares americanos para libras esterlinas fica: {resultado:.2f} libras')

        if escolha == 7:
            resultado = escolha2 * 5.35
            print(f'A conversão de {escolha2} euros para reais fica: {resultado:.2f} reais')

        if escolha == 8:
            resultado = escolha2 * 1.08
            print(f'A conversão de {escolha2} euros para dólares americanos fica: {resultado:.2f} dólares')

        if escolha == 9:
            resultado = escolha2 * 0.85
            print(f'A conversão de {escolha2} euros para libras esterlinas fica: {resultado:.2f} libras')

        if escolha == 10:
            resultado = escolha2 * 6.26
            print(f'A conversão de {escolha2} libras esterlinas para reais fica: {resultado:.2f} reais')

        if escolha == 11:
            resultado = escolha2 * 1.26
            print(f'A conversão de {escolha2} libras esterlinas para dólares americanos fica: {resultado:.2f} dólares')

        if escolha == 12:
            resultado = escolha2 * 1.16
            print(f'A conversão de {escolha2} libras esterlinas para euros fica: {resultado:.2f} euros')


    if escolha3 == 4:
        if escolha == 1:
            resultado = escolha2 * 1000
            print(f'A conversão de {escolha2} quilolitros para litros fica: {resultado:.2f} litros')

        if escolha == 2:
            resultado = escolha2 * 1000000
            print(f'A conversão de {escolha2} quilolitros para mililitros fica: {resultado:.2f} mililitros')

        if escolha == 3:
            resultado = escolha2 / 1000
            print(f'A conversão de {escolha2} litros para quilolitros fica: {resultado:.2f} quilolitros')

        if escolha == 4:
            resultado = escolha2 * 1000
            print(f'A conversão de {escolha2} litros para mililitros fica: {resultado:.2f} mililitros')

        if escolha == 5:
            resultado = escolha2 / 1000000
            print(f'A conversão de {escolha2} mililitros para quilolitros fica: {resultado:.2f} quilolitros')

        if escolha == 6:
            resultado = escolha2 / 1000
            print(f'A conversão de {escolha2} mililitros para litros fica: {resultado:.2f} litros')


    if escolha3 == 5:
        if escolha == 1:
            resultado = escolha2 * 60
            print(f'A conversão de {escolha2} horas para minutos fica: {resultado:.2f} minutos')

        if escolha == 2:
            resultado = escolha2 * 3600
            print(f'A conversão de {escolha2} horas para segundos fica: {resultado:.2f} segundos')

        if escolha == 3:
            resultado = escolha2 / 60
            print(f'A conversão de {escolha2} minutos para horas fica: {resultado:.2f} horas')

        if escolha == 4:
            resultado = escolha2 * 60
            print(f'A conversão de {escolha2} minutos para segundos fica: {resultado:.2f} segundos')

        if escolha == 5:
            resultado = escolha2 / 3600
            print(f'A conversão de {escolha2} segundos para horas fica: {resultado:.2f} horas')

        if escolha == 6:
            resultado = escolha2 / 60
            print(f'A conversão de {escolha2} segundos para minutos fica: {resultado:.2f} minutos')


    pergunta = input('Você deseja repetir o programa? Digite Y para sim, e N para não. Em letras maiúsculas: ')

    if pergunta == 'Y':
        continue

    if pergunta == 'N':
        print('Obrigado por usar o programa!')
        break

input('Pressione qualquer tecla para fechar: ')
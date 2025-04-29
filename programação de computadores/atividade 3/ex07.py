soma_am =0
soma_ah =0
cont_m =0
cont_h =0

while True:
    sexo = str(input('digite o sexo f=feminino m=masculino, se quiser parar digite 0: '))

    if sexo == 0:
        break

    altura = float(input('digite a altura em metros: '))

    if sexo =='m':
        soma_am += altura #acumula a altura das mulheres
        cont_m +=1 #conta as mulheres p média

    if sexo =='h':
        soma_ah += altura
        cont_h +=1

if cont_m >0:
    media_m = soma_am / cont_m
    print(f'a altura media das mulheres é: {media_m:.2f} m.')
else:
    print('não foram registradas.')


if cont_h >0:
    media_h = soma_ah / cont_h
    print(f'a altura media dos homens é: {media_h:.2f} m.')
else:
    print('não foram registrados.')

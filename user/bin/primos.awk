#!/usr/bin/mawk -f
function primos(hasta){

#   Exepto 0 y 1, todos los demas son posible primo 
    for (primo=2; primo<=hasta; primo++)
        criba[primo] = 1

#   Tacho los productos
#   Recorro los multiplos en orden invertido para poder usar solo los primos
#   sin tener que considerar los cubos como casos especiales 
    for (primo = 2; primo <= sqrt(hasta); primo++)
        if (criba[primo])
            for (multiplo=int(hasta/primo); multiplo >= primo; multiplo--)
                criba[multiplo * primo] = 0

#   Muestro los numeros no tachados
    for (primo=2; primo <= hasta; primo++)
        if (criba[primo])
            print primo
}

BEGIN{
    if (ARGC == 2)
        primos(ARGV[1])
    else
        if (ARGC == 1)
        {
            print "No se especifico ningun valor, se calculara hasta 1000."
            primos(1000)
        }
        else
            print "Debe especificar un unico argumento numerico."
}

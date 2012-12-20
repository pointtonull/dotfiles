#!/home/deimos/bin/clif
#include <stdio.h>
#include <malloc.h>

#define hasta 10000000

enum boolean{False, True};
enum boolean criba[hasta + 1];
int primo, multiplo;

int main()
{

    /* Exepto 0 y 1, todos los demas son posible primo */
    for (primo=2; primo <= hasta; primo++)
        criba[primo] = True;

    /* Tacho los productos *
     * Recorro los multiplos en orden invertido para poder usar solo los primos
     * sin tener que considerar los cubos como casos especiales */
    for (primo=2; primo <= sqrt(hasta); primo++)
        if (criba[primo])
            for (multiplo=(hasta / primo); multiplo >= primo; multiplo--)
                if (criba[multiplo])
                    criba[primo * multiplo] = False;

    /* Muestro los numeros no tachados */
    for (primo=2; primo <= hasta; primo++)
        if (criba[primo])
            printf("%d\n", primo);

    return 0;
};


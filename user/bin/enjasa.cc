echo Hola ma!
awk '

function procesa(agencia, cadena){
    filename = "~/documentos/temporales/" agencia ".html"
    system("enjasa.pago cc " cadena "> " filename "&& navegador " filename)
}

BEGIN{
    printf "\nGenerar: "
}

{
    if (/\*/){
        split("75,17,141,148,110,69", a, ",")
        for (i=1; i<=length(a); i++){
            cadena = $0
            gsub("*", a[i], cadena)
            procesa(a[i], cadena)
        }
    }
    else
        procesa($1, $0)
    printf "\nGenerar: "
}'

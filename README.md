### Cliente y Servidor TCP en Python

#### Librerias utilizadas
* socket
* time

#### Instrucciones de uso

* Para la ejecución de los archivos .py no es necesario un entorno virtual, puede realizarla en su python global.
* Ejecutar en una terminal (cmd, bash, etc)
    `python servidor.py`
* Ejecutar en otra terminal (cmd, bash, etc)
    `python cliente.py`

#### Funcionalidad
##### Servidor
* El servidor se queda escuchando por 30 segundos, alguna conexión de cliente o clientes. Si no fuera así, el servidor se cierra automaticamente por inactividad.
* Se muestra en pantalla cuando la conexión ha sido recibida por algún cliente
* Si el cliente envia algun mensaje, se muestra en pantalla.
* Si el cliente manda el mensaje de DESCONEXION, el servidor se desconecta del cliente y se queda a la espera de algun cliente.
##### Cliente
* Se conecta al servidor al localhost y puesto correspondiente. En caso contrario, muestra un mensaje de error de conexión.
* Solicita al usuario un mensaje. En caso de teclear DESCONEXION se cierra la conexion, en caso contrario, se envia el mensaje y se recibe la respuesta del servidor del mismo mensaje pero en mayusculas.
* Se puede interrumpir la conexión tecleando ctrl + c

#### Pruebas manuales



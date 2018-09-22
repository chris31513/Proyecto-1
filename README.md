  # Proyecto-1
  Versión:<br />
    python 2.7<br />
    <br />
    
  Uso:<br />
    interfaz gráfica: <br />
      $ make run_interfaz<br />
    modo terminal del server (al abrir, se solicitará el puerto y se ejecutarán las pruebas unitarias):<br />
      $ make run_server<br />
   modo terminal del cliente (al abrir, se solicitara a la ip del host al que se quiere conectar y el puerto, además de que se     ejecutarán las pruebas unitarias):<br />
      $ make run_cliente

  Recomendaciones:<br />
    Se recomienda instalar python-tk para la interfaz gráfica.<br />
    Es demasiado recomendable que, después de ejecutar la interfaz gráfica ó el modo terminal, se ejectue el comando:<br />
      $ make clean
      
  Errores conocidos:<br />
    -El servidor puede quedarse colgado y se debe matar con:<br />
      $ ps<br />
      $ kill -9 PID<br />
    -Puede que las pruebas no pasen en algún intento, porque el servidor no libera el puerto que está usando.<br />
    -Si el servidor termina antes que el cliente, el cliente entra en bucle infinito que imprime en la pantalla.<br />
    -La interfaz a veces no muestra los mensajes, además de que se debe apretar enter en la ventana de "Conectar" y em la de  "Chat" en cada cuadro de texto para que le programa capture lo que escribiste.<br />

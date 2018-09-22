.PHONY: clean 
run_server: 
	python2.7 src/MainServer.py
run_cliente: 
	python2.7 test/Test.py
	python2.7 src/MainCliente.py
	mkdir trash
	mv src/*.pyc trash
run_interfaz:
	python2.7 test/Test.py
	python2.7 src/Controlador.py
	mkdir trash
	mv src/*.pyc trash
	mv ig/*.pyc trash
clean:
	rm -r trash




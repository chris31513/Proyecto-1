.PHONY: clean 
run_server: test_servidor
	python src/Server.py
	mkdir trash
	mv src/*.pyc trash
run_cliente: test_cliente
	python src/Cliente.py
	mkdir trash
	mv src/*.pyc trash
clean:
	rm -r trash
test_cliente:
	python test/TestCliente.py
test_servidor:
	python test/TestServer.py



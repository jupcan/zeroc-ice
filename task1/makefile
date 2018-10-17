shutdown_systemctl:
	sudo systemctl stop icegridregistry
	sudo systemctl stop icegridnode

node1:
	mkdir -p /tmp/db/registry
	icegridregistry --Ice.Config=node1.config

server:
	./server.py --Ice.Config=server.config

client:
	./client.py --Ice.Config=client.config "printer1 -t @ PrinterAdapter1"

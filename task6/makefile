shutdown_systemctl:
	sudo systemctl stop icegridregistry
	sudo systemctl stop icegridnode

node1:
	mkdir -p /tmp/db/node1
	mkdir -p /tmp/db/registry
	icegridnode --Ice.Config=node1.config

node2:
	mkdir -p /tmp/db/node2
	icegridnode --Ice.Config=node2.config

copy_binaries:
	mkdir -p /tmp/printer
	cp server.py /tmp/printer
	cp client.py /tmp/printer
	cp printer.ice /tmp/printer
	cp printerfactory.ice /tmp/printer
	icepatch2calc /tmp/printer

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import Ice
Ice.loadSlice('-I. --all printerfactory.ice')
import Example

class Client(Ice.Application):
    def run(self, argv):
        proxy = self.communicator().stringToProxy(argv[1])
        factory = Example.PrinterFactoryPrx.checkedCast(proxy)

        if not factory:
            raise RuntimeError('Invalid proxy')

        printer = factory.make("printer1")
        printer2 = factory.make("printer2")
        printer.write('hello world!')
        printer2.write('hello world!')
        factory.removeprxy(printer)
        return 0

sys.exit(Client().main(sys.argv))

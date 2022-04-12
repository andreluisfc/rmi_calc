import Pyro4
from Pyro4 import naming
import _thread
import json


@Pyro4.expose
class Calculadora(object):

    @staticmethod
    def somar(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtrair(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def dividir(a: float, b: float) -> float:
        return a / b

    @staticmethod
    def multiplicar(a: float, b: float) -> float:
        return a * b


server = _thread.start_new_thread(naming.startNSloop, ())

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(Calculadora)
ns.register('calculadora', uri)
print("Calculadora registrada", uri)
daemon.requestLoop()

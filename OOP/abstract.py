# interfaces show what methods a class must implement without providing the implementation details. 
# implementation we implement the declaration of the method in the interface
# properties you should not be able to create an object of abstract class, abstract method should be part of abstract class
# abstract method does not have a implementation in the abstract class, it must be implemented by the subclass

from abc import ABC, abstractmethod

#example
class PaymentGateway(ABC):

    @abstractmethod
    def pay(self):
        pass

class RazorPay(PaymentGateway):

    def pay(self):
        print("Payment processed through RazorPay")


class Purchase:

    def __init__(self, gateway):
        self.gateway = gateway

    def checkout(self):
        print("Processing payment through gateway...")
        self.gateway.pay()

gateway = RazorPay()
purchase = Purchase(gateway)
purchase.checkout()



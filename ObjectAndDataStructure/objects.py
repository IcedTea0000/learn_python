import json

class Customer():
    def __init__(self, name):
        self.name = name

    pass


class Customer2():
    area = 'North America'

    def __init__(self):
        self.name: str
        pass

    def register(self):
        print('{} registers information'.format(self.name))
        pass
    pass


class ElderCustomer(Customer2):
    def __init__(self):
        Customer2.__init__(self)
        print('elder customer init')
        pass

    def register(self):
        print('{} registers with override method'.format(self.name))


    def __str__(self):
        return json.dumps(self.__dict__, indent=2)
    pass


if __name__ == '__main__':
    # my_customer = Customer(name='Martin')
    # my_customer.name = 'updated'
    # print(my_customer.name)
    # my_customer = Customer2()
    # my_customer.name = 'Martin'
    # print(my_customer.name)
    # my_customer.register()
    #
    # my_customer2 = Customer2()
    # my_customer.area = 'South America'
    # print(my_customer2.area)
    # print(my_customer2.area)

    my_elder_customer = ElderCustomer()
    print(my_elder_customer.area)
    my_elder_customer.name = 'Elder'
    my_elder_customer.register()

    print(my_elder_customer)

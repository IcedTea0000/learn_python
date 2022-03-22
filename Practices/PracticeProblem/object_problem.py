class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.__dict__)


class Kangaroo():
    def __init__(self, name=None, pouch_contents=None):
        self.name = name
        if pouch_contents == None:
            pouch_contents = []
        self.pouch_contents = pouch_contents

    def put_in_pouch(self, input_object):
        self.pouch_contents.append(input_object)

    def __str__(self):
        return ('{} : {}'.format(self.name, str(self.pouch_contents)))


if __name__ == '__main__':
    # point1 = Point()
    # print(point1)

    kanga = Kangaroo('kanga')
    roo = Kangaroo('roo')

    kanga.put_in_pouch('waller')
    kanga.put_in_pouch('keys')
    kanga.put_in_pouch(roo)
    print(kanga)
    print(roo)

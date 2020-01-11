class Hewan(object):
    def __init__(self, nama):
        self.nama = nama

    def gonggong(self):
        print 'Suara gonggongan hewan'

class Anjing(Hewan):
    def gonggong(self):
        super(Anjing, self).gonggong()
        return "woork"

class Srigala(Hewan):
    def gonggong(self):
        Hewan.gonggong(self)
        return "hooooowll"

class Singa(Hewan):
    def gonggong(self):
       return "Roaaarsss"

dog = Anjing('Anjing')
wolf = Srigala('Serigala')
lion = Singa('Singa')

print 'Suara ' + dog.nama + ' yaitu ' + dog.gonggong()
print 'Suara ' + wolf.nama + ' yaitu ' + wolf.gonggong()
print 'Suara ' + lion.nama + ' yaitu ' + lion.gonggong()

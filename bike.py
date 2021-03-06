
class Bike(object):
    def __init__(self, price, max_speed):

        self.price = price
        self.max_speed = max_speed
        self.miles= 0

    def displayInfo(self):
        print 'Price is: $' +  str(self.price)
        print 'Max speed: ' + str(self.max_speed) + "mph"
        print 'Total miles: ' + str(self.miles) + "miles"
        return self

    def ride(self):
        print "Riding"
        self.miles+= 10


    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5

bike1 = Bike(300, 25)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(200, 15)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike(100, 10)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()

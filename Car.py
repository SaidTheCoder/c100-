class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.model=model
        self.color=color
        self.company=company
        self.speed_limit=speed_limit
        
    def start(self):
        print("Car has started!!!")
    def stop(self):
        print("THE CAR HAS STOPED!!!")
    def accelerate(self):
        print("THE CAR HAS ACCELERATED!!")
    def changeGear(self):
        print("THE CAR CHANGED GEAR")
        
truck=Car("a6","red","tata",80)
print(truck.start())
print(truck.stop())
print(truck.accelerate())
print(truck.changeGear())

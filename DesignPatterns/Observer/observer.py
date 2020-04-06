import abc 


class Subject(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def add_observer(self, subscriber):
        pass
    
    @abc.abstractmethod
    def remove_observer(self, subscriber):
        pass
    
    @abc.abstractmethod
    def do_notify(self):
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        self.subscribers = []
        self.msg = ""

    def add_observer(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_observer(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def do_notify(self):
        for subscriber in self.subscribers:
            subscriber.update_status(self.msg)

    def twitt(self, new_msg):
        self.msg = new_msg
        self.do_notify()


class Observer(metaclass = abc.ABCMeta):
    @abc.abstractmethod 
    def update_status(self, msg):
        pass

    def subscribe(self, subject):
        subject.add_observer(self)

    def unsubscribe(self, subject):
        subject.remove_observer(self)

    def __init__(self, name):
        self.name = name 

    
class FirstView(Observer):
    
    def __init__(self, name):
        super().__init__(name)

    def update_status(self, msg):
        print("------------------")
        print(f"{self.name} wall")
        print(f"<h1> {msg} </h1>")
        print("------------------")

class SecondView(Observer):
    def __init__(self, name):
        super().__init__(name)

    def update_status(self, msg):
        print("------------------")
        print(f"{self.name} wall")
        print(f"<h2> {msg} </h2>")
        print("------------------")


#============================ client part ===================================


def main():
    Hajiahmad = ConcreteSubject()


    VusalaAlekberova = FirstView('Vusala')
    AliAskarli = FirstView('Ali')
    TapdigMaharramli = SecondView('Tapdig')

    
    VusalaAlekberova.subscribe(Hajiahmad)
    TapdigMaharramli.subscribe(Hajiahmad)
    '''    
    subject.add_observer(VusalaAlekberova)
    subject.add_observer(AliAskarli)
    subject.add_observer(TapdigMaharramli)
    '''
    

    VusalaAlekberova.unsubscribe(Hajiahmad)

    Hajiahmad.twitt('hello there')

    AliAskarli.subscribe(Hajiahmad)
    
    Hajiahmad.twitt('hi there this is my second status')


if __name__ == "__main__":
    main()















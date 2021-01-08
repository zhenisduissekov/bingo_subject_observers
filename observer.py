from abc import ABCMeta, abstractmethod
import random


class IObservable(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def subscribe(observer):
        "The subscribe method"

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        "The unsubscribe method"

    @staticmethod
    @abstractmethod
    def notify(observer):
        "The notify method"


class Subject(IObservable):
    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, number):
        print(f"We got number: {number}")
        for observer in self._observers:
            observer.notify(self, number)


class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def notify(observable, *args, **kwargs):
        "Receive notifications"


class Observer(IObserver):
    def __init__(self, observable, name):
        self.name = name
        self.ownlist = [round(100*random.random()) for _ in range(5)]
        self.list = []
        print(self.name, self.ownlist)
        observable.subscribe(self)

    def notify(self, observable, number):
        self.list.append(number)
        for i in self.ownlist:
            if i not in self.list:
                return
        print(f'{self.name} BINGO!!!\n\n')
        print_numbers(self.ownlist, self.list)
        exit(0)


def print_numbers(win_list, full_list):
    counter = 1
    for i in full_list:
        if i in win_list:
            print('\033[1m' + str(i) + "\033[0m", end='')
        else:
            print(str(i), end='')
        if counter % 10 == 0:
            print('\n', end='')
        else:
            print(' ', end='')
        counter += 1


SUBJECT = Subject()

OBSERVER1 = Observer(SUBJECT, name="AZAMAT")
OBSERVER2 = Observer(SUBJECT, name="BERIK")
OBSERVER2 = Observer(SUBJECT, name="ALMAZ")
OBSERVER2 = Observer(SUBJECT, name="SAKEN")
OBSERVER2 = Observer(SUBJECT, name="GULSHAT")

counter = 0
print("Welcome to the bingo game")
while True:
    SUBJECT.notify(round(100*random.random()))


__author__    = 'Bojan Delic <bojan@delic.in.rs>'
__date__      = 'Aug 23, 2013'
__copyright__ = 'Copyright (c) 2013 Bojan Delic'

import os
import wpf
from mvvm import ViewModel, Notifiable, command, notifiable, List
from System.Windows import Application, Window


class Person(ViewModel):
    name = Notifiable()
    age = Notifiable()

    def __init__(self, name, age):
        super(Person, self).__init__()
        self.name = name
        self.age = age


# Every user ViewModel should inherit from ViewModel
class MyViewModel(ViewModel):
    # creation of properties whose setters automatically
    # invokes PropertyChanged event. Initial value is optional.
    text1 = Notifiable('initial value')
    text2 = Notifiable()
    elements = Notifiable(List([Person('John', 23), Person('Phil', 33)]))
    
    @notifiable
    def text3(self):
        return 'Initial value for text3'

    # using decorator to turn method to subclass of ICommand interface
    @command
    def ClickCommand(self):
        self.text2 = 'This will show up after click'
        for person in self.elements[1:]:
            person.name = 'Bob'
        self.elements.append(Person('Sam', 12))


# Just creating window and adding DataContext, nothing special here
class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, os.path.join(os.path.dirname(__file__), 'example1.xaml'))
        self.DataContext = MyViewModel()

if __name__ == '__main__':
    Application().Run(MyWindow())

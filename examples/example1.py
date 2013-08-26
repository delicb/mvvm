__author__    = 'Bojan Delic <bojan@delic.in.rs>'
__date__      = 'Aug 23, 2013'
__copyright__ = 'Copyright (c) 2013 Bojan Delic'

import os
import wpf
from mvvm import ViewModelBase, Notifiable, command
from System.Windows import Application, Window


# Every ViewModel should inherit from ViewModelBase
class MyViewModel(ViewModelBase):
    # creation of properties whose setters automatically
    # invokes PropertyChanged event. Initial value is optional.
    Text1 = Notifiable('initial value')
    Text2 = Notifiable()

    # using decorator to turn method to subclass of ICommand interface
    @command
    def ClickCommand(self):
        self.Text2 = 'This will show up after click'


# Just creating window and adding DataContext, nothing special here
class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, os.path.join(os.path.dirname(__file__), 'example1.xaml'))
        self.DataContext = MyViewModel()

if __name__ == '__main__':
    Application().Run(MyWindow())

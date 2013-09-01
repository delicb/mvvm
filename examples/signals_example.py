__author__    = 'Bojan Delic <bojan@delic.in.rs>'
__date__      = 'Sep 1, 2013'
__copyright__ = 'Copyright (c) 2013 Bojan Delic'

import os
import wpf
from mvvm import ViewModel, Signal, Notifiable, command
from System.Windows import Window, Application


class MyViewModel(ViewModel):
    text1 = Notifiable('always showing')
    text2 = Notifiable()

    # Creating signal by creating instance of class
    signal = Signal()

    def __init__(self):
        super(MyViewModel, self).__init__()

        # Subscribe to signal. This will probably be in different view model
        # in real application
        self.signal.connect(self.on_signal)

    # signal handler - it will be all parameters provided in `emit` method
    # of signal
    def on_signal(self, content):
        self.text2 = content

    @command
    def send_signal(self):
        # on some event - emit signal with provided parameters
        self.signal.emit('from signal')


class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, os.path.join(os.path.dirname(__file__), 'signals_example.xaml'))
        self.DataContext = MyViewModel()

if __name__ == '__main__':
    Application().Run(MyWindow())

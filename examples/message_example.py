__author__    = 'Bojan Delic <bojan@delic.in.rs>'
__date__      = 'Aug 30, 2013'
__copyright__ = 'Copyright (c) 2013 Bojan Delic'

import os
import wpf
import time
from threading import Thread
from mvvm import ViewModel, Notifiable, command, notifiable, List
from System.Windows import Application, Window


class MyViewModel(ViewModel):
    text1 = Notifiable('always showing')
    text2 = Notifiable()
    
    def __init__(self):
        super(MyViewModel, self).__init__()
        # subscribe to message with id 'messageId'
        self.messenger.subscribe('messageId', self.on_message)

    # message handler - will be executed in GUI thread
    def on_message(self, content):
        self.text2 = content


# Just creating window and adding DataContext, nothing special here
class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, os.path.join(os.path.dirname(__file__), 'message_example.xaml'))
        self.DataContext = MyViewModel()

        # thread that wats for 3 seconds and then sends message with content
        def threaded_function(messenger):
            time.sleep(3)
            messenger.send('messageId', 'This will show up in GUI')
        t = Thread(target=threaded_function, args=(self.DataContext.messenger,))
        t.start()

if __name__ == '__main__':
    Application().Run(MyWindow())

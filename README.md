IronPythonMVVM
==============

Set of helper classes for easier using MVVM pattern with WPF and IronPython.

Inspired by http://www.galasoft.ch/mvvm/, but addapted to be more pythonic.

Example of creating ViewModel:

```python
from mvvm import ViewModelBase, Notifiable, command

class MyViewModel(ViewModelBase):
    TextField = Notifiable()

    @command
    def MyCommand(self):
        # do something
        # maybe update `TestField`, event will be raise automatically
        TextField = 'some value'
```

This view model can be used in XAML just as if `INotifyPropertyChanged`
and `ICommand` is implemented directly.

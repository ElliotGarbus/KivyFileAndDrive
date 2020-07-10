from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty


class LoadDialog(Popup):
    filters = ListProperty()
    path = StringProperty()

    def __init__(self, **kwargs):
        self.filters = kwargs['filters']
        self.path= kwargs['path']
        super().__init__(**kwargs)


class SaveDialog(Popup):
    filters = ListProperty()
    path = StringProperty()

    def __init__(self, **kwargs):
        self.filters = kwargs['filters']
        self.path= kwargs['path']
        super().__init__(**kwargs)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty


class TestBox(BoxLayout):
    pass


class FCTest(App):
    pass


# class LoadDialog(Popup):
#     filters = ListProperty()
#     path = StringProperty()
#
#     def __init__(self, **kwargs):
#         self.filters = kwargs['filters']
#         self.path= kwargs['path']
#         super().__init__(**kwargs)
#
#
# class SaveDialog(Popup):
#     filters = ListProperty()
#     path = StringProperty()
#
#     def __init__(self, **kwargs):
#         filters = kwargs['filters']
#         path= kwargs['path']
#         super().__init__(**kwargs)


if __name__ == '__main__':
    FCTest().run()

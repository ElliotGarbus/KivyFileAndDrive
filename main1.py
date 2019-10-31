from kivy.app import App
from kivy.lang.builder import Builder


kv = '''
#: import Factory kivy.factory.Factory
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: '30dp'
        Button:
            text: 'Open PopUp'
            on_release:
                Factory.MyPopUp().open()

<MyPopUp@Popup>:
    auto_dismiss: True
    title: 'Just a test'
    size_hint: .6,.75
    BoxLayout:
        orientation: 'vertical'
        Label:
            size_hint_y: .1
            text: 'size: ' + str(root.size) + ' pos: ' + str(root.pos)
        Button:
            size_hint_y: .1
            text: 'Cancel'
            on_release: root.dismiss()
        FileChooserListView:
            size_hint_y: .8
            path: '.'
        
'''


class PUPTestApp(App):
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    PUPTestApp().run()

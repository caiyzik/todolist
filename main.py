from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.clock import Clock

from datetime import datetime, timedelta

Window.size = (500, 400)

class ToDoListItem(BoxLayout):
    btn_text = StringProperty()
    timer_text = StringProperty()
    elapsed = 0

    def update(self, dt):

        sec = timedelta(self.elapsed)
        d = datetime(1, 1, 1) + sec

        time_str = "%02d:%02d:%02d:%02d" % (d.second, d.minute, d.hour, d.day - 1)
        self.timer_text = time_str
        self.elapsed+=1

    def onClick(self):
        event = Clock.schedule_interval(self.update, 1)
        #event_trig = Clock.create_trigger(self.update, 1)
        if self.btn_text == "Start":
            self.btn_text = "Stop"
            #event_trig()
        else:
            self.btn_text = "Start"
            event.cancel()

class ToDoLayout(BoxLayout):

    def sort(self):
        self.rv.data = sorted(self.rv.data, key=lambda x: x['value'])

    def clear(self):
        self.rv.data = []

    def insert(self, value):
        self.rv.data.insert(0, {'item_text': value or 'default value'})

    def update(self, value):
        if self.rv.data:
            self.rv.data[0]['value'] = value or 'default new value'
            self.rv.refresh_from_data()

    def remove(self):
        if self.rv.data:
            self.rv.data.pop(0)

class ToDoApp(App):
    def build(self):
        return ToDoLayout()

td = ToDoApp()
td.run()
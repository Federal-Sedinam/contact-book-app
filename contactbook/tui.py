from textual.app import App
from textual.widgets import Footer, Header

class ContactsApp(App):
    def compose(sef):
        yield Header()
        yield Footer()

    def on_mount(self):
        self.title = "RP Contacts"
        self.sub_title = "A Contacts Book App With Textual And Python"
        
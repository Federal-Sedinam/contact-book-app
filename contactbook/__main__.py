from contactbook.database import Database
from contactbook.tui import ContactsApp

def main():
    app = ContactsApp(db=Database())
    app.run()

if __name__ =="__main__":
    main()

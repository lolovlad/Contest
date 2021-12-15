import eel


@eel.expose
def retrieve():
    eel.show("main.html")


@eel.expose
def open_posl():
    eel.show("posl.html")


if __name__ == '__main__':
    eel.init('templates')
    eel.start('login.html', mode="chrome", size=(760, 760))
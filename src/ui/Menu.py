class Menu():

    def __init__(self, ui):
        self.menu = {}

        self.add_menu('main')
        self.add_option("main", "Start", "callback")
        self.add_option("main", "Options", "callback")
        self.add_option("main", "End", "callback")
        
        print(self.menu)

    def add_menu(self, name, parent = None):
        self.menu[name] = {
            'options': [],
            'scroler': 0,
            'parent': parent
        }

    def add_option(self, menu_name, option_name, callback):
        if menu_name not in self.menu:
            print(menu_name, " doesn't exist")
            return
        self.menu[menu_name]['options'].append({
            'name': option_name,
            'callback': callback
        })

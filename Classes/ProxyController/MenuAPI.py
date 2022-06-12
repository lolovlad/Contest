from Interfase.Proxy.Menu import Menu
from Classes.RequestsAPI import RequestsAPI
from Classes.ProxyController.AdminPanelAPI import AdminPanelAPI
from functools import partial


class MenuAPI(Menu):

    __api = RequestsAPI("123")

    def load_to_database_contest(self, data):
        admin_panel = AdminPanelAPI()
        return admin_panel.load_to_database_contest(data)
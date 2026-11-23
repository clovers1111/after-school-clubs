from PySide6.QtWidgets import QWidget, QPushButton, QComboBox, QTableView

from controller import HomeController
from views.components import GenericTable


class HomeView(QWidget):
    home_controller: HomeController
    loading: bool = False



    def __init__(self, controller: HomeController, rows, headers):
        super().__init__()

        self.home_controller = controller

        # widgets
        # Need a widget for the clubs
        self._clubs_dropdown = QComboBox(placeholderText="Club")

        # Opens a view of the club
        self._open_club = QPushButton("View")
        self._open_club.clicked.connect(self.open_club)
        # Re-fetches clubs
        self._refresh_clubs = QPushButton("Refresh")
        self._refresh_clubs.clicked.connect(self.refresh_clubs)
        # Should open a prompt to add a new club
        self._add_club = QPushButton("Add")
        self._add_club.clicked.connect(self.open_add_club)


        # This is our model
        self._table_model = GenericTable(rows, headers)
        # This is the actual drawn display
        self._table = QTableView()
        self._table.setModel(self._table_model)


    def set_clubs(self, clubs):
        self._table_model.set_clubs(clubs)

    def open_club(self):
        # needs to create a new popup
        return
        self.loading = True
        self.home_controller.open_club()

    def refresh_clubs(self):
        self.loading = True
        self.home_controller.fetch_clubs()
        self.loading = False

    def open_add_club(self):
        return




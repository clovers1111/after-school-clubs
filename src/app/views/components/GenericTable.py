from PySide6.QtCore import QAbstractTableModel, Qt

# Reusable table model: give it rows (tuples/lists) and column headers.
class GenericTable(QAbstractTableModel):

    def __init__(self, rows, headers):
        super().__init__()
        self.rows = rows          # from cursor.fetchall()
        self.headers = headers

    def set_rows(self, rows):
        self.beginResetModel()
        self.rows = rows
        self.endResetModel()

    def rowCount(self, parent=None):
        return len(self.rows)

    def columnCount(self, parent=None):
        return len(self.headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self.rows[index.row()][index.column()]
            return "" if value is None else str(value)
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if (role == Qt.ItemDataRole.DisplayRole
                and orientation == Qt.Orientation.Horizontal):
            return self.headers[section]
        return None
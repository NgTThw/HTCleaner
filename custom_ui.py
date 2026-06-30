from PySide6.QtWidgets import QComboBox
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import Qt


class CheckableComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setModel(QStandardItemModel(self))
        self.view().pressed.connect(self.handle_item_pressed)
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().setPlaceholderText("Select options...")
        self.model().dataChanged.connect(self.update_display_text)

    def add_checkable_item(self, text, item_id, checked=False):
        """Add an item with a checkbox."""
        item = QStandardItem(text)
        item.iid = item_id
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        item.setData(Qt.Checked if checked else Qt.Unchecked, Qt.CheckStateRole)
        self.model().appendRow(item)

    def handle_item_pressed(self, index):
        """Toggle checkbox state when clicked."""
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)
    
    def set_only_item_id(self, ids, checked):
        for i in range(self.model().rowCount()):
            item = self.model().item(i)
            if item.iid in ids :
                item.setCheckState(Qt.Checked if checked else Qt.Unchecked)
            else:
                item.setCheckState(Qt.Unchecked if checked else Qt.Checked)
        self.update_display_text()

    def update_display_text(self):
        """Update the combo box text to show selected items."""
        selected_items = []
        for i in range(self.model().rowCount()):
            item = self.model().item(i)
            if item.checkState() == Qt.Checked:
                selected_items.append(item.text())
        self.lineEdit().setText(", ".join(selected_items))

    def checked_items(self):
        """Return a list of checked item texts."""
        return [(self.model().item(i).text(), self.model().item(i).iid) for i in range(self.model().rowCount()) if self.model().item(i).checkState() == Qt.Checked]

    def checked_item_ids(self):
        return [self.model().item(i).iid for i in range(self.model().rowCount()) if self.model().item(i).checkState() == Qt.Checked]

import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QTableView,
    QHeaderView, QVBoxLayout, QHBoxLayout, QRadioButton,
    QToolBar, QAction, QFileDialog, QPushButton,
)
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from tools import read_csv_data
from widgets import AdvanceSearchDialog
from db import session
from models import Row


class Viewer(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(900, 700)
        self.setStyleSheet("background: #b4bfff") # rgb(180, 191, 255)
        # self.setStyleSheet("colour:red")
        mainLayout = QVBoxLayout()
        searchLayout = QHBoxLayout()
        id_r_button = QRadioButton("ID")
        id_r_button.check_index = 0
        id_r_button.toggled.connect(self.choice_search_field)
        details_r_button = QRadioButton("Details")
        details_r_button.check_index = 1
        details_r_button.toggled.connect(self.choice_search_field)
        death_r_button = QRadioButton("Date of death")
        death_r_button.check_index = 2
        death_r_button.toggled.connect(self.choice_search_field)
        f_name_r_button = QRadioButton("First name")
        f_name_r_button.check_index = 3
        f_name_r_button.toggled.connect(self.choice_search_field)
        m_name_r_button = QRadioButton("Middle name")
        m_name_r_button.check_index = 4
        m_name_r_button.toggled.connect(self.choice_search_field)
        s_name_r_button = QRadioButton("Surname")
        s_name_r_button.check_index = 5
        s_name_r_button.toggled.connect(self.choice_search_field)
        address_r_button = QRadioButton("Address")
        address_r_button.check_index = 6
        address_r_button.toggled.connect(self.choice_search_field)

        tool_bar = QToolBar("Tool Bar")
        tool_bar.setAutoFillBackground(True)
        tool_bar.setStyleSheet("QToolBar {background-color: #b4bfff; margin: 0px; padding: 3px;}")
        update_action = QAction("Load from CSV", self)
        update_action.setStatusTip("Load new data to database from csv file")
        update_action.triggered.connect(self.action_update)
        refresh_table = QAction("Refresh table", self)
        refresh_table.triggered.connect(self.action_refresh_table)
        tool_bar.addAction(update_action)
        tool_bar.addAction(refresh_table)
        mainLayout.addWidget(tool_bar)

        data = []
        qs = session.query(Row).all()
        if len(qs):
            for item in qs:
                data.append([item.item_id, item.detail, item.d_o_d, item.f_name, item.m_name, item.s_name, item.address])
        else:
            data.append(["2101032", "Lamberts Solicitors, 60 Commercial Road, Paddock Wood, Kent TN12 6DP. (G.K.C. Chapman)",
            "03-Dec-13", "Audrey", "May", "Ballard", "45 Warrington Road, Paddock Wood, Kent TN12 6HN"])
        self.headers = [
            "ID", "Details", "Date of death", "First name", "Middle name", "Surname", "Address"
        ]
        model = QStandardItemModel(len(data), len(data[0]))
        model.setHorizontalHeaderLabels(self.headers)
        for row, values in enumerate(data):
            for val in values:
                item = QStandardItem(val)
                model.setItem(row, values.index(val), item)
        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity())
        self.filter_proxy_model.setRecursiveFilteringEnabled(True)
        # self.filter_proxy_model.setFilterKeyColumn(0)
        # self.filter_proxy_model.setFilterKeyColumn(1)

        search_field = QLineEdit()
        search_field.setStyleSheet("font-size: 20px; height: 30px; background-color: lightgrey;")
        search_field.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
        searchLayout.addWidget(search_field)
        searchLayout.addWidget(id_r_button)
        searchLayout.addWidget(details_r_button)
        searchLayout.addWidget(death_r_button)
        searchLayout.addWidget(f_name_r_button)
        searchLayout.addWidget(m_name_r_button)
        searchLayout.addWidget(s_name_r_button)
        searchLayout.addWidget(address_r_button)
        mainLayout.addLayout(searchLayout)

        self.table = QTableView()
        self.table.setAutoFillBackground(True)
        self.table.setStyleSheet(
            "QTableView::item:selected{"
            "background-color:#8c96ff;"
            "}"
            "QHeaderView::section{"
            "border-top:5px solid lightgrey;"
            "border-left:5px solid lightgrey;"
            "border-right:5px solid lightgrey;"
            "border-bottom: 5px solid lightgrey;"
            "background-color:lightgrey;"
            "padding:0px;"
            "}"
            "QTableCornerButton::section{"
            "border-top:5px solid lightgrey;"
            "border-left:5px solid lightgrey;"
            "border-right:5px solid lightgrey;"
            "border-bottom: 5px solid lightgrey;"
            "background-color:lightgrey;"
            "}")
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setModel(self.filter_proxy_model)
        mainLayout.addWidget(self.table)

        id_r_button.setChecked(True)

        advance_search_dialog_button = QPushButton("Advance search", self)
        advance_search_dialog_button.setStyleSheet("background-color: lightgrey")
        advance_search_dialog_button.clicked.connect(self.advance_search_dialog)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(advance_search_dialog_button)
        self.setLayout(mainLayout)

    def action_update(self):
        fname = QFileDialog.getOpenFileName(parent=self, caption="Open file", filter="CSV Files (*.csv)")[0]
        if fname:
            data = read_csv_data(fname)
            fill_data_to_db = []
            for row in data:
                fill_data_to_db.append(Row(
                    item_id=row[0],
                    detail=row[1],
                    d_o_d=row[2],
                    f_name=row[3],
                    m_name=row[4],
                    s_name=row[5],
                    address=row[6],
                ))
            session.add_all(fill_data_to_db)
            session.commit()

            data = []
            qs = session.query(Row).all()
            for item in qs:
                data.append(
                    [item.item_id, item.detail, item.d_o_d, item.f_name, item.m_name, item.s_name, item.address])
            model = QStandardItemModel(len(data), len(data[0]))
            model.setHorizontalHeaderLabels(self.headers)
            for row, values in enumerate(data):
                for val in values:
                    item = QStandardItem(val)
                    model.setItem(row, values.index(val), item)
            self.filter_proxy_model.setSourceModel(model)
            self.table.setModel(self.filter_proxy_model)

    def action_refresh_table(self):
        data = []
        qs = session.query(Row).all()
        for item in qs:
            data.append(
                [item.item_id, item.detail, item.d_o_d, item.f_name, item.m_name, item.s_name, item.address])
        model = QStandardItemModel(len(data), len(data[0]))
        model.setHorizontalHeaderLabels(self.headers)
        for row, values in enumerate(data):
            for val in values:
                item = QStandardItem(val)
                model.setItem(row, values.index(val), item)
        self.filter_proxy_model.setSourceModel(model)
        self.table.setModel(self.filter_proxy_model)

    def choice_search_field(self):
        rb = self.sender()
        if rb.isChecked():
            self.filter_proxy_model.setFilterKeyColumn(rb.check_index)

    def advance_search_dialog(self):
        dlg = AdvanceSearchDialog(self)
        if dlg.exec_():
            data = []
            qs = session.query(Row).filter(
                Row.item_id.contains(dlg.id_edit_line.text()),
                Row.detail.contains(dlg.detail_edit_line.text()),
                Row.d_o_d.contains(dlg.dod_edit_line.text()),
                Row.f_name.contains(dlg.f_name_edit_line.text()),
                Row.m_name.contains(dlg.m_name_edit_line.text()),
                Row.s_name.contains(dlg.s_name_edit_line.text()),
                Row.address.contains(dlg.address_edit_line.text())
            ).all()
            for item in qs:
                data.append(
                    [item.item_id, item.detail, item.d_o_d, item.f_name, item.m_name, item.s_name, item.address])
            model = QStandardItemModel(len(data), len(data[0]))
            model.setHorizontalHeaderLabels(self.headers)
            for row, values in enumerate(data):
                for val in values:
                    item = QStandardItem(val)
                    model.setItem(row, values.index(val), item)
            self.filter_proxy_model.setSourceModel(model)
            self.table.setModel(self.filter_proxy_model)
        else:
            print("Cancel!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = Viewer()
    viewer.show()
    sys.exit(app.exec_())

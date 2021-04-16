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
        tool_bar.addAction(update_action)
        mainLayout.addWidget(tool_bar)


        data = [
            ["2101032", "Lamberts Solicitors, 60 Commercial Road, Paddock Wood, Kent TN12 6DP. (G.K.C. Chapman)",
            "03-Dec-13", "Audrey", "May", "Ballard", "45 Warrington Road, Paddock Wood, Kent TN12 6HN"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
            "Mary", "May", "Bee",
            "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101032", "Lamberts Solicitors, 60 Commercial Road, Paddock Wood, Kent TN12 6DP. (G.K.C. Chapman)",
             "03-Dec-13", "Audrey", "May", "Ballard", "45 Warrington Road, Paddock Wood, Kent TN12 6HN"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101032", "Lamberts Solicitors, 60 Commercial Road, Paddock Wood, Kent TN12 6DP. (G.K.C. Chapman)",
             "03-Dec-13", "Audrey", "May", "Ballard", "45 Warrington Road, Paddock Wood, Kent TN12 6HN"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
            ["2101034", "Frearsons, 50 Algitha Road, Skegness, Lincolnshire PE25 2AW. (Ian Dexter)", "11-Sep-13",
             "Mary", "May", "Bee",
             "Syne Hills Care Home, 16 Syne Avenue, Skegness, Lincolnshire PE25 3DJ formerly of5 Mount Pleasant, Wainfleet, Skegness, Lincolnshire"],
        ]
        headers = [
            "ID", "Details", "Date of death", "First name", "Middle name", "Surname", "Address"
        ]
        model = QStandardItemModel(len(data), len(data[0]))
        model.setHorizontalHeaderLabels(headers)

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

        table = QTableView()
        table.setAutoFillBackground(True)
        table.setStyleSheet(
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
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setModel(self.filter_proxy_model)
        mainLayout.addWidget(table)

        id_r_button.setChecked(True)

        advance_search_dialog_button = QPushButton("Advance search", self)
        advance_search_dialog_button.setStyleSheet("background-color: lightgrey")
        advance_search_dialog_button.clicked.connect(self.advance_search_dialog)
        mainLayout.addSpacing(10)
        mainLayout.addWidget(advance_search_dialog_button)
        self.setLayout(mainLayout)

    def action_update(self):
        fname = QFileDialog.getOpenFileName(parent=self, caption="Open file", filter="CSV Files (*.csv)" )[0]
        if fname:
            data = read_csv_data(fname)
            print(data)

    def choice_search_field(self):
        rb = self.sender()
        if rb.isChecked():
            self.filter_proxy_model.setFilterKeyColumn(rb.check_index)
            print(rb.check_index)

    def advance_search_dialog(self):
        print("ADVANCE SEARCH DIALOG")
        dlg = AdvanceSearchDialog(self)
        if dlg.exec_():
            if dlg.id_checkbox.isChecked():
                print(f'id_edit_line values: {dlg.id_edit_line.text()}')
            if dlg.detail_checkbox.isChecked():
                print(f'detail_edit_line values: {dlg.detail_edit_line.text()}')
            if dlg.dod_checkbox.isChecked():
                print(f'dod_edit_line values: {dlg.dod_edit_line.text()}')
            if dlg.f_name_checkbox.isChecked():
                print(f'f_name_edit_line values: {dlg.f_name_edit_line.text()}')
            if dlg.m_name_checkbox.isChecked():
                print(f'm_name_edit_line values: {dlg.m_name_edit_line.text()}')
            if dlg.s_name_checkbox.isChecked():
                print(f's_name_edit_line values: {dlg.s_name_edit_line.text()}')
            if dlg.address_checkbox.isChecked():
                print(f'address_edit_line values: {dlg.address_edit_line.text()}')
        else:
            print("Cancel!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = Viewer()
    viewer.show()
    sys.exit(app.exec_())

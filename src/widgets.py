import sys
from PyQt5.QtWidgets import (
    QDialog, QDialogButtonBox, QLabel,
    QVBoxLayout, QHBoxLayout, QLineEdit,
    QRadioButton, QCheckBox
)
from PyQt5 import QtCore


class AdvanceSearchDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("background: #dce7ff")
        layout = QVBoxLayout()
        id_search_layout = QHBoxLayout()
        detail_search_layout = QHBoxLayout()
        dod_search_layout = QHBoxLayout()
        f_name_search_layout = QHBoxLayout()
        m_name_search_layout = QHBoxLayout()
        s_name_search_layout = QHBoxLayout()
        address_search_layout = QHBoxLayout()
        self.setWindowTitle("Advance search")

        self.id_checkbox = QCheckBox("ID")
        self.id_checkbox.stateChanged.connect(self.id_checkbox_action)
        self.detail_checkbox = QCheckBox("Details")
        self.detail_checkbox.stateChanged.connect(self.detail_checkbox_action)
        self.dod_checkbox = QCheckBox("Date of death")
        self.dod_checkbox.stateChanged.connect(self.dod_checkbox_action)
        self.f_name_checkbox = QCheckBox("First name")
        self.f_name_checkbox.stateChanged.connect(self.f_name_checkbox_action)
        self.m_name_checkbox = QCheckBox("Middle name")
        self.m_name_checkbox.stateChanged.connect(self.m_name_checkbox_action)
        self.s_name_checkbox = QCheckBox("Surname")
        self.s_name_checkbox.stateChanged.connect(self.s_name_checkbox_action)
        self.address_checkbox = QCheckBox("Address")
        self.address_checkbox.stateChanged.connect(self.address_checkbox_action)

        self.id_edit_line = QLineEdit(self)
        self.id_edit_line.setStyleSheet("""QLineEdit{
                                                background-color: #dce7ff;
                                                }""")
        self.id_edit_line.setEnabled(False)
        self.detail_edit_line = QLineEdit(self)
        self.detail_edit_line.setStyleSheet("""QLineEdit{
                                                background-color: #dce7ff;
                                                }""")
        self.detail_edit_line.setEnabled(False)
        self.dod_edit_line = QLineEdit(self)
        self.dod_edit_line.setStyleSheet("""QLineEdit{
                                                background-color: #dce7ff;
                                                }""")
        self.dod_edit_line.setEnabled(False)
        self.f_name_edit_line = QLineEdit(self)
        self.f_name_edit_line.setStyleSheet("""QLineEdit{
                                                background-color: #dce7ff;
                                                }""")
        self.f_name_edit_line.setEnabled(False)
        self.m_name_edit_line = QLineEdit(self)
        self.m_name_edit_line.setStyleSheet("""QLineEdit{
                                                background-color: #dce7ff;
                                                }""")
        self.m_name_edit_line.setEnabled(False)
        self.s_name_edit_line = QLineEdit(self)
        self.s_name_edit_line.setStyleSheet("""QLineEdit{
                                                background-color: #dce7ff;
                                                }""")
        self.s_name_edit_line.setEnabled(False)
        self.address_edit_line = QLineEdit(self)
        self.address_edit_line.setStyleSheet("""QLineEdit{
                                                background-color: #dce7ff;
                                                }""")
        self.address_edit_line.setEnabled(False)

        id_search_layout.addWidget(self.id_checkbox)
        id_search_layout.addWidget(self.id_edit_line)
        detail_search_layout.addWidget(self.detail_checkbox)
        detail_search_layout.addWidget(self.detail_edit_line)
        dod_search_layout.addWidget(self.dod_checkbox)
        dod_search_layout.addWidget(self.dod_edit_line)
        f_name_search_layout.addWidget(self.f_name_checkbox)
        f_name_search_layout.addWidget(self.f_name_edit_line)
        m_name_search_layout.addWidget(self.m_name_checkbox)
        m_name_search_layout.addWidget(self.m_name_edit_line)
        s_name_search_layout.addWidget(self.s_name_checkbox)
        s_name_search_layout.addWidget(self.s_name_edit_line)
        address_search_layout.addWidget(self.address_checkbox)
        address_search_layout.addWidget(self.address_edit_line)

        btns = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        button_box = QDialogButtonBox(btns)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout.addLayout(id_search_layout)
        layout.addLayout(detail_search_layout)
        layout.addLayout(dod_search_layout)
        layout.addLayout(f_name_search_layout)
        layout.addLayout(m_name_search_layout)
        layout.addLayout(s_name_search_layout)
        layout.addLayout(address_search_layout)
        layout.addWidget(button_box)
        self.setLayout(layout)

    def id_checkbox_action(self, state):
        if QtCore.Qt.Checked == state:
            self.id_edit_line.setEnabled(True)
            self.id_edit_line.setStyleSheet("""QLineEdit { background-color: white;}""")
        else:
            self.id_edit_line.setEnabled(False)
            self.id_edit_line.setStyleSheet("""QLineEdit { background-color: #dce7ff;}""")

    def detail_checkbox_action(self, state):
        if QtCore.Qt.Checked == state:
            self.detail_edit_line.setEnabled(True)
            self.detail_edit_line.setStyleSheet("""QLineEdit { background-color: white;}""")
        else:
            self.detail_edit_line.setEnabled(False)
            self.detail_edit_line.setStyleSheet("""QLineEdit { background-color: #dce7ff;}""")

    def dod_checkbox_action(self, state):
        if QtCore.Qt.Checked == state:
            self.dod_edit_line.setEnabled(True)
            self.dod_edit_line.setStyleSheet("""QLineEdit { background-color: white;}""")
        else:
            self.dod_edit_line.setEnabled(False)
            self.dod_edit_line.setStyleSheet("""QLineEdit { background-color: #dce7ff;}""")

    def f_name_checkbox_action(self, state):
        if QtCore.Qt.Checked == state:
            self.f_name_edit_line.setEnabled(True)
            self.f_name_edit_line.setStyleSheet("""QLineEdit { background-color: white;}""")
        else:
            self.f_name_edit_line.setEnabled(False)
            self.f_name_edit_line.setStyleSheet("""QLineEdit { background-color: #dce7ff;}""")

    def m_name_checkbox_action(self, state):
        if QtCore.Qt.Checked == state:
            self.m_name_edit_line.setEnabled(True)
            self.m_name_edit_line.setStyleSheet("""QLineEdit { background-color: white;}""")
        else:
            self.m_name_edit_line.setEnabled(False)
            self.m_name_edit_line.setStyleSheet("""QLineEdit { background-color: #dce7ff;}""")

    def s_name_checkbox_action(self, state):
        if QtCore.Qt.Checked == state:
            self.s_name_edit_line.setEnabled(True)
            self.s_name_edit_line.setStyleSheet("""QLineEdit { background-color: white;}""")
        else:
            self.s_name_edit_line.setEnabled(False)
            self.s_name_edit_line.setStyleSheet("""QLineEdit { background-color: #dce7ff;}""")

    def address_checkbox_action(self, state):
        if QtCore.Qt.Checked == state:
            self.address_edit_line.setEnabled(True)
            self.address_edit_line.setStyleSheet("""QLineEdit { background-color: white;}""")
        else:
            self.address_edit_line.setEnabled(False)
            self.address_edit_line.setStyleSheet("""QLineEdit { background-color: #dce7ff;}""")



import maya.cmds as cmds
import os
import sys


from PySide2 import QtWidgets, QtCore
from name_validator_ui import Ui_Name_Validator
from rename_ui import Ui_Rename
from name_validator_v003 import Name_Validator

class Rename(Name_Validator, Ui_Rename):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.listMaterial = Name_Validator.listMaterial

    def populateList(self):
        self.listMaterial






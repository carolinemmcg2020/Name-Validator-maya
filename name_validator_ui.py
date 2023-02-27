from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from wildchildanimation.gui.swing_utils import fakestr

class Ui_Name_Validator(object):

    def setupUI(self, Name_Validator):
        if not Name_Validator.objectName():
            Name_Validator.setObjectName(u"Name Validator")
        Name_Validator.setWindowModality(Qt.ApplicationModal)
        Name_Validator.resize(680, 460)

        self.verticalLayout_2 = QVBoxLayout(Name_Validator)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.labelGeoSelected = QLabel(Name_Validator)
        self.labelGeoSelected.setObjectName(u"labelGeoSelected")
        self.verticalLayout.addWidget(self.labelGeoSelected)
        
        self.labelMat = QLabel(Name_Validator)
        self.labelMat.setObjectName(u"labelMat")
        self.verticalLayout.addWidget(self.labelMat)

        self.listMaterial = QListWidget()
        self.listMaterial.setObjectName(u"listMaterial")
        self.verticalLayout.addWidget(self.listMaterial)
        self.listMaterial.setSortingEnabled(True)
        self.listMaterial.installEventFilter(self)
        self.listMaterial.sortItems(Qt.SortOrder.AscendingOrder)
        
        QListWidgetItem("S:\productions\sdmp\sdmp_work\\assets\kit\mlegazeboava\\tx\mlegazeboava\\t_MLEGazeboBaseAvA_Concrete_d.1001.png", self.listMaterial)
        QListWidgetItem("S:\productions\sdmp\sdmp_work\\assets\kit\mlegazeboava\\tx\mlegazeboava\\t_MLEGazeboBaseAvA_Concrete_n.1001.png", self.listMaterial)
        QListWidgetItem("S:\productions\sdmp\sdmp_work\\assets\kit\mlegazeboava\\tx\mlegazeboava\\t_MLEGazeboBaseAvA_Concrete_r.1001.png", self.listMaterial)
        QListWidgetItem("S:\productions\sdmp\sdmp_work\\assets\kit\mlegazeboava\\tx\mlegazeboava\\t_MLEGazeboBaseAvA_Poles_d.1001.png", self.listMaterial)
        QListWidgetItem("S:\productions\sdmp\sdmp_work\\assets\kit\mlegazeboava\\tx\mlegazeboava\\t_MLEGazeboBaseAvA_Poles_n.1001.png", self.listMaterial)

        self.labelTexNoMat = QLabel(Name_Validator)
        self.labelTexNoMat.setObjectName(u"labelPreset")
        self.verticalLayout.addWidget(self.labelTexNoMat)

        self.listMatTexIncorrect = QListWidget()
        self.listMatTexIncorrect.setObjectName(u"listMatTexIncorrect")
        self.listMatTexIncorrect.setSortingEnabled(True)
        self.listMatTexIncorrect.sortItems(Qt.SortOrder.AscendingOrder)
        self.listMatTexIncorrect.installEventFilter(self)
        self.verticalLayout.addWidget(self.listMatTexIncorrect)
        QListWidgetItem("mi_MLEPeelingPaintedWoodTilesAvA", self.listMatTexIncorrect)
        QListWidgetItem("mi_MLEPeelingPaintedWoodTilesAvB", self.listMatTexIncorrect)
        QListWidgetItem("mi_MLEPeelingPaintedWoodTilesAvC", self.listMatTexIncorrect)
        QListWidgetItem("SDMP_MainLodgeExt_StorageBuilding_Mo_v15:_ShackFBXASC046RoofFBXASC046001SG4", self.listMatTexIncorrect)
        QListWidgetItem("SDMP_MainLodgeExt_StorageBuilding_Mo_v15:Moss_001", self.listMatTexIncorrect)
        QListWidgetItem("MLEGazeboBaseAvA_Poles", self.listMatTexIncorrect)
        QListWidgetItem("SDMP_MainLodgeExt_StorageBuilding_Mo_v15:SDMP_DoorC_Mo_v01:mi_DoorGreenPaint", self.listMatTexIncorrect)
        
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        
        # This might not be needed but left it here just incase
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.rename_btn = QPushButton()
        self.rename_btn.setObjectName(u"rename_btn")
        self.buttonBox.addButton(self.rename_btn, QDialogButtonBox.ActionRole)
        self.search_btn = QPushButton()
        self.search_btn.setObjectName(u"search_btn")
        self.buttonBox.addButton(self.search_btn, QDialogButtonBox.AcceptRole)
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        
        
        #self.verticalLayout_2.addWidget(self.search_btn)


        self.retranslateUi(Name_Validator)
        self.buttonBox.accepted.connect(Name_Validator.material_checker)
        self.buttonBox.rejected.connect(Name_Validator.reject)

        QMetaObject.connectSlotsByName(Name_Validator)
        
 
    def retranslateUi(self, Name_Validator):
        Name_Validator.setWindowTitle(fakestr(u"Name Validator", None))
        self.labelMat.setText(fakestr(u"Textures without Materials in selection:", None))
        self.labelTexNoMat.setText(fakestr(u"Materials without textures or named incorrectly in selection:", None))
        self.search_btn.setText("Search")
        self.rename_btn.setText("Rename")

    

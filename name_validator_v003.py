#import maya.cmds as cmds
import os
import sys

from PySide2 import QtWidgets, QtCore
from name_validator_ui import Ui_Name_Validator
from rename_ui import Ui_Rename

class Name_Validator(QtWidgets.QDialog, Ui_Name_Validator):

    VERSION = "1.0.4"

    def __init__(self, parent = None):
        super(Name_Validator, self).__init__(None) # Call the inherited classes __init__ method
        self.setupUI(self)
        self.search_btn.clicked.connect(self.material_checker)
        self.rename_btn.clicked.connect(self.rename_on_selection)
      
        #self.listMatTexIncorrect.itemClicked.connect(self.itemClicked)
        #self.listMaterial.itemClicked.connect(self.itemClicked)       

    def eventFilter(self, source, event):
        _contextMenu = QtCore.QEvent.ContextMenu
        menu = QtWidgets.QMenu()
        
        if (event.type() == _contextMenu and source is self.listMatTexIncorrect or event.type() == _contextMenu and source is self.listMaterial):
            menu.addAction('Rename')
            if menu.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
                self.executeRenameDialog()
                Ui_Rename.listMaterial.addItem(item.text())
                print(item.text())
            return True
        return super(Name_Validator, self).eventFilter(source, event)        

    # debugging function
    def itemClicked(self, item):
        print(item.text())

    # function to rename material
    # spllts material name at ':' 
    # concatonates 'mi_' prefix to extracted material name 
    def rename_item(self):
        item = self.listMatTexIncorrect.currentItem()
        #cmds.select(item.text())
        if (item.text().find(":") != -1):
            if(item.text().find("mi_") == -1): 
                extractedMatName= item.text().rsplit(":")[-1]
                mat_prefix = "mi"
                newFileName= mat_prefix + extractedMatName

                #item.editItem(item)
                #cmds.rename()
                print(newFileName)

        else: 
            print("This is not renamed")

    # rename on listwidget selection
    # extracts texture name and material name 
    # compares and if true adds 'mi_' prefix
    def rename_on_selection(self):
        tex_item = self.listMaterial.currentItem()
        
        tex_fname = tex_item.text().rsplit("t_")[-1]
        split_tex_fname = tex_fname.split("_")
        extracted_tex_fname = split_tex_fname[0] + "_" + split_tex_fname[1]

        mat_item = self.listMatTexIncorrect.currentItem()
        mat_index = self.listMatTexIncorrect.currentRow()
        mat_name = mat_item.text().rsplit(":")[-1]
        #cmds.select(mat_item.text())

        if(mat_name.find(extracted_tex_fname) != -1):
            mat_prefix = "mi_"
            newMatFname = mat_prefix + mat_name
            #cmds.rename(newMatFname)
            self.listMatTexIncorrect.takeItem(mat_index)

            self.listMatTexIncorrect.addItem(QtWidgets.QListWidgetItem(newMatFname))
            
            print("This is the renamed material file: " + newMatFname)

        else:
            print("This material does not match the texture selected")

    # function that calls Rename Dialog UI
    def executeRenameDialog(self):
        myDialog = Ui_Rename(self)
        myDialog.setupUI(self)
        myDialog.show()

    # get selected meshes
    def get_meshes():
        selected = []
        meshes = []
        selected = cmds.ls(sl = True, type = 'transform', l = True)

        if len(selected) > 0:
            for sel in selected:
                mesh = cmds.listRelatives( sel, ad=True , type = 'mesh', f = True)
                for m in mesh:
                    meshes.append(m)
        else:
            meshes = cmds.ls(type = 'mesh', l = True)

        return(meshes)

    # function to get list of materials in the scene
    def get_mat(meshes):
        materials = []
        mat_names = []

        # get materials assigned to meshes
        for mesh in meshes:
            
            shade_eng = cmds.listConnections(mesh , type = 'shadingEngine')
            # check if shape has material (rouge shape nodes in the scene not connected to a transform)
            if shade_eng:
                material = cmds.ls(cmds.listConnections(shade_eng ), materials = True)
                materials.append(material)
                
        # get a clean list of material names
        for mat in materials:
            if isinstance(mat, list):
                for m_str in mat:
                    if m_str in mat_names:
                        pass
                    else:
                        mat_names.append(m_str)
            if isinstance(mat, str):
                if mat in mat_names:
                    pass
                else:
                    mat_names.append(m_str)(mat)
                
        return(mat_names)

    # function to get a list of textures in a selected dir.
    def get_texture_files():
        path = cmds.fileDialog2(fileMode = 3, dialogStyle=2, okCaption = 'Select Folder')
        
        #print("This is the selected texture directory: {} \n".format(path))
        if path:
        
            files = []
            # r=root, d=directories, f = files
            for r, d, f in os.walk(path[0]):
                
                for file in f:
                    fn, ext = os.path.splitext(file)
                    #print("Checking Name: {} Ext {}".format(fn, ext))
                    
                    if ext in ['.png', '.jpg', '.exr', '.uasset']:
                        # print("+ {}".format(file))
                        files.append(os.path.join(r, file))
            return(files, path)
        else: 
            
            return  cmds.confirmDialog(title= 'Cancel', message = 'Please select a folder to continue', button = ['OK'])    
        

    # get short texture names    
    def get_texture_names(self, texture_files):
        texture_names = []
        for texture_file in texture_files:
            texture_name = texture_file.split('/')[-1]
            texture_names.append(texture_name)
        return(texture_names)

    # Check if material name starts with mi_
    def check_material_names(mat_names):
        correct_mat_names = []
        incorrect_mat_names = []

        for mat_name in mat_names:
            no_namespace_mat = mat_name.split(":")[-1]
            split_mat_name = no_namespace_mat.split("_")
            if split_mat_name[0] == 'mi':
                correct_mat_names.append(mat_name)
            else:
                incorrect_mat_names.append(mat_name)

        return(correct_mat_names, incorrect_mat_names) 

    # function to check texture names in material list  
    def check_mat_name_against_tex(materials, textures):

        mat_texture_match = []
        mat_match = []
        mat_texture_no_match = []

        for tex in textures:
            texture_check_name = ''
            texture_check_name = Name_Validator.get_texture_name_to_check(tex)

            for mat in materials:
                if texture_check_name:
                    if texture_check_name in mat:
                        mat_texture_match.append(tex)
                        mat_match.append(mat)
                    else:
                        mat_texture_no_match.append(tex)
                        
            
        return(mat_texture_match, mat_texture_no_match, mat_match)

    
    def get_texture_name_to_check(full_texture_path):
        full_texture_name = full_texture_path.split('/')
        name = ''
            
        tex_name = full_texture_name[-1].split('.')[0]
        tex_list = tex_name.split('_')
        if (tex_list[0] == 't'):
            name = tex_name[2:]
            name = name[:-2]
            return(name)
        else:
            return(None)
        

    def reformat_path(texture_files):
        texture_path = []

        for t in texture_files:
           for path in t:
            tex_path = os.path.normpath(path)
            #print(tex_path)
            texture_path.append(tex_path)

        return(texture_path)

    def material_checker(self):        
        meshes = Name_Validator.get_meshes()
        texture_files = Name_Validator.get_texture_files()
        texture_files_reformat = Name_Validator.reformat_path(texture_files)
        materials = Name_Validator.get_mat(meshes)
        checked_material_names = Name_Validator.check_material_names(materials)
        
        # only feed in valid material names to texture check

        matches = Name_Validator.check_mat_name_against_tex(checked_material_names[0], texture_files_reformat)
        no_tex_match = []
        no_mat_match = []
        no_mat_name = checked_material_names[1]

        for texture in texture_files_reformat:

            if texture in matches[0]:
                pass
            else:
                no_tex_match.append(texture)

        for material in materials:
            if material in matches[2]:
                pass
            else:
                no_mat_match.append(material)

        #print('\nMaterials on geo without "mi_" prefix')
        for m in no_mat_name:
            #print(m)
            no_mat_list_item = QtWidgets.QListWidgetItem(m)
            # self.listGeo.addItem(no_mat_list_item)
                
        #print('\nTextures without Materials in selection')
        for n in no_tex_match:
            #print(n)
            no_tex_list_item = QtWidgets.QListWidgetItem(n)
            self.listMaterial.addItem(no_tex_list_item)

        #print('\nMaterials without textures or named incorrectly in selection')
        for mm in no_mat_match:
            #print(mm)
            no_mat_match_list_item = QtWidgets.QListWidgetItem(mm)
            self.listMatTexIncorrect.addItem(no_mat_match_list_item)

    # function to save last used folder
    def save_tex_folder(self):
        self.settings = QtCore.QSettings()
        self.settings.beginGroup(self.__class__.__name__)
        self.settings.value("last_used_folder", os.path.expanduser("~"))

           
if __name__ == '__main__':

    # Name_Validator.material_checker()
    app = QtWidgets.QApplication(sys.argv)

    dialog = Name_Validator()
    ret = dialog.exec_()
    sys.exit(ret)
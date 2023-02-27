#import maya.cmds as cmds
import os

# select all objects
#cmds.selectType(allObjects=True)


# function to get list of materials in the scene
def get_mat():

    # select materials currently in the scene
    list_of_mats = cmds.ls(mat=True)

    # new list for split material names
    ls_mats = [i.rsplit(":")[-1] for i in list_of_mats]
    # removes prefixes
    no_prefx_mats = [i.rsplit("mi_")[-1] for i in ls_mats]

    return no_prefx_mats


# function to get a list of textures in a specified file dir.
def get_tex(file_path="S:/productions/sdmp/sdmp_work/assets/kit/mlegazeboava/tx/mlegazeboava"):

    # list of files in specified directory
    ls_tex = cmds.getFileList(folder= file_path)

    # remove the texture prefix
    no_prefx_tex = [i.rsplit("t_")[-1] for i in ls_tex]

    # remove the file type prefixes 'jpg' 
    ls_name_of_tex = [i.rsplit("_")[0] for i in no_prefx_tex]

    return ls_name_of_tex


# function to check texture names in material list  
def check_naming(no_prefx_mats, ls_name_of_tex):

    # empty list for correct names
    correct_names = []

    # empty list for incorrect names
    incorrect_names = []

    # debugging print statement for material list
    print("material list : " + str(no_prefx_mats))

    # debugging print statement for texture list
    print("texture list : " + str(ls_name_of_tex))

    # iterates based on the length of material list
    for i in range(len(no_prefx_mats)):
        # validator; checks to see if a material name is in the list of textures
        if no_prefx_mats[i] not in ls_name_of_tex:
            # add to list of incorrect names
            incorrect_names.append(no_prefx_mats[i])
        else:
            # add to list of correct names
            correct_names.append(no_prefx_mats[i])

    print(correct_names)
    
    print(incorrect_names)
        
if __name__ == '__main__':
    get_tex()


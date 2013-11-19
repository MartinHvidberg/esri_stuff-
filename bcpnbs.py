import os, arcpy
 
def inventory_data(workspace, datatypes):
    for path, path_names, data_names in arcpy.da.Walk(workspace, datatype=datatypes):
        for data_name in data_names:
            yield os.path.join(path, data_name)

def match_feature_names(FA,lstFB):
    FAName = FA[FA.rfind("\\")+1:]
    for FB in lstFB:
        if FAName in FB:
            return FB
    return False

#Main
genWSA = inventory_data(r"C:\data\input.gdb", "FeatureClass")
lstWSA = list(genWSA)
genWSB = inventory_data(r"C:\data\output.gdb", "FeatureClass")
lstWSB = list(genWSB)

for FCA in lstWSA:
    print "Copying:"+FCA
    lst_field_names = [fldX.name for fldX in arcpy.ListFields(FCA)]
    curWrite = arcpy.da.InsertCursor(match_feature_names(FCA,lstWSB),lst_field_names)
    with arcpy.da.SearchCursor(FCA,"*") as curRead:
        for row in curRead:
            curWrite.insertRow(row)
    del curRead,curWrite

import arcpy
import ecarc

def match_feature_names(FA,lstFB):
    FAName = FA[FA.rfind("\\")+1:]
    for FB in lstFB:
        if FAName in FB:
            return FB
    return False

def two_fcs_to_numpy(fclA,fclB):
    
    def fcs_to_numpy(fclX):
        lstXFields = arcpy.ListFields(fclX)
        lstFldnames = list()
        for fldx in lstXFields:
            print "fff:",fldx.baseName,fldx.type,
            if (fldx.type in ["Date","Geometry","geometry","raster","BLOB"]) or (fldx.baseName in ["SCAMIN","SCAMAX"]):
                print "   <--- SKIPPED"
            else:
                lstFldnames.append(str(fldx.baseName))
                print
        print str(type(fclX)),fclX
        print str(type(lstFldnames)),lstFldnames
        npaX = arcpy.da.FeatureClassToNumPyArray(fclX,lstFldnames) # <--- Can't handle it ...
        print "nap?",str(type(npaX))
        
    return (fcs_to_numpy(fclA),fcs_to_numpy(fclB))
    

def fcComp(fcA, fcB, fldL):
    
    def list_relevant_fieldnames(fcX):    
        #print "LR",fcX
        lstXFields = arcpy.ListFields(fcX)
        lstFldnames = list()
        for fldx in lstXFields:
            #print "fff:",fldx.baseName,fldx.type,
            if (fldx.type in ["Date","Geometry","raster","BLOB"]) or (fldx.baseName in ["OBJECTID","GLOBALID","LNAM","NOID","NIS_VERIFIED","NIS_VERIFIER"]):
                #print "   <--- SKIPPED"
                pass
            else:
                lstFldnames.append(str(fldx.baseName))
                #print
        return lstFldnames
    
    def report_differences(index,tupA,tupB,lrfC):
        for numI in range(len(tupA)):
            if tupA[numI] != tupB[numI]:
                print " !!! "+str(index)+" > "+str(lrfC[numI])+" > "+str(tupA[numI])+" != "+str(tupB[numI])
    
    lrfA = list_relevant_fieldnames(fcA)
    lrfB = list_relevant_fieldnames(fcB)
    
    # Work with index, incl geo-key
    if fldL.lower() == "geo":
        # Add Geo.key
        print "INDEX = geo-key"
        numIndexFld = -1
    else:
        if (fldL in lrfA) and (fldL in lrfB):
            # slim list of fields to common fields
            lrfC = list()
            for fA in lrfA:
                if fA in lrfB:
                    lrfC.append(fA)
            if (len(lrfC) == len(lrfA)) and (len(lrfC) == len(lrfB)):
                numIndexFld = lrfC.index(fldL)
                print "INDEX =",numIndexFld,"=",lrfC[numIndexFld]                
            else:
                print "Error : Non identical list of relevant fields... :", fcA, fcB
    
    # Work on ...       
    dicA = dict()
    dicB = dict()
    with arcpy.da.SearchCursor(fcA,lrfC) as cursorA:
        for rowA in cursorA:
            if rowA[numIndexFld] != None:
                dicA[rowA[numIndexFld]] = rowA
            else:
                print "<Null> is not a good key : "+str(rowA[numIndexFld])
    del rowA, cursorA
    with arcpy.da.SearchCursor(fcB,lrfC) as cursorB:
        for rowB in cursorB:
            if rowB[numIndexFld] != None:
                if rowB[numIndexFld] in dicA.keys():
                    dicB[rowB[numIndexFld]] = rowB
                else:
                    print "Key found in B that was not in A:"+str(rowB[numIndexFld])
            else:
                print "<Null> is still not a good key : "+str(rowB[numIndexFld])                    
    del rowB, cursorB
    
    # Now measure the two dics against each other...
    for indexC in dicB.keys():
        if dicA[indexC] != dicB[indexC]:
            report_differences(dicA[indexC][numIndexFld],dicA[indexC],dicB[indexC],lrfC)
    
    return 0

def showme(featureclass):
    print featureclass
 
genFeatA = ecarc.inventory_data(r"C:\Martin\NIScopy140830.gdb", "FeatureClass")
lstFcA = list(genFeatA)
genFeatB = ecarc.inventory_data(r"C:\Martin\NIScopy.gdb", "FeatureClass")
lstFcB = list(genFeatB)

for fcA in lstFcA:
    fcB = match_feature_names(fcA,lstFcB)
    print fcA, fcB
    if "DangersA" in fcA:
        #objX = two_fcs_to_numpy(fcA,fcB)
        print "Comparing (",fcA,",",fcB,")"
        objX = fcComp(fcA,fcB,"NAME")
        showme(objX)

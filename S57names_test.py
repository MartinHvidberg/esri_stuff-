import S57names

for strFC in ["AidsToNavigationP","XXXxxx",u'"AidsToNavigationP"']:
    print strFC, S57names.FCexists(strFC)

print "\nList of FCs:"
for t in S57names.ListofFCs(["Ice","Routes"]):
    print t


print "\nList of SFCs:"
for t in S57names.ListofSFCs():
    print t, ":", S57names.FCSFC2ABB(t[0],t[1]),":", S57names.FCSFC2Name(t[0],t[1])

#===============================================================================
# FC = "MilitaryFeaturesP"    
# print "\nList SFCs in "+FC
# for t in S57names.ListofSFCsInFC(FC,[]):
#     print t
# print " Only '30'"
# for t in S57names.ListofSFCsInFC(FC,["30"]):
#     print t
#===============================================================================

#===============================================================================
# print "\nCase:"
# FC = "RegulatedAreasAndLimitsL"
# SFC = "1"
# print "> FC :",FC
# print "> SFC:",SFC
# print "< ABB:",S57names.FCSFC2ABB(FC,SFC)
# print "< Nam:",S57names.FCSFC2Name(FC,SFC)
# 
# print "\nCase:"
# ABB = "TOPMAR"
# print "Find SFC for ",ABB
# for i in S57names.S57ABB2FSC(ABB):
#    print i 
# 
# print "\nCase:"
# ABB = "WATTUR"
# print "Find SFC for ",ABB
# for i in S57names.S57ABB2FSC(ABB):
#    print i
#===============================================================================





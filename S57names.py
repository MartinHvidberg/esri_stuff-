
"""Operations used to convert between S-57 abbreviations and -names, vs. Esri NIS Feature types, and sub-type numbers"""

# *** XXX To Do: Consider adding list of use ["ECN","AML", etc.]
        
lstFCSFC = [
        ["AidsToNavigationP","1","BCNCAR","Beacon Cardinal"],
        ["AidsToNavigationP","5","BCNISD","Beacon Isolated Danger"],
        ["AidsToNavigationP","10","BCNLAT","Beacon Lateral"],
        ["AidsToNavigationP","15","BCNSAW","Beacon Safe Water"],
        ["AidsToNavigationP","20","BCNSPP","Beacon Special Purpose"],
        ["AidsToNavigationP","25","BOYCAR","Buoy Cardinal"],
        ["AidsToNavigationP","30","BOYINB","Buoy Installation"],
        ["AidsToNavigationP","35","BOYISD","Buoy Isolated Danger"],
        ["AidsToNavigationP","40","BOYLAT","Buoy Lateral"],
        ["AidsToNavigationP","45","BOYSAW","Buoy Safe Water"],
        ["AidsToNavigationP","50","BOYSPP","Buoy Special Purpose"],
        ["AidsToNavigationP","55","DAYMAR","Day Mark"],
        ["AidsToNavigationP","60","FOGSIG","Fog Signal"],
        ["AidsToNavigationP","65","LIGHTS","Light"],
        ["AidsToNavigationP","70","LITFLT","Light Float"],
        ["AidsToNavigationP","75","LITVES","Light Vessel"],
        ["AidsToNavigationP","80","navaid","Navigational Aid"],
        ["AidsToNavigationP","85","RADRFL","Radar Reflector"],
        ["AidsToNavigationP","90","RADSTA","Radar Station"],
        ["AidsToNavigationP","95","RDOSTA","Radio Station"],
        ["AidsToNavigationP","100","RETRFL","Retro Reflector"],
        ["AidsToNavigationP","105","RTPBCN","Radar Transponder Beacon"],
        ["AidsToNavigationP","110","TOPMAR","Topmark"],
        ["AidsToNavigationP","115","turnpt","Turning Point"],
        ["CoastlineA","1","SLCONS","Shoreline Construction"],
        ["CoastlineL","1","COALNE","Coastline"],
        ["CoastlineL","5","SLCONS","Shoreline Construction"],
        ["CoastlineP","1","SLCONS","Shoreline Construction"],
        ["CulturalFeaturesA","1","AIRARE","Airport Area"],
        ["CulturalFeaturesA","5","BRIDGE","Bridge"],
        ["CulturalFeaturesA","10","BUAARE","Built Up Area"],
        ["CulturalFeaturesA","15","BUISGL","Building Single"],
        ["CulturalFeaturesA","20","CONVYR","Conveyor"],
        ["CulturalFeaturesA","25","DAMCON","Dam"],
        ["CulturalFeaturesA","30","FORSTC","Fortified Structure"],
        ["CulturalFeaturesA","35","LNDMRK","Landmark"],
        ["CulturalFeaturesA","40","PRDARE","Production Storage Area"],
        ["CulturalFeaturesA","45","PYLONS","Pylon Bridge Support"],
        ["CulturalFeaturesA","50","ROADWY","Road"],
        ["CulturalFeaturesA","55","RUNWAY","Runway"],
        ["CulturalFeaturesA","60","SILTNK","Silo Tank"],
        ["CulturalFeaturesA","65","TUNNEL","Tunnel"],
        ["CulturalFeaturesL","1","BRIDGE","Bridge"],
        ["CulturalFeaturesL","5","CBLOHD","Cable Overhead"],
        ["CulturalFeaturesL","10","CONVYR","Conveyor"],
        ["CulturalFeaturesL","15","DAMCON","Dam"],
        ["CulturalFeaturesL","20","FNCLNE","Fence Wall"],
        ["CulturalFeaturesL","25","FORSTC","Fortified Structure"],
        ["CulturalFeaturesL","30","LNDMRK","Landmark"],
        ["CulturalFeaturesL","35","PIPOHD","Pipeline Overhead"],
        ["CulturalFeaturesL","40","RAILWY","Railway"],
        ["CulturalFeaturesL","45","ROADWY","Road"],
        ["CulturalFeaturesL","50","RUNWAY","Runway"],
        ["CulturalFeaturesL","55","TUNNEL","Tunnel"],
        ["CulturalFeaturesP","1","AIRARE","Airport Area"],
        ["CulturalFeaturesP","5","BRIDGE","Bridge"],
        ["CulturalFeaturesP","10","BUAARE","Built Up Area"],
        ["CulturalFeaturesP","15","BUISGL","Building Single"],
        ["CulturalFeaturesP","20","CTRPNT","Control Point"],
        ["CulturalFeaturesP","25","DAMCON","Dam"],
        ["CulturalFeaturesP","30","FORSTC","Fortified Structure"],
        ["CulturalFeaturesP","35","LNDMRK","Landmark"],
        ["CulturalFeaturesP","40","PRDARE","Production Storage Area"],
        ["CulturalFeaturesP","45","PYLONS","Pylon Bridge Support"],
        ["CulturalFeaturesP","50","ROADWY","Road"],
        ["CulturalFeaturesP","55","RUNWAY","Runway"],
        ["CulturalFeaturesP","60","SILTNK","Silo Tank"],
        ["CulturalFeaturesP","65","TUNNEL","Tunnel"],
        ["DangersA","1","CTNARE","Caution Area"],
        ["DangersA","5","divloc","Diving Location"],
        ["DangersA","10","FSHFAC","Fishing Facility"],
        ["DangersA","15","OBSTRN","Obstruction"],
        ["DangersA","20","WATTUR","Water Turbulence"],
        ["DangersA","25","WRECKS","Wrecks"],
        ["DangersL","1","FSHFAC","Fishing Facility"],
        ["DangersL","5","OBSTRN","Obstruction"],
        ["DangersL","10","OILBAR","Oil Barrier"],
        ["DangersL","15","WATTUR","Water Turbulence"],
        ["DangersP","1","CTNARE","Caution Area"],
        ["DangersP","5","divloc","Diving Location"],
        ["DangersP","10","FSHFAC","Fishing Facility"],
        ["DangersP","15","histob","Contact History"],
        ["DangersP","20","OBSTRN","Obstruction"],
        ["DangersP","25","senanm","Sensor Anomaly"],
        ["DangersP","30","smalbo","Small Bottom Objects"],
        ["DangersP","35","UWTROC","Underwater Awash Rock"],
        ["DangersP","40","WATTUR","Water Turbulence"],
        ["DangersP","45","WRECKS","Wrecks"],
        ["DepthsA","1","DEPARE","Depth Area"],
        ["DepthsA","5","DRGARE","Dredged Area"],
        ["DepthsA","10","SWPARE","Swept Area"],
        ["DepthsA","15","UNSARE","Unsurveyed Area"],
        ["DepthsL","1","DEPARE","Depth Area"],
        ["DepthsL","5","DEPCNT","Depth Contour"],
        ["IceFeaturesA","1","brgare","Iceberg Area"],
        ["IceFeaturesA","5","iceadv","Ice Advisory Area"],
        ["IceFeaturesA","15","ICEARE","Ice Area"],
        ["IceFeaturesA","20","icebrg","Iceberg"],
        ["IceFeaturesA","25","icelea","Ice Lead"],
        ["IceFeaturesA","30","icemov","Ice Movement"],
        ["IceFeaturesA","35","icepol","Ice Polynya"],
        ["IceFeaturesA","40","lndice","Land Ice"],
        ["IceFeaturesA","45","seaice","Sea Ice"],
        ["IceFeaturesL","1","icelea","Ice Lead"],
        ["IceFeaturesL","5","icelin","Ice Line"],
        ["IceFeaturesL","10","icerte","Ice Route"],
        ["IceFeaturesP","1","icebrg","Iceberg"],
        ["IceFeaturesP","5","icemov","Ice Movement"],
        ["MetaDataA","1","M_ACCY","Accuracy of Data"],
        ["MetaDataA","5","m_clas","Security Classification Information"],
        ["MetaDataA","10","m_conf","Completeness for the product specification"],
        ["MetaDataA","15","M_COVR","Coverage"],
        ["MetaDataA","20","M_CSCL","Compilation Scale of Data"],
        ["MetaDataA","25","M_HOPA","Horizontal Datum Shift Parameters"],
        ["MetaDataA","30","M_NPUB","Nautical Publication Information"],
        ["MetaDataA","35","M_NSYS","Navigational System of Marks"],
        ["MetaDataA","40","M_QUAL","Quality of Data"],
        ["MetaDataA","45","M_SDAT","Sounding Datum"],
        ["MetaDataA","50","M_SREL","Survey Reliability"],
        ["MetaDataA","55","M_VDAT","Vertical Datum of Data"],
        ["MetaDataA","65","M_UNIT","Unit of Measure"],
        ["MetaDataL","1","m_line","Defined Straight Lines"],
        ["MetaDataL","5","M_SREL","Survey Reliability"],
        ["MetaDataP","1","M_NPUB","Nautical Publication Information"],
        ["MetaDataP","60","m_vers","Vertical Datum Shift Area"],
        ["MilitaryFeaturesA","1","airres","Airspace Restriction"],
        ["MilitaryFeaturesA","5","btdare","Bottom Tactical Data Area"],
        ["MilitaryFeaturesA","10","lndstp","Landing Strip"],
        ["MilitaryFeaturesA","15","ctlasp ","Controlled Airspace"],
        ["MilitaryFeaturesA","20","drpzne","Drop Zone"],
        ["MilitaryFeaturesA","25","imgare","Area of Imagery Coverage"],
        ["MilitaryFeaturesA","30","lndste","Landing Site"],
        ["MilitaryFeaturesA","35","lndzne","Landing Zone"],
        ["MilitaryFeaturesA","40","lndare","Landing Area"],
        ["MilitaryFeaturesA","45","marman","Marine Management Area"],
        ["MilitaryFeaturesA","50","mcmare","MCM Area"],
        ["MilitaryFeaturesA","55","mexasp","Military Exercise Airspace"],
        ["MilitaryFeaturesA","60","MIPARE","Military Practice Area"],
        ["MilitaryFeaturesA","65","patare","Patrol Area"],
        ["MilitaryFeaturesA","70","pfdare","Performance Data Area"],
        ["MilitaryFeaturesA","75","resloc","Resource Location"],
        ["MilitaryFeaturesA","80","rkdare","Risk Data Area"],
        ["MilitaryFeaturesA","85","trfare","Trafficability Area"],
        ["MilitaryFeaturesL","1","atsctl","ATS Route Centerline"],
        ["MilitaryFeaturesL","5","bchext","Beach Exit"],
        ["MilitaryFeaturesL","10","ctlasp ","Controlled Airspace"],
        ["MilitaryFeaturesL","15","qroute","Q-Route Leg"],
        ["MilitaryFeaturesP","1","bchext","Beach Exit"],
        ["MilitaryFeaturesP","5","drpzne","Drop Zone"],
        ["MilitaryFeaturesP","10","lndplc","Landing Place"],
        ["MilitaryFeaturesP","15","lndpnt","Landing Point"],
        ["MilitaryFeaturesP","30","MIPARE","Military Practice Area"],
        ["MilitaryFeaturesP","35","resloc","Resource Location"],
        ["MilitaryFeaturesP","40","shlloc","Shelter Location"],
        ["MilitaryFeaturesP","45","viewpt","Viewpoint"],
        ["NaturalFeaturesA","1","LAKARE","Lake"],
        ["NaturalFeaturesA","5","LNDARE","Land Area"],
        ["NaturalFeaturesA","10","LNDRGN","Land Region"],
        ["NaturalFeaturesA","15","RAPIDS","Rapids"],
        ["NaturalFeaturesA","20","RIVERS","River"],
        ["NaturalFeaturesA","25","SEAARE","Sea Area Named Water"],
        ["NaturalFeaturesA","30","SLOGRD","Sloping Ground"],
        ["NaturalFeaturesA","35","VEGATN","Vegetation"],
        ["NaturalFeaturesL","1","LNDARE","Land Area"],
        ["NaturalFeaturesL","5","LNDELV","Land Elevation"],
        ["NaturalFeaturesL","10","RAPIDS","Rapids"],
        ["NaturalFeaturesL","15","RIVERS","River"],
        ["NaturalFeaturesL","20","SLOTOP","Slope Topline"],
        ["NaturalFeaturesL","25","VEGATN","Vegetation"],
        ["NaturalFeaturesL","30","WATFAL","Waterfall"],
        ["NaturalFeaturesP","1","LNDARE","Land Area"],
        ["NaturalFeaturesP","5","LNDELV","Land Elevation"],
        ["NaturalFeaturesP","10","LNDRGN","Land Region"],
        ["NaturalFeaturesP","15","RAPIDS","Rapids"],
        ["NaturalFeaturesP","20","SEAARE","Sea Area Named Water"],
        ["NaturalFeaturesP","25","SLOGRD","Sloping Ground"],
        ["NaturalFeaturesP","30","VEGATN","Vegetation"],
        ["NaturalFeaturesP","35","WATFAL","Waterfall"],
        ["OffshoreInstallationsA","1","CBLARE","Cable Area"],
        ["OffshoreInstallationsA","5","OFSPLF","Offshore Platform"],
        ["OffshoreInstallationsA","10","OSPARE","Offshore Production Area"],
        ["OffshoreInstallationsA","15","PIPARE","Pipeline Area"],
        ["OffshoreInstallationsL","1","CBLSUB","Cable Submarine"],
        ["OffshoreInstallationsL","5","PIPSOL","Pipeline Submarine On Land"],
        ["OffshoreInstallationsP","1","OFSPLF","Offshore Platform"],
        ["OffshoreInstallationsP","5","PIPARE","Pipeline Area"],
        ["OffshoreInstallationsP","10","PIPSOL","Pipeline Submarine On Land"],
        ["PLTS_COLLECTIONS","1","C_AGGR","Aggregation"],
        ["PLTS_COLLECTIONS","5","C_ASSO","Association"],
        ["PortsAndServicesA","1","BERTHS","Berth"],
        ["PortsAndServicesA","5","CANALS","Canal"],
        ["PortsAndServicesA","10","CAUSWY","Causeway"],
        ["PortsAndServicesA","15","CHKPNT","Check Point"],
        ["PortsAndServicesA","20","CRANES","Cranes"],
        ["PortsAndServicesA","25","DOCARE","Dock Area"],
        ["PortsAndServicesA","30","DRYDOC","Dry Dock"],
        ["PortsAndServicesA","35","DYKCON","Dyke"],
        ["PortsAndServicesA","40","FLODOC","Floating Dock"],
        ["PortsAndServicesA","45","GATCON","Gate"],
        ["PortsAndServicesA","50","GRIDRN","Gridiron"],
        ["PortsAndServicesA","55","HRBFAC","Harbour Facility"],
        ["PortsAndServicesA","60","HULKES","Hulkes"],
        ["PortsAndServicesA","65","LOKBSN","Lock Basin"],
        ["PortsAndServicesA","70","MORFAC","Mooring Warping Facility"],
        ["PortsAndServicesA","75","PILBOP","Pilot Boarding Place"],
        ["PortsAndServicesA","80","PONTON","Pontoon"],
        ["PortsAndServicesA","85","SMCFAC","Small Craft Facility"],
        ["PortsAndServicesL","1","BERTHS","Berth"],
        ["PortsAndServicesL","5","CANALS","Canal"],
        ["PortsAndServicesL","10","CAUSWY","Causeway"],
        ["PortsAndServicesL","15","DYKCON","Dyke"],
        ["PortsAndServicesL","20","FLODOC","Floating Dock"],
        ["PortsAndServicesL","25","GATCON","Gate"],
        ["PortsAndServicesL","30","MORFAC","Mooring Warping Facility"],
        ["PortsAndServicesL","35","PONTON","Pontoon"],
        ["PortsAndServicesP","1","BERTHS","Berth"],
        ["PortsAndServicesP","5","CGUSTA","Coast Guard Station"],
        ["PortsAndServicesP","10","CHKPNT","Check Point"],
        ["PortsAndServicesP","15","CRANES","Cranes"],
        ["PortsAndServicesP","20","DISMAR","Distance Mark"],
        ["PortsAndServicesP","25","GATCON","Gate"],
        ["PortsAndServicesP","30","GRIDRN","Gridiron"],
        ["PortsAndServicesP","35","HRBFAC","Harbour Facility"],
        ["PortsAndServicesP","40","HULKES","Hulkes"],
        ["PortsAndServicesP","45","MORFAC","Mooring Warping Facility"],
        ["PortsAndServicesP","50","PILBOP","Pilot Boarding Place"],
        ["PortsAndServicesP","55","PILPNT","Pile"],
        ["PortsAndServicesP","60","RSCSTA","Rescue Station"],
        ["PortsAndServicesP","65","SISTAT","Signal Station Traffic"],
        ["PortsAndServicesP","70","SISTAW","Signal Station Warning"],
        ["PortsAndServicesP","75","SMCFAC","Small Craft Facility"],
        ["RegulatedAreasAndLimitsA","1","ACHARE","Anchorage Area"],
        ["RegulatedAreasAndLimitsA","5","ACHBRT","Anchor Berth"],
        ["RegulatedAreasAndLimitsA","5","CONZNE","Contiguous Zone"],
        ["RegulatedAreasAndLimitsA","10","ADMARE","Administration Area Named"],
        ["RegulatedAreasAndLimitsA","15","ARCSLN","Archipelagic Sea Lane"],
        ["RegulatedAreasAndLimitsA","25","COSARE","Continental Shelf Area"],
        ["RegulatedAreasAndLimitsA","30","CTSARE","Cargo Transhipment Area"],
        ["RegulatedAreasAndLimitsA","35","CUSZNE","Custom Zone"],
        ["RegulatedAreasAndLimitsA","40","DMPGRD","Dumping Ground"],
        ["RegulatedAreasAndLimitsA","45","envare","Environmentally Sensitive Area"],
        ["RegulatedAreasAndLimitsA","50","EXEZNE","Exclusive Economic Zone"],
        ["RegulatedAreasAndLimitsA","55","FRPARE","Free Port Area"],
        ["RegulatedAreasAndLimitsA","60","FSHGRD","Fishing Ground"],
        ["RegulatedAreasAndLimitsA","65","FSHZNE","Fishery Zone"],
        ["RegulatedAreasAndLimitsA","70","HRBARE","Harbour Area Administrative"],
        ["RegulatedAreasAndLimitsA","75","ICNARE","Incineration Area"],
        ["RegulatedAreasAndLimitsA","80","intwtr","Internal Waters Area"],
        ["RegulatedAreasAndLimitsA","85","LOGPON","Log Pond"],
        ["RegulatedAreasAndLimitsA","90","lsrare","Leisure Activity Area"],
        ["RegulatedAreasAndLimitsA","95","MARCUL","Marine Farm Culture"],
        ["RegulatedAreasAndLimitsA","100","msiare","Maritime Safety Information Area"],
        ["RegulatedAreasAndLimitsA","105","RESARE","Restricted Area"],
        ["RegulatedAreasAndLimitsA","110","SPLARE","Sea Plane Landing Area"],
        ["RegulatedAreasAndLimitsA","115","TESARE","Territorial Sea Area"],
        ["RegulatedAreasAndLimitsL","1","ASLXIS","Archipelagic Sea Lane Axis"],
        ["RegulatedAreasAndLimitsL","25","MARCUL","Marine Farm Culture"],
        ["RegulatedAreasAndLimitsL","30","STSLNE","Straight Territorial Sea Baseline"],
        ["RegulatedAreasAndLimitsL","35","TESARE","Territorial Sea Area"],
        ["RegulatedAreasAndLimitsP","1","ACHARE","Anchorage Area"],
        ["RegulatedAreasAndLimitsP","5","ACHBRT","Anchor Berth"],
        ["RegulatedAreasAndLimitsP","10","CTSARE","Cargo Transhipment Area"],
        ["RegulatedAreasAndLimitsP","15","DMPGRD","Dumping Ground"],
        ["RegulatedAreasAndLimitsP","20","envare","Environmentally Sensitive Area"],
        ["RegulatedAreasAndLimitsP","25","ICNARE","Incineration Area"],
        ["RegulatedAreasAndLimitsP","30","LOGPON","Log Pond"],
        ["RegulatedAreasAndLimitsP","35","MARCUL","Marine Farm Culture"],
        ["RegulatedAreasAndLimitsP","45","SPLARE","Sea Plane Landing Area"],
        ["SeabedA","5","botmft","Bottom Feature"],
        ["SeabedL","5","botmft","Bottom Feature"],
        ["SeabedP","5","botmft","Bottom Feature"],
        ["SeabedA","1","bchare","Beach Survey"],
        ["SeabedA","10","bprare","Burial Probability Area"],
        ["SeabedA","15","SBDARE","Seabed Area"],
        ["SeabedA","20","sedlay","Geological Layer"],
        ["SeabedA","25","seiare","Seismic Activity Area"],
        ["SeabedA","30","SNDWAV","Sand Waves"],
        ["SeabedA","35","twlscr","Trawl Scour"],
        ["SeabedA","40","WEDKLP","Weed Kelp"],
        ["SeabedL","1","bchprf","Beach Profile"],
        ["SeabedL","10","SBDARE","Seabed Area"],
        ["SeabedL","15","SNDWAV","Sand Waves"],
        ["SeabedL","20","twlscr","Trawl Scour"],
        ["SeabedP","1","bchare","Beach Survey"],
        ["SeabedP","10","iscour","Impact Scour"],
        ["SeabedP","15","SBDARE","Seabed Area"],
        ["SeabedP","20","sedlay","Geological Layer"],
        ["SeabedP","25","SNDWAV","Sand Waves"],
        ["SeabedP","30","SPRING","Spring"],
        ["SeabedP","35","WEDKLP","Weed Kelp"],
        ["SoundingsP","1","SOUNDG","Soundings"],
        ["TidesAndVariationsA","5","LOCMAG","Local Magnetic Anomaly"],
        ["TidesAndVariationsA","10","MAGVAR","Magnetic Variation"],
        ["TidesAndVariationsA","15","T_HMON","Tide Harmonic Prediction"],
        ["TidesAndVariationsA","20","T_NHMN","Tide Non-Harmonic Prediction"],
        ["TidesAndVariationsA","25","T_TIMS","Tide Time Series"],
        ["TidesAndVariationsA","30","TIDEWY","Tideway"],
        ["TidesAndVariationsA","35","TS_FEB","Tidal Stream Flood Ebb"],
        ["TidesAndVariationsA","40","TS_PAD","Tidal Stream Panel Data"],
        ["TidesAndVariationsA","45","TS_PNH","Tidal Stream Non-Harmonic Prediction"],
        ["TidesAndVariationsA","50","TS_PRH","Tidal Stream Harmonic Prediction"],
        ["TidesAndVariationsA","55","TS_TIS","Tidal Stream Time Series"],
        ["TidesAndVariationsL","5","LOCMAG","Local Magnetic Anomaly"],
        ["TidesAndVariationsL","10","MAGVAR","Magnetic Variation"],
        ["TidesAndVariationsL","15","TIDEWY","Tideway"],
        ["TidesAndVariationsP","1","CURENT","Current Non-Gravitational"],
        ["TidesAndVariationsP","5","LOCMAG","Local Magnetic Anomaly"],
        ["TidesAndVariationsP","10","MAGVAR","Magnetic Variation"],
        ["TidesAndVariationsP","15","T_HMON","Tide Harmonic Prediction"],
        ["TidesAndVariationsP","20","T_NHMN","Tide Non-Harmonic Prediction"],
        ["TidesAndVariationsP","25","T_TIMS","Tide Time Series"],
        ["TidesAndVariationsP","30","TS_FEB","Tidal Stream Flood Ebb"],
        ["TidesAndVariationsP","35","TS_PAD","Tidal Stream Panel Data"],
        ["TidesAndVariationsP","40","TS_PNH","Tidal Stream Non-Harmonic Prediction"],
        ["TidesAndVariationsP","45","TS_PRH","Tidal Stream Harmonic Prediction"],
        ["TidesAndVariationsP","50","TS_TIS","Tidal Stream Time Series"],
        ["TracksAndRoutesA","1","DWRTPT","Deep Water Route Part"],
        ["TracksAndRoutesA","5","FAIRWY","Fairway"],
        ["TracksAndRoutesA","10","FERYRT","Ferry Route"],
        ["TracksAndRoutesA","15","ISTZNE","Inshore Traffic Zone"],
        ["TracksAndRoutesA","20","PRCARE","Precautionary Area"],
        ["TracksAndRoutesA","25","RADRNG","Radar Range"],
        ["TracksAndRoutesA","30","RCTLPT","Recommended Traffic Lane Part"],
        ["TracksAndRoutesA","35","rdoare","Radio Broadcast Area"],
        ["TracksAndRoutesA","40","RECTRC","Recommended Track"],
        ["TracksAndRoutesA","45","SUBTLN","Submarine Transit Lane"],
        ["TracksAndRoutesA","50","TSEZNE","Traffic Separation Zone"],
        ["TracksAndRoutesA","55","TSSCRS","Traffic Separation Scheme Crossing"],
        ["TracksAndRoutesA","60","TSSLPT","Traffic Separation Scheme Lane Part"],
        ["TracksAndRoutesA","65","TSSRON","Traffic Separation Scheme Roundabout"],
        ["TracksAndRoutesA","70","TWRTPT","Two Way Route"],
        ["TracksAndRoutesL","1","DWRTCL","Deep Water Route Centerline"],
        ["TracksAndRoutesL","5","FERYRT","Ferry Route"],
        ["TracksAndRoutesL","10","NAVLNE","Navigation Line"],
        ["TracksAndRoutesL","15","RADLNE","Radar Line"],
        ["TracksAndRoutesL","20","RCRTCL","Recommended Route Centerline"],
        ["TracksAndRoutesL","25","RDOCAL","Radio Calling In Point"],
        ["TracksAndRoutesL","30","RECTRC","Recommended Track"],
        ["TracksAndRoutesL","35","tfcrte","Traffic Route"],
        ["TracksAndRoutesL","40","TSELNE","Traffic Separation Line"],
        ["TracksAndRoutesL","45","TSSBND","Traffic Separation Scheme Boundary"],
        ["TracksAndRoutesP","1","PRCARE","Precautionary Area"],
        ["TracksAndRoutesP","5","RCTLPT","Recommended Traffic Lane Part"],
        ["TracksAndRoutesP","10","RDOCAL","Radio Calling In Point"],
        ["UserDefinedFeaturesA","1","NEWOBJ","New Object"],
        ["UserDefinedFeaturesA","5","u_defd","User Defined"],
        ["UserDefinedFeaturesL","1","NEWOBJ","New Object"],
        ["UserDefinedFeaturesL","5","u_defd","User Defined"],
        ["UserDefinedFeaturesP","1","NEWOBJ","New Object"],
        ["UserDefinedFeaturesP","5","u_defd","User Defined"]
        ]

def CleanSFCstring(strSFC):
    try:
        return str(int(strSFC))
    except:
        return "-1"
    
def FCexists(strFC):
    for i in lstFCSFC:
        if strFC == i[0]:
            return True
    return False
    
def ListofFCs(lstKeywords):
    """List of all known Feature classes
    If arguments given, must be list of strings, 
    then only return layers where one or more of 
    these strings can be found in Feature Cass name.
    Returns list of FCs"""
    
    lstR = []
    
    def ListAdd(lstN,strN):
        if not strN in lstN:
            lstN.append(strN)
        return lstN
    
    for i in lstFCSFC:
        if len(lstKeywords)>0:
            for k in lstKeywords:
                if k in i[0]:
                    lstR = ListAdd(lstR,i[0])
        else:
            lstR = ListAdd(lstR,i[0])
    return lstR
    
def ListofSFCs():
    lstR = []
    for i in lstFCSFC:
        lstSFC = [i[0],i[1]]
        if not lstSFC in lstR:
            lstR.append(lstSFC)
    #lstR.sort() # cant handle text and number combination, ant they were in the right order from the start...
    return lstR

def ListofSFCsInFC(FC,lstKeywords):
    lstR = []
    for i in lstFCSFC:
        if i[0]==FC:
            if len(lstKeywords)>0:
                for k in lstKeywords:
                    if k == i[1]:
                        lstR.append(i)
            else:
                lstR.append(i)            
    return lstR

def FCSFC2ABB(strFC,strSFC):
    if CleanSFCstring(strSFC)!="-1":
        for i in lstFCSFC:
            if strFC == i[0]:
                if strSFC == i[1]:
                    return i[2]
    return "FC_SFC not found ("+str(strFC)+", "+str(strSFC)+")"

def FCSFC2Name(strFC,strSFC):
    if CleanSFCstring(strSFC)!="-1":
        for i in lstFCSFC:
            if strFC == i[0]:
                if strSFC == i[1]:
                    return i[3]
    return "FC_SFC not found"

def S57ABB2Name(S57ABB):
    for i in lstFCSFC:
        if S57ABB == i[2]:
            return i[3]
    return "S57ABB not found"

def S57ABB2FSC(S57ABB):
    lstR = []
    for i in lstFCSFC:
        if i[2]==S57ABB:
            lstR.append(i)
    return lstR
    
                
    
# Music that accompanied the coding of this script:



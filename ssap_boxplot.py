### http://matplotlib.org/examples/pylab_examples/boxplot_demo2.html
#   This is simplified to work towards SSAP plotting
#   Thanks Josh Hemann for the example

import numpy as np
import matplotlib.pyplot as plt
import S57names

def pltit(dic_ssap_plot_obj):
    
    FCname = dic_ssap_plot_obj["meta"]["fcname"]
    fil_out = open(u"C:\Martin\Work\ssap\SSAP_boxplot_"+FCname+".ecp","w")
    fil_out.write("SSAP boxplot pltit() buld 1408181743 : " + FCname + "\n\n") 
    
    # *** See what the Plot suitable data structure looks like
    fil_out.write("The whole lot... "+str(dic_ssap_plot_obj)+"\n\n")
    
    obj_meta = dic_ssap_plot_obj["meta"]
    for tag in obj_meta.keys():
        fil_out.write(" meta  : "+str(tag)+" : "+str(obj_meta[tag])+"\n")
    fil_out.write("       :\n") 
    
    obj_allio = dic_ssap_plot_obj["allio"]
    for param in obj_allio.keys():
        fil_out.write(" allio : "+str(param)+" : "+str(obj_allio[param])+"\n")
    fil_out.write("       :\n") 
    
    obj_group = dic_ssap_plot_obj["group"]
    for param in obj_group.keys():
        fil_out.write(" group : "+str(param)+" : \n")
        for grp in obj_group[param].keys():
            fil_out.write(" group :     "+str(grp)+" : "+str(obj_group[param][grp])+"\n")
            
    fil_out.write("\n=====================================================================================================\n")

    # *** Building a plotable object, per parameter
    lst_parameters = dic_ssap_plot_obj["allio"].keys()
    for parameter in lst_parameters:
        fil_out.write("\n\n*** Making plot of parameter : " + parameter + "\n") 
        lol_data = list()
        lst_lbls = list()
        # ** Append the grouped data
        for group in dic_ssap_plot_obj["group"][param].keys():
            lol_data.append(dic_ssap_plot_obj["group"][parameter][group])
            num_n = len(dic_ssap_plot_obj["group"][parameter][group]) # The count of samples in the group
            str_S57 = S57names.FCSFC2ABB(dic_ssap_plot_obj["meta"]["fcname"],str(group)) # The S-57 name of the object
            if "not found" in str_S57:
                lst_lbls.append(str(group) + "\n[" + str(num_n) + "]")
                fil_out.write("   S57names can't find : " + str(dic_ssap_plot_obj["meta"]["fcname"])+", "+str(group) + "\n")
            else:
                lst_lbls.append(str_S57 + "\n[n=" + str(num_n) + "]")
                
        # ** Append the AllInOne data
        lol_data.append(dic_ssap_plot_obj["allio"][parameter])
        num_n = len(dic_ssap_plot_obj["allio"][parameter]) # The count of samples in the group
        lst_lbls.append("All" + "\n[" + str(num_n) + "]")
        
        fil_out.write(" data : " + str(lol_data) + "\n")
        fil_out.write(" labl : " + str(lst_lbls) + "\n")
        
        # ** Generate the plot ...
        
        # * calc min and max value in data
        num_of_groups = len(lol_data)
        num_max = -999999999999
        num_min =  999999999999
        for i in lol_data:
            if max(i) > num_max:
                num_max = max(i)
            if min(i) < num_min:
                num_min = min(i)
        
        fig, ax1 = plt.subplots(figsize=(10,6))
        fig.canvas.set_window_title('A Box-and-whiskers plot. ')
        plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)
        
        bp = plt.boxplot(lol_data, notch=0, sym='+', vert=1, whis=1.5)
        plt.setp(bp['boxes'], color='red')
        plt.setp(bp['whiskers'], color='red')
        plt.setp(bp['fliers'], color='blue', marker='+')
        
        # Add a horizontal grid to the plot, but make it very light in color
        # so we can use it for reading data values but not be distracting
        ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
        
        # Hide these grid behind plot objects
        ax1.set_axisbelow(True)
        ax1.set_title(str(dic_ssap_plot_obj["meta"]['fcname'])+" - "+str(parameter))
        #ax1.set_xlabel('X-axis lable')
        #ax1.set_ylabel('Y-axis lable')
        
        # Set the axes ranges and axes labels
        ax1.set_xlim(0.5, num_of_groups+0.5)
        top = num_max
        bottom = num_min
        ax1.set_ylim(bottom*1.01, top*1.01)
        xtickNames = plt.setp(ax1, xticklabels=np.repeat(lst_lbls,1))
        plt.setp(xtickNames, rotation=45, fontsize=8)
        
        ##plt.show()
        
        
        # Save the plot to file
        plt.savefig(u"C:\Martin\Work\ssap\ssapbox_"+str(dic_ssap_plot_obj["meta"]['fcname'])+"_"+str(parameter)+".png")
        
    return 0

# Assignment 4

def wallCalc_withParallel(ListOfLayers_series, ListOfLayers_parallel, f1, season):
    ### this function computes the overall U-factor of a wall. In input recieves two list: 
    ### a list contains the layer of the wall who are in series each other and the other list contain the layers of the wall
    ### which are in parallel each other. f1 is the ratio between the area of the first parallel layer to the total one.
    ### It returns a dictionary with the thermal resistances of all layers, total resistance, and the total U of the wall.
    ### Also a season can be specify for determine the thermal resistance of the outer(external) layer. 
    
    Material_Library={"Outside_surface_winter":0.03, "Outside_surface_summer":0.044, "Inside_surface":0.12, 
    "Cement_mortar_13mm":0.018, "Plywood_13mm":0.11, "Building_paper":0.011, "Acoustic_tile":0.32,
    "Wood_stud_140mm":0.98, "Wood_stud_90mm":0.63, "Glass_fiber_90mm":2.45, "Glass_fiber_25mm":0.7, 
    "Wood_fiberboard_13mm":0.23, "Wood_bevel_13mm":0.14, "Gypsum_wallboard_13mm":0.079, "Stucco_25mm":0.037,
    "Common_brick_100mm":0.12, "Wood_50mm":0.44}
    
    ListOfLayers_series.append("Inside_surface")
    
    if season=="winter":
        ListOfLayers_series.append("Outside_surface_winter")
    elif season=="summer":
        ListOfLayers_series.append("Outside_surface_summer")
    else:
        print("Please select a season between winter or summer")
        
    R_series=[]
    for anyLayer in ListOfLayers_series:
        R_series.append(Material_Library[anyLayer])
    R_series_tot=sum(R_series)
        
    R=[]
    for anyLayer in ListOfLayers_parallel:
        R_section_value=Material_Library[anyLayer]+R_series_tot
        R.append(R_section_value)
        
    
    R_pall_valueOne=Material_Library[ListOfLayers_parallel[0]]
    R_sectionOne=R_series+[R_pall_valueOne]
    R_pall_valueTwo=Material_Library[ListOfLayers_parallel[1]]
    R_sectionTwo=R_series+[R_pall_valueTwo]
    
    
    Utot=f1*R[0]**-1+(1-f1)*R[1]**-1
    
    Results={'Utot':Utot, 'Section One':R_sectionOne, 'Section Two':R_sectionTwo, 'Rtot12':R}
    return Results
    
    
    
def wallCalc_onlyInSeries(ListOfLayers):
        ### This computes the U-value for an opaque surface who has only layers 
        ### in series each other.
        
    
        Material_Library={"Outside_surface_winter":0.03, "Outside_surface_summer":0.044, "Inside_surface":0.12, 
        "Cement_mortar_13mm":0.018,"Wood_50mm":0.44, "Plywood_13mm":0.11, "Building_paper":0.011, "Acoustic_tile":0.32,
        "Wood_stud_140mm":0.98, "Wood_stud_90mm":0.63, "Glass_fiber_90mm":2.45, "Glass_fiber_25mm":0.7, 
        "Wood_fiberboard_13mm":0.23, "Wood_bevel_13mm":0.14, "Gypsum_wallboard_13mm":0.079, "Stucco_25mm":0.037}
        
        
        ListOfLayers_complete=["Inside_surface"]+["Outside_surface_winter"]+ListOfLayers
        Rtot=0
        R_list=[]
        for anylayers in ListOfLayers_complete:
            R_list.append(Material_Library[anylayers])
        Rtot=sum(R_list)
        
        U=Rtot**-1
        
        result={"Utot": U, "Rvalues_layers": R_list}
        return result
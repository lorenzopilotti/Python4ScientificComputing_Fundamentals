#Assignment3_step2


def wall_calc_assignment(ListOfLayers_series, ListOfLayers_parallel, f1, season):
    ### this function computes the overall U-factor of a wall. In input recieves two list: 
    ### a list contains the layer of the wall who are in series each other and the other list contain the layers of the wall
    ### which are in parallel each other. f1 is the ratio between the area of the first parallel layer to the total one.
    ### It returns a dictionary with the thermal resistances of all layers, total resistance, and the total U of the wall.
    ### Also a season can be specify for determine the thermal resistance of the outer(external) layer. 
    
    Material_Library={"Outside_surface_winter":0.03, "Outside_surface_summer":0.044, "Inside_surface":0.12, 
    "Cement_mortar_13mm":0.018, "Plywood_13mm":0.11, "Building_paper":0.011, "Acoustic_tile":0.32,
    "Wood_stud_140mm":0.98, "Wood_stud_90mm":0.63, "Glass_fiber_90mm":2.45, "Glass_fiber_25mm":0.7, 
    "Wood_fiberboard_13mm":0.23, "Wood_bevel_13mm":0.14, "Gypsum_wallboard_13mm":0.079}
    
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
    
    results={'Utot':Utot, 'Section One':R_sectionOne, 'Section Two':R_sectionTwo, 'Rtot12':R}
    return results

Layers_series=["Wood_bevel_13mm", "Wood_fiberboard_13mm", "Gypsum_wallboard_13mm"]
Layers_parallel=["Glass_fiber_90mm", "Wood_stud_90mm"]

#Overall U-factot
f1=0.75
season="winter"
Results=wall_calc_assignment(Layers_series, Layers_parallel, f1, season)
print Results

print('The overall U-factor of the wall is: ' +str(Results['Utot'])+' W/Km2')

#Rate of heat loss through the wall under design conditions (W)

p=0.2 # glazing percentage
P=50  # perimeter in m
H=2.5 # height in m
Tin=22
Tout=-2
Q_dot=(1-p)*P*H*Results['Utot']*(Tin-Tout) # watts
print('The rate of heat loss through the wall is: ' +str(Q_dot)+ ' W')
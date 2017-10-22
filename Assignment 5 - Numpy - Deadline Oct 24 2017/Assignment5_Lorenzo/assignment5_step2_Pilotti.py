#Assignment 5

import numpy as np

MaterialsNames=np.array(["Outside_surface_winter", "Outside_surface_summer", "Inside_surface", 
"Cement_mortar_13mm", "Plywood_13mm", "Building_paper", "Acoustic_tile",
"Wood_stud_140mm", "Wood_stud_90mm", "Glass_fiber_90mm", "Glass_fiber_25mm", 
"Wood_fiberboard_13mm", "Wood_bevel_13mm", "Gypsum_wallboard_13mm"])

MaterialsRvalue=np.array([0.03,0.044,0.12,0.018, 0.11, 0.011, 0.32, 0.98, 0.63, 2.45, 0.7, 0.23, 0.14, 0.079])

Materials_names_series=np.array(["Outside_surface_winter", "Wood_bevel_13mm", "Wood_fiberboard_13mm", 
"Gypsum_wallboard_13mm", "Inside_surface"])
Materials_name_parallel=np.array(["Glass_fiber_90mm", "Wood_stud_90mm"])
A_ratio=0.75


#Series calculation
Rvalue_series=np.zeros(Materials_names_series.size)

for layerName in Materials_names_series:
    Rvalue_series[Materials_names_series==layerName]=MaterialsRvalue[MaterialsNames==layerName]
    
print Rvalue_series

#Parallel calculation
Rvalue_parallel=np.zeros(Materials_name_parallel.size)

for layerName in Materials_name_parallel:
    Rvalue_parallel[Materials_name_parallel==layerName]=MaterialsRvalue[MaterialsNames==layerName]
    
print Rvalue_parallel

Uvalue_section1=(Rvalue_series.sum()+Rvalue_parallel[0])**-1
Uvaleu_section2=(Rvalue_series.sum()+Rvalue_parallel[1])**-1
Utot=A_ratio*Uvalue_section1+(1-A_ratio)*Uvaleu_section2

print Utot

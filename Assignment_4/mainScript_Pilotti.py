# Assignment 4


import os
os.chdir("C:\Users\Lorenzo\Dropbox_Polimi_PC\Dropbox\git_fork\Python4ScientificComputing_Fundamentals\Assignment_4")
import wallCalculations_Pilotti as WC


# Roof U-value calculation
Layers_roof=["Wood_stud_140mm", "Glass_fiber_90mm","Stucco_25mm"]
Roof_result=WC.wallCalc_onlyInSeries(Layers_roof)
U_roof=Roof_result["Utot"]
print("The U-value of the roof is: " + str(U_roof)+" W/m2/K.")

# Door U-value calculation
Layers_door=["Wood_50mm"]
Door_Result=WC.wallCalc_onlyInSeries(Layers_door)
U_door=Door_Result["Utot"]
print("The U-value of the roof is: " + str(U_door)+" W/m2/K.")

# Walls U-value calculation
Layers_series=["Wood_bevel_13mm", "Wood_fiberboard_13mm", "Gypsum_wallboard_13mm", "Common_brick_100mm"]
Layers_parallel=["Glass_fiber_90mm", "Wood_stud_90mm"]
Walls_result=WC.wallCalc_withParallel(Layers_series, Layers_parallel, 0.7, "winter")
U_walls=Walls_result["Utot"]
print("The U-value of the walls is: " + str(U_walls)+" W/m2/K.")
print("*********")

#Surfaces
deltaT_heating=20-(-4.8)
A_door=1*2.2
A_roof=10*20
A_fenestration=(4*1.8)*3+8*1.8
A_walls=(10*2+20*2)*2.4-A_door-A_fenestration

# Heating Factor (HF=deltaT*U)
HF_roof=deltaT_heating*U_roof
print("The heating factor (HF) of the roof is: " +str(HF_roof)+" W/m2.")
HF_door=deltaT_heating*U_door
print("The heating factor (HF) of the door is: " +str(HF_door)+" W/m2.")
HF_walls=deltaT_heating*U_walls
print("The heating factor (HF) of the walls is: " +str(HF_walls)+" W/m2.")
print("***********")

# Heating loads (Q=HF*A)
Q_roof=HF_roof*A_roof
print("The heating load due to the roof is: " +str(Q_roof)+ " W.")
Q_door=HF_door*A_door
print("The heating load due to the door is: " +str(Q_door)+ " W.")
Q_walls=HF_walls*A_walls
print("The heating load due to the roof is: " +str(Q_walls)+ " W.")

Q_tot_heating=Q_roof+Q_door+Q_walls
print("")
print("The total haeting load is :"+str(Q_tot_heating)+ " W.")




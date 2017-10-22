Material_Library = {"Outside_surface_Winter":0.030,"Inside_surface": 0.12,
"Insulation_Glass_Fiber_90mm":2.45, "WoodStud_90mm":0.63, 
"WoodFiberboard": 0.23,"WoodBevel_13x200": 0.14,"Gypsum_13mm":0.079,
"Stucco_25mm":0.037,"MineralFiber_25mm":0.66,"Plywood_13mm":0.11}

Layers_Wall_Serie = ["Outside_surface_Winter","WoodBevel_13x200","WoodFiberboard","Gypsum_13mm","Inside_surface"] 
Layers_Wall_Parallel= ["Insulation_Glass_Fiber_90mm","WoodStud_90mm"]

Rtot=0
Rvalues_serie=[]
for anyLayer in Layers_Wall_Serie:
    RValue= Material_Library[anyLayer]
    Rtot = Rtot+RValue
    Rvalues_serie.append(RValue)

Layers_Glass=Layers_Wall_Serie+[Layers_Wall_Parallel[0]]
RValue_glass= Material_Library["Insulation_Glass_Fiber_90mm"]
Rtot_g=Rtot+RValue_glass
U_glass=1/Rtot_g

Layers_Stud=Layers_Wall_Serie+[Layers_Wall_Parallel[1]]
RValue_stud= Material_Library["WoodStud_90mm"]
Rtot_s=Rtot+RValue_stud
U_stud=1/Rtot_s

fraction=0.75
U_tot=fraction*(U_glass)+(1-fraction)*(U_stud)
R_TOT=1/U_tot
print "The total R is "+str(R_TOT)
print "The total U is "+str(U_tot)
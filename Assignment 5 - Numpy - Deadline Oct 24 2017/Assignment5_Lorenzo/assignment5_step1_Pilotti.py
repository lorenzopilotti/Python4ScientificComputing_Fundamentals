# Assignment 5

import numpy as np


#Resistances in series
Res_series_names=np.array(["Rin", "R1", "R2", "R6", "Rout"])
Res_series_types=np.array(["Conv", "Cond", "Cond", "Cond", "Conv"])
Res_series_h=np.array([10, None, None, None, 25])
Res_series_L=np.array([None, 0.03, 0.02, 0.02, None])
Res_series_k=np.array([None, 0.026, 0.22, 0.22, None])
A_series=0.25*1
Res_series_Rvalue=np.array(np.zeros(5))
Res_series_Rvalue[Res_series_types=="Conv"]=1.0/Res_series_h[Res_series_types=="Conv"]/A_series
Res_series_Rvalue[Res_series_types=="Cond"]=Res_series_L[Res_series_types=="Cond"]/Res_series_k[Res_series_types=="Cond"]/A_series
Res_series_tot=Res_series_Rvalue.sum()

#Resistance in parallel
Res_parallel_names=np.array(["R3", "R4", "R5"])
Res_parallel_types=np.array(["Cond", "Cond", "Cond"])
Res_parallel_L=np.array([0.16, 0.16, 0.16])
Res_parallel_k=np.array([0.22, 0.72, 0.22])
Res_parallel_A=np.array([0.015, 0.22, 0.015])
Res_parallel_Rvalue=np.array(np.zeros(3))
Res_parallel_Rvalue[Res_parallel_types=="Cond"]=Res_parallel_L[Res_parallel_types=="Cond"]/Res_parallel_k[Res_parallel_types=="Cond"]/Res_parallel_A[Res_parallel_types=="Cond"]
U_parallel_value=1.0/Res_parallel_Rvalue
U_parallel_tot=U_parallel_value.sum()
Res_parallel_tot=U_parallel_tot**-1


#Total resistance
Rtot=+Res_series_tot+Res_parallel_tot  # referred to 0.25 m2 of surface area.







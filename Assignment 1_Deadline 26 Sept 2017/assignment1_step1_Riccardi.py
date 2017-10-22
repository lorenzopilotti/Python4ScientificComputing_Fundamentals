# -*- coding: utf-8 -*-
Tinf1=20 #indoor temperature  [°C]
Tinf2=-10 #outdoor temperature [°C]
h1=10 #indoor convective coeffcient [W/(m2*°C)]
h2=25 #outdoor convective coeffcient [W/(m2*°C)]
Kb=0.72 #thermal conductivity of bricks [W/(m*°C)]
Kp=0.22 #thermal conductivity of plaster [W/(m*°C)]
Kf=0.026 #thermal conductivity of foam [W/(m*°C)]
H1=0.25 #height of teh considered surface [m]
W1=1.0 #depth [m]
A1=H1*W1 #wall's considered surface [m2]
R1=1/(h1*A1) # indoor air thermoresistance [°C/W]
Lf=0.03 #foam thickness [m]
Rf=Lf/(Kf*A1) #foam thermoresistance [°C/W]
Lp=0.02 #thickness of a plaster layer [m]
Rp1=Lp/(Kp*A1) #thermoresistance of plaster layer 1 [°C/W]
Rp2=Rp1 #thermoresistance of plaster layer 2 [°C/W]
R2=1/(h2*A1) #thermoresistance of outdoor air [°C/W]
Lb=0.16 #brick's thickness [m]
Hb=0.22 #brick's height [m]
Ab=Hb*W1 # brick's surface [m2]
Rb=Lb/(Kb*Ab) #brick's thermoresistance [°C/W]
Hc1=0.015 #upper surface's height [m]
Ac1=W1*Hc1 #upper surface [m2]
Rc1=Lb/(Kp*Ac1)# upper thermoresistance [°C/W]
Rc2=Rc1 #lower thermoresistance [°C/W]
Rpar=(1/Rb+1/Rc1+1/Rc2)**(-1) #parallel resistance of Rb,Rc1 and Rc2 [°C/W]
Rtot=R1+Rf+Rp1+Rp2+Rpar+R2 # total resistance of the unit [°C/W]
Qunit=(Tinf1-Tinf2)/Rtot #heat flow crossing the unit [W]
Hwall=3 #wall's height [m]
Wwall=5 #wall's depth [m]
Awall=Hwall*Wwall #wall's surface [m2]
Qwall=Qunit*Awall/A1 #heat flow crossing the entire wall [W]
print("The total resistance of the unit is: "+str(Rtot)+" [°C/W]")
print("By using the formula Qunit=(Tinf1-Tinf2)/Rtot, the heat flow crossing the unit is: "+str(Qunit)+" [W]")
print("In the end, the total heat flow crossing the entire wall is Qwall=Qunit*Awall/Aunit="+str(Qwall)+" [W]")
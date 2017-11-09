# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  9 21:15:01 2017</p>
#
ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.00915327,-10000,10000,0,'Beta_time_PT' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0325237,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.0759791,-10000,10000,0,'Beta_Cost' )

Beta_Age1 = Beta('Beta_Age1',0.0570478,-10000,10000,0,'Beta_Age1' )

Beta_Age2 = Beta('Beta_Age2',-0.0102873,-10000,10000,0,'Beta_Age2' )

Beta_Age3 = Beta('Beta_Age3',0.00157186,-10000,10000,0,'Beta_Age3' )

Beta_urb = Beta('Beta_urb',0.673723,-10000,10000,0,'Beta_urb' )

Beta_TripWork = Beta('Beta_TripWork',0.349722,-10000,10000,0,'Beta_TripWork' )

Beta_TripLeisure = Beta('Beta_TripLeisure',-0.282636,-10000,10000,0,'Beta_TripLeisure' )

ASC_PM  = Beta('ASC_PM ',0.469475,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0190094,-10000,10000,0,'Beta_time_PM' )

Beta_rural = Beta('Beta_rural',-0.960377,-10000,10000,0,'Beta_rural' )

Beta_roman = Beta('Beta_roman',1.14569,-10000,10000,0,'Beta_roman' )

Beta_german = Beta('Beta_german',0.21971,-10000,10000,0,'Beta_german' )

ASC_SM = Beta('ASC_SM',1.44944,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.712484,-10000,10000,0,'Beta_Distance' )

Beta_Age1_walk = Beta('Beta_Age1_walk',-1.40397,-10000,10000,0,'Beta_Age1_walk' )

Beta_Age2_walk = Beta('Beta_Age2_walk',-0.00199755,-10000,10000,0,'Beta_Age2_walk' )

Beta_Age3_walk = Beta('Beta_Age3_walk',-0.00960892,-10000,10000,0,'Beta_Age3_walk' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Age1','Beta_Age1_walk','Beta_Age2','Beta_Age2_walk','Beta_Age3','Beta_Age3_walk','Beta_Cost','Beta_Distance','Beta_TripLeisure','Beta_TripWork','Beta_german','Beta_roman','Beta_rural','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','Beta_urb']
values = [[-3.26082e+08,-2.6731e+07,1.31133e+06,4.0549e+07,-191077,247728,661323,196164,3.83211e+06,4.67557e+07,-1.47049e+07,-8.13792e+06,1.95455e+08,3.69871e+08,3.10776e+08,1.88205e+06,1.45999e+06,-350978,1.16621e+08],[0.0801985,0.686675,0.000959935,0.551036,0.000618959,-0.0113183,0.000382001,-0.00753163,0.000847218,-0.0139206,0.0377814,0.0314752,0.0363515,0.0404041,-0.0439835,4.21235e-05,-0.000107715,0.000430012,0.0436476],[0.00100995,0.000967952,0.000246882,0.000194377,2.20101e-05,8.60519e-06,1.68204e-05,6.52072e-06,2.62083e-05,-1.41555e-05,0.000144443,7.92573e-05,0.000403491,0.000680111,-7.93054e-05,-1.31519e-05,-9.0395e-06,5.3257e-07,-3.7682e-05],[-0.0302333,0.551338,0.000183549,0.990146,3.98608e-05,-0.0122607,8.7739e-06,-0.008119,-0.000111371,0.0117053,-0.00593361,-0.00933112,-0.0164972,-0.0133163,0.0403234,-2.09335e-05,1.16951e-05,-2.4232e-05,-0.0424866],[0.000674276,0.000617757,2.19973e-05,3.7773e-05,2.437e-05,9.86462e-06,1.38076e-05,6.11317e-06,-5.12126e-07,3.08957e-06,8e-05,1.13335e-06,0.000351554,0.000307629,3.60641e-05,3.16498e-06,2.07308e-06,-9.72175e-08,-3.76742e-05],[0.000527623,-0.0113188,8.71308e-06,-0.0122574,9.84764e-06,0.000256998,5.98212e-06,0.000162339,2.63179e-08,-3.2129e-05,0.000100417,0.000122485,0.000290328,0.000273443,-0.000285741,1.56969e-06,9.08421e-07,4.46228e-08,0.00031926],[0.000437454,0.000384458,1.68181e-05,1.18627e-05,1.38114e-05,5.94945e-06,1.46992e-05,6.78011e-06,3.07028e-06,6.15011e-07,-7.8558e-05,2.53645e-05,0.000250098,0.000226672,1.53415e-05,-4.73684e-08,-1.93296e-07,5.58907e-07,1.88983e-06],[0.000299839,-0.00753206,6.59043e-06,-0.00811695,6.10202e-06,0.000162341,6.8015e-06,0.000137673,-4.30468e-08,-2.81502e-05,7.19645e-05,8.26595e-05,0.000180873,0.00014555,-0.000101325,6.82404e-07,3.68425e-07,-2.4217e-08,0.000133878],[0.000547765,0.000858702,2.62321e-05,-9.61452e-05,-5.0061e-07,-1.28013e-07,3.07915e-06,-1.45522e-07,0.000204529,3.42102e-05,0.000134534,0.000261858,0.000334621,0.000450774,-8.10257e-05,4.67924e-06,-6.96549e-06,7.07815e-06,0.000128823],[-0.00304364,-0.013717,-1.27017e-05,0.0120282,3.17831e-06,-3.49517e-05,1.09248e-06,-3.00065e-05,3.55671e-05,0.00641935,0.000652454,0.000855973,8.91612e-05,1.1871e-05,0.00439507,0.000117025,7.85274e-05,1.29924e-05,-0.00407265],[0.0297576,0.0377267,0.000144233,-0.00601308,7.9952e-05,0.000101164,-7.8641e-05,7.24547e-05,0.000134339,0.000656491,0.049677,0.0357813,0.0139627,0.0148123,-0.000873187,3.57113e-05,-5.41641e-05,0.000218132,-0.00146999],[0.0274386,0.0314903,7.92856e-05,-0.00930577,1.16773e-06,0.000122273,2.53599e-05,8.25314e-05,0.000261664,0.000852446,0.0357817,0.0454297,0.0134385,0.0134437,-0.00191536,9.93817e-05,-3.75913e-05,0.00022103,-0.00136992],[3.26082e+08,2.6731e+07,-1.31133e+06,-4.0549e+07,191077,-247728,-661323,-196164,-3.83211e+06,-4.67557e+07,1.47049e+07,8.13792e+06,-1.95455e+08,-3.69871e+08,-3.10776e+08,-1.88205e+06,-1.45999e+06,350978,-1.16621e+08],[3.26082e+08,2.6731e+07,-1.31133e+06,-4.0549e+07,191077,-247728,-661323,-196164,-3.83211e+06,-4.67557e+07,1.47049e+07,8.13792e+06,-1.95455e+08,-3.69871e+08,-3.10776e+08,-1.88205e+06,-1.45999e+06,350978,-1.16621e+08],[-0.0710018,-0.0427658,-7.73671e-05,0.0419793,3.75425e-05,-0.000302177,1.62303e-05,-0.000112097,-8.15235e-05,0.00423161,-0.000852523,-0.00190747,-0.0212166,-0.0301348,0.097684,3.18336e-05,4.49862e-05,-5.62793e-05,-0.087566],[-9.73718e-06,4.68987e-05,-1.31265e-05,-1.43079e-05,3.16683e-06,1.50492e-06,-4.04463e-08,6.3864e-07,4.69226e-06,0.000116825,3.57186e-05,9.95685e-05,9.57841e-05,1.38384e-05,3.38363e-05,6.6544e-05,4.30485e-05,3.25064e-06,4.46968e-05],[-8.99781e-05,-0.000103896,-9.02199e-06,1.69358e-05,2.07512e-06,8.56753e-07,-1.88333e-07,3.33642e-07,-6.95735e-06,7.83005e-05,-5.41448e-05,-3.74609e-05,4.06843e-05,-3.78879e-05,4.62615e-05,4.30476e-05,3.46812e-05,-5.06643e-06,3.26741e-05],[0.0003524,0.000427909,5.28266e-07,-2.72323e-05,-9.99552e-08,7.31674e-08,5.5705e-07,-5.71781e-09,7.07863e-06,1.32678e-05,0.000218105,0.000221028,0.000147776,0.0001814,-5.63928e-05,3.255e-06,-5.06371e-06,1.44725e-05,8.36606e-06],[0.0585743,0.0443021,-3.58838e-05,-0.0415496,-3.69308e-05,0.000310358,2.48262e-06,0.000128073,0.000128511,-0.00414985,-0.00146263,-0.00136332,0.0320597,0.0337596,-0.0875045,4.32001e-05,3.17248e-05,8.23665e-06,0.0973327]]
vc = bioMatrix(19,names,values)
BIOGEME_OBJECT.VARCOVAR = vc

# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:20:42 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Tue Nov 21 13:26:36 2017</p>
#
ASC_PT = Beta('ASC_PT',-2.36359,-10000,10000,0,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.636767,-10000,10000,0,'Beta_time_PT' )

LAMBDA = Beta('LAMBDA',1.07109e-08,-10000,10000,0,'LAMBDA' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0461026,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost_age1 = Beta('Beta_Cost_age1',-0.0111439,-10000,10000,0,'Beta_Cost_age1' )

Beta_Cost_age2 = Beta('Beta_Cost_age2',-0.00106895,-10000,10000,0,'Beta_Cost_age2' )

Beta_Cost_age3 = Beta('Beta_Cost_age3',-0.000149313,-10000,10000,0,'Beta_Cost_age3' )

Beta_Age1_PT = Beta('Beta_Age1_PT',1.98222,-10000,10000,0,'Beta_Age1_PT' )

Beta_Age2_PT = Beta('Beta_Age2_PT',-0.020401,-10000,10000,0,'Beta_Age2_PT' )

Beta_urb = Beta('Beta_urb',-0.212276,-10000,10000,0,'Beta_urb' )

Beta_TripWork = Beta('Beta_TripWork',0.394285,-10000,10000,0,'Beta_TripWork' )

Beta_TripLeisure = Beta('Beta_TripLeisure',-0.210708,-10000,10000,0,'Beta_TripLeisure' )

Beta_have_ga = Beta('Beta_have_ga',2.27546,-10000,10000,0,'Beta_have_ga' )

ASC_PM  = Beta('ASC_PM ',-0.360166,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0160409,-10000,10000,0,'Beta_time_PM' )

Beta_Age1_PM = Beta('Beta_Age1_PM',1.92796,-10000,10000,0,'Beta_Age1_PM' )

Beta_Age2_PM = Beta('Beta_Age2_PM',-0.0084998,-10000,10000,0,'Beta_Age2_PM' )

Beta_multi_trips = Beta('Beta_multi_trips',-0.381947,-10000,10000,0,'Beta_multi_trips' )

Beta_roman = Beta('Beta_roman',0.941943,-10000,10000,0,'Beta_roman' )

Beta_Distance = Beta('Beta_Distance',-0.645754,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_PT','Beta_Age1_PM','Beta_Age1_PT','Beta_Age2_PM','Beta_Age2_PT','Beta_Cost_age1','Beta_Cost_age2','Beta_Cost_age3','Beta_Distance','Beta_TripLeisure','Beta_TripWork','Beta_have_ga','Beta_multi_trips','Beta_roman','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','Beta_urb','LAMBDA']
values = [[0.18619,0.146125,0.137661,0.137611,-0.00300073,-0.00287569,-6.16573e-05,9.03123e-06,-1.24356e-05,0.0145836,-2.68313e-05,0.00111479,0.00119547,-0.00423731,-0.00686525,6.62004e-05,0.00918034,-0.000148833,0.00240148,-1.50077e-09],[0.146125,0.526235,0.14275,0.14323,-0.00285827,-0.00332913,0.00030228,1.0654e-05,-1.08761e-05,0.00909589,-0.0410075,-0.0250527,-0.00747619,0.0234494,0.00619703,-0.000951802,-0.0961954,0.00136445,-0.0146629,3.67469e-09],[0.137661,0.14275,0.433372,0.433053,-0.00282224,-0.0028742,-5.57239e-05,-1.2947e-05,-2.01008e-05,-0.00281195,-0.00213739,0.00352143,0.00108867,-0.00393541,-0.00467115,1.07951e-05,-0.00089982,-3.30403e-05,0.00105316,-2.34975e-09],[0.137611,0.14323,0.433053,0.432994,-0.00282366,-0.00286949,-3.7928e-05,-1.29245e-05,-2.00751e-05,-0.00282594,-0.00193606,0.00352993,0.000938699,-0.00383561,-0.00439317,9.10655e-06,-0.00118583,-2.59624e-05,0.000914039,-2.36947e-09],[-0.00300073,-0.00285827,-0.00282224,-0.00282366,7.1858e-05,6.83402e-05,6.94133e-07,-6.48305e-07,3.45376e-07,-4.78787e-05,-4.80777e-06,-1.76252e-05,5.64855e-05,3.1755e-05,-3.58474e-06,5.69726e-08,-1.84252e-06,2.56355e-07,-2.22739e-05,6.17548e-11],[-0.00287569,-0.00332913,-0.0028742,-0.00286949,6.83402e-05,7.60704e-05,7.28674e-08,-5.69177e-07,3.6976e-07,-4.37808e-05,0.000116208,-5.39692e-05,-2.99161e-06,2.06499e-05,-1.89235e-05,7.34195e-07,6.17301e-05,-1.5581e-06,-1.71127e-05,5.71418e-11],[-6.16573e-05,0.00030228,-5.57239e-05,-3.7928e-05,6.94133e-07,7.28674e-08,1.34704e-05,-1.96929e-07,-1.49555e-08,-1.3851e-05,9.631e-05,7.85536e-05,-5.42952e-05,3.16769e-05,4.4148e-05,7.90233e-07,-0.000167984,8.86506e-06,-4.23023e-05,-2.94208e-11],[9.03123e-06,1.0654e-05,-1.2947e-05,-1.29245e-05,-6.48305e-07,-5.69177e-07,-1.96929e-07,2.48659e-07,4.7134e-09,6.26594e-06,7.19727e-06,8.62187e-06,-2.28023e-05,-1.29909e-06,-1.0855e-06,-1.82171e-07,-4.47334e-06,1.19477e-07,-9.74533e-07,5.79771e-12],[-1.24356e-05,-1.08761e-05,-2.01008e-05,-2.00751e-05,3.45376e-07,3.6976e-07,-1.49555e-08,4.7134e-09,2.70198e-08,2.48757e-06,6.80449e-07,1.27793e-06,-1.34e-07,-2.86507e-06,-3.35066e-07,-2.70359e-08,-9.37629e-07,-2.57779e-08,1.21742e-07,1.08068e-12],[0.0145836,0.00909589,-0.00281195,-0.00282594,-4.78787e-05,-4.37808e-05,-1.3851e-05,6.26594e-06,2.48757e-06,0.005647,0.000490984,0.000288372,6.87732e-06,-0.000213399,-0.000314152,1.94687e-05,0.00144815,-1.28986e-05,0.000225904,2.8661e-10],[-2.68313e-05,-0.0410075,-0.00213739,-0.00193606,-4.80777e-06,0.000116208,9.631e-05,7.19727e-06,6.80449e-07,0.000490984,0.0517698,0.0404902,-0.00524551,-0.0114045,0.00112278,5.00429e-05,-0.00267125,0.000248757,-0.00131395,-1.52862e-09],[0.00111479,-0.0250527,0.00352143,0.00352993,-1.76252e-05,-5.39692e-05,7.85536e-05,8.62187e-06,1.27793e-06,0.000288372,0.0404902,0.053946,-0.00568062,-0.0181754,0.000353659,4.13405e-05,-0.00531902,0.000253434,-0.00284994,-1.22248e-09],[0.00119547,-0.00747619,0.00108867,0.000938699,5.64855e-05,-2.99161e-06,-5.42952e-05,-2.28023e-05,-1.34e-07,6.87732e-06,-0.00524551,-0.00568062,0.0573886,-0.00211441,0.000607651,0.00012343,0.0047573,-0.00016974,0.00173069,-2.36457e-09],[-0.00423731,0.0234494,-0.00393541,-0.00383561,3.1755e-05,2.06499e-05,3.16769e-05,-1.29909e-06,-2.86507e-06,-0.000213399,-0.0114045,-0.0181754,-0.00211441,0.0525466,0.00115832,-0.000108598,-0.00545091,0.000341581,-0.00241913,2.56949e-09],[-0.00686525,0.00619703,-0.00467115,-0.00439317,-3.58474e-06,-1.89235e-05,4.4148e-05,-1.0855e-06,-3.35066e-07,-0.000314152,0.00112278,0.000353659,0.000607651,0.00115832,0.0260959,-2.56826e-05,-0.001763,3.34114e-05,-0.00487213,3.63244e-10],[6.62004e-05,-0.000951802,1.07951e-05,9.10655e-06,5.69725e-08,7.34195e-07,7.90233e-07,-1.82171e-07,-2.70359e-08,1.94687e-05,5.00429e-05,4.13405e-05,0.00012343,-0.000108598,-2.56826e-05,9.5693e-06,0.000284992,1.13014e-06,1.0443e-05,-8.74063e-11],[0.00918034,-0.0961954,-0.00089982,-0.00118583,-1.84252e-06,6.17301e-05,-0.000167984,-4.47334e-06,-9.37629e-07,0.00144815,-0.00267125,-0.00531902,0.0047573,-0.00545091,-0.001763,0.000284992,0.0327424,-0.000625648,0.00307754,-9.97404e-10],[-0.000148833,0.00136445,-3.30403e-05,-2.59624e-05,2.56355e-07,-1.5581e-06,8.86506e-06,1.19477e-07,-2.57779e-08,-1.28986e-05,0.000248757,0.000253434,-0.00016974,0.000341581,3.34114e-05,1.13014e-06,-0.000625648,2.84458e-05,-0.000130558,-3.15558e-11],[0.00240148,-0.0146629,0.00105316,0.000914039,-2.22739e-05,-1.71127e-05,-4.23023e-05,-9.74533e-07,1.21742e-07,0.000225904,-0.00131395,-0.00284994,0.00173069,-0.00241913,-0.00487213,1.0443e-05,0.00307754,-0.000130558,0.0197,-7.41405e-10],[-1.50077e-09,3.67469e-09,-2.34975e-09,-2.36947e-09,6.17548e-11,5.71418e-11,-2.94208e-11,5.79771e-12,1.08068e-12,2.8661e-10,-1.52862e-09,-1.22248e-09,-2.36457e-09,2.56949e-09,3.63244e-10,-8.74063e-11,-9.97404e-10,-3.15558e-11,-7.41405e-10,2.29541e-14]]
vc = bioMatrix(20,names,values)
BIOGEME_OBJECT.VARCOVAR = vc

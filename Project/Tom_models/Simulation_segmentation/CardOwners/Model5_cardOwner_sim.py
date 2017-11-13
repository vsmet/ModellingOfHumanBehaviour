# Tom Suter
# 19.10.2017

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *


ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_time_PT = Beta('Beta_time_PT',0.252139,-10000,10000,0,'Beta_time_PT' )

LAMBDA = Beta('LAMBDA',0.20764,-10000,10000,0,'LAMBDA' )

Beta_time_PT_walk = Beta('Beta_time_PT_walk',-0.0403981,-10000,10000,0,'Beta_time_PT_walk' )

Beta_Cost = Beta('Beta_Cost',-0.0821963,-10000,10000,0,'Beta_Cost' )

Beta_Age1 = Beta('Beta_Age1',0.0682839,-10000,10000,0,'Beta_Age1' )

Beta_Age2 = Beta('Beta_Age2',-0.000118568,-10000,10000,0,'Beta_Age2' )

Beta_Age3 = Beta('Beta_Age3',0.00691567,-10000,10000,0,'Beta_Age3' )

Beta_urb = Beta('Beta_urb',-0.23458,-10000,10000,0,'Beta_urb' )

Beta_TripWork = Beta('Beta_TripWork',0.458256,-10000,10000,0,'Beta_TripWork' )

Beta_TripLeisure = Beta('Beta_TripLeisure',-0.2203,-10000,10000,0,'Beta_TripLeisure' )

ASC_PM  = Beta('ASC_PM ',0.325775,-10000,10000,0,'ASC_PM ' )

Beta_time_PM = Beta('Beta_time_PM',-0.0173783,-10000,10000,0,'Beta_time_PM' )

Beta_multi_trips = Beta('Beta_multi_trips',-0.286666,-10000,10000,0,'Beta_multi_trips' )

Beta_roman = Beta('Beta_roman',0.964825,-10000,10000,0,'Beta_roman' )

Beta_german = Beta('Beta_german',0.130362,-10000,10000,0,'Beta_german' )

ASC_SM = Beta('ASC_SM',0.907143,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.620771,-10000,10000,0,'Beta_Distance' )

Beta_Age1_walk = Beta('Beta_Age1_walk',-0.274965,-10000,10000,0,'Beta_Age1_walk' )

Beta_Age2_walk = Beta('Beta_Age2_walk',0.0155277,-10000,10000,0,'Beta_Age2_walk' )

Beta_Age3_walk = Beta('Beta_Age3_walk',-0.00274398,-10000,10000,0,'Beta_Age3_walk' )


## Code for the sensitivity analysis
names = ['ASC_PM ','ASC_SM','Beta_Age1','Beta_Age1_walk','Beta_Age2','Beta_Age2_walk','Beta_Age3','Beta_Age3_walk','Beta_Cost','Beta_Distance','Beta_TripLeisure','Beta_TripWork','Beta_german','Beta_multi_trips','Beta_roman','Beta_time_PM','Beta_time_PT','Beta_time_PT_walk','Beta_urb','LAMBDA']
values = [[1.61849e+11,3.08978e+10,-2.86527e+09,-1.45456e+10,-2.61846e+09,4.91065e+07,-1.96933e+09,1.01467e+09,-9.71055e+08,-1.04215e+10,6.01425e+10,6.66155e+10,-7.91003e+10,-2.17429e+10,-8.42464e+10,-2.05472e+09,9.0097e+10,-1.3476e+09,-4.27031e+09,-1.12272e+11],[-0.163955,0.72031,-0.00478832,0.0075488,-0.00427962,-0.00903502,-0.00316669,-0.00498472,0.00179522,-0.0449924,0.131875,0.143864,0.43853,-0.0258548,0.431356,-0.00297392,0.20537,-0.00157678,0.0020679,-0.256332],[0.000879681,0.00227466,0.000365563,0.000151091,3.88977e-05,1.89976e-05,2.83692e-05,1.73011e-05,-2.83826e-06,-0.000111656,0.000598892,0.00072481,0.00232022,-7.68263e-05,0.00260144,-1.50499e-05,0.000536097,-5.49641e-06,2.81697e-05,-0.000852934],[0.0610859,0.049663,-0.00232096,0.0431912,-0.00228785,-0.000529664,-0.00169498,0.000363231,-0.000659424,-0.00992664,0.0449709,0.0508223,-0.00612927,-0.0162986,-0.00744298,-0.00169059,0.0759962,-0.00105311,-0.00402268,-0.0970352],[0.000949481,0.00157421,4.32838e-05,-8.12635e-05,3.68116e-05,1.73661e-05,2.26524e-05,1.33608e-05,-7.88485e-06,-5.53338e-05,0.000177481,0.000188387,0.00151256,-2.25218e-05,0.0014653,-7.23371e-06,0.000386637,-4.73359e-06,1.01753e-05,-0.000483252],[0.00422154,-0.00987785,0.00012397,-0.000278561,0.000105499,0.000219526,7.41641e-05,0.000115924,-3.18636e-06,0.000372026,-0.0011464,-0.00137038,-0.00488463,4.57874e-05,-0.00489676,5.90413e-05,-0.00297807,2.97565e-05,0.000205558,0.00393427],[0.000631485,0.00104942,3.19734e-05,-5.46864e-05,2.30659e-05,1.04068e-05,2.35283e-05,1.24118e-05,-8.19333e-06,-3.89545e-05,-7.25145e-05,0.000155795,0.00102283,3.4299e-05,0.000960446,-5.92637e-06,0.000254592,-3.16308e-06,1.33212e-05,-0.00032275],[0.00285808,-0.00656083,8.44679e-05,-0.000177072,7.0012e-05,0.000132676,5.34419e-05,0.000125332,-4.48603e-06,0.000280224,-0.000751482,-0.000897475,-0.00325027,5.34773e-05,-0.0032772,3.82753e-05,-0.00196559,1.9948e-05,0.000101182,0.00258431],[-5.15886e-05,0.00178302,-1.16228e-05,-8.26916e-05,-1.37276e-05,-4.89541e-06,-1.21124e-05,-5.90555e-06,0.000318493,9.15126e-05,0.000587678,0.00103286,0.00163302,-0.000759459,0.00143376,4.49378e-05,0.000426765,5.93268e-06,0.00025767,-0.000113538],[0.011968,-0.0145791,0.000106054,0.000111406,9.8055e-05,-9.52335e-05,6.84364e-05,-3.87212e-05,0.00011518,0.00930744,-0.000237319,-0.00071211,-0.00906285,-0.00043878,-0.00904272,0.00012197,-0.00197421,2.10536e-05,0.000263253,0.00415875],[0.0119612,0.0549056,-0.00010177,-0.00142446,-0.000368598,0.000139005,-0.000458391,0.000155486,0.000602674,-0.00156893,0.0713999,0.0542799,0.051674,-0.0177095,0.0517878,-3.51914e-05,0.0148868,0.000100428,-0.00146353,-0.0188207],[0.0112744,0.0522992,-3.55433e-05,-0.00123941,-0.000397378,0.000140644,-0.000257849,0.000164499,0.00102757,-0.00184677,0.0535655,0.0722337,0.0514096,-0.0244586,0.0495133,-4.79802e-05,0.0146286,1.41741e-05,-0.00173472,-0.0190176],[-1.61849e+11,-3.08978e+10,2.86527e+09,1.45456e+10,2.61846e+09,-4.91065e+07,1.96933e+09,-1.01467e+09,9.71055e+08,1.04215e+10,-6.01425e+10,-6.66155e+10,7.91003e+10,2.17429e+10,8.42464e+10,2.05472e+09,-9.0097e+10,1.3476e+09,4.27031e+09,1.12272e+11],[-0.017309,0.00114718,1.34374e-05,3.23657e-05,4.35468e-05,-0.00039353,8.13496e-05,-0.00024719,-0.000745186,-0.000683692,-0.01664,-0.0233129,-0.00503057,0.06934,-0.00342429,-0.000313677,-0.00366505,0.000413485,-0.00632851,-0.00054811],[-1.61849e+11,-3.08978e+10,2.86527e+09,1.45456e+10,2.61846e+09,-4.91065e+07,1.96933e+09,-1.01467e+09,9.71055e+08,1.04215e+10,-6.01425e+10,-6.66155e+10,7.91003e+10,2.17429e+10,8.42464e+10,2.05472e+09,-9.0097e+10,1.3476e+09,4.27031e+09,1.12272e+11],[0.000174455,0.000878385,-7.35199e-06,-1.74961e-05,-2.8455e-06,-2.25714e-07,-2.97002e-06,-1.06095e-06,4.88922e-05,4.42342e-05,0.00023629,0.00024161,0.000816738,-0.000332999,0.0007305,2.55114e-05,0.00027352,4.22315e-06,6.96304e-05,1.27419e-05],[0.0118986,0.0109877,-7.46071e-05,-0.000733881,6.72287e-06,8.33183e-06,-4.41347e-06,2.37244e-05,0.000234251,0.00112858,0.00194019,0.00129997,0.00516329,-0.00324852,0.00463672,0.000161102,0.00558712,-9.15802e-05,0.000422644,-0.00182702],[-0.000181049,0.000537469,-4.04786e-06,-1.00703e-05,-4.50729e-06,-3.08696e-06,-3.07889e-06,-1.5331e-06,7.58454e-06,-2.87785e-05,0.000267693,0.000197807,0.000522338,0.000391587,0.000524575,2.64861e-06,3.97578e-05,1.97364e-05,-7.0836e-05,-0.000179628],[0.00564966,0.00519777,-4.41294e-06,-0.00124325,-1.46325e-05,0.000155364,-3.66351e-06,7.49975e-05,0.000250042,0.00011381,-0.000863296,-0.0010339,0.00772649,-0.0065458,0.000841605,4.65783e-05,0.00147696,-8.29953e-05,0.026262,-0.00102918],[-0.00557788,0.00258026,-9.28284e-05,0.000330129,-2.43468e-05,-1.69578e-05,-1.21331e-05,-4.38457e-05,0.000168877,-0.000396652,-0.000840355,-0.000469576,0.00575188,-0.00113987,0.00524821,0.000137716,-0.000178128,-1.3711e-05,0.000283793,0.00265699]]

# Define here arithmetic expressions for name that are not directly available from the data
#--- availability
pm_avail =  DefineVariable('pm_avail', ((CarAvail != 3)+(NbMoto>=1))>0 )
bike_walk_avail =  DefineVariable('bike_walk_avail', ((distance_km)<8 + (NbBicy>0)*(distance_km)<16)>0)
CardOwner = DefineVariable('CardOwners', (HalfFareST == 1) + (LineRelST == 1) + (GenAbST == 1) + (AreaRelST == 1) + (OtherST == 1) > 0)

one  = DefineVariable('one',1)
#----time
car_time  = DefineVariable('car_time', TimeCar )
pt_total_time = DefineVariable('pt_total_time', TimePT)
pt_wait_time = DefineVariable('pt_wait_time', WaitingTimePT)
pt_walk_time = DefineVariable('pt_walk_time',WalkingTimePT)
pt_transp_time= DefineVariable('pt_transp_time',InVehicleTime*(InVehicleTime>0))

distance_trip=DefineVariable('distance_trip',distance_km)
reported_time=DefineVariable('reported_time',ReportedDuration)
#---cost
car_cost=DefineVariable('car_cost',CostCar)
PT_cost=DefineVariable('PT',MarginalCostPT)  #marginal tiens en compte le demi tarif etc
#socioeco
CalcIncome= DefineVariable('CalcIncome', CalculatedIncome*(CalculatedIncome>0) )
age1= DefineVariable('age1', age*(age<=25))
age2= DefineVariable('age2', age*(25<age<=65))
age3= DefineVariable('age3', age*(age>65))
urb= DefineVariable('urb',1*(UrbRur==1))
rur= DefineVariable('rur',1*(UrbRur==2))
roman= DefineVariable('roman',1*(Region<4))
german = DefineVariable('german',1*(Region>=4))
commune1=DefineVariable('commune1',1*(TypeCommune<7))
commune2=DefineVariable('commune2',1*(TypeCommune>7))
Tripwork=DefineVariable('Tripwork',1*(TripPurpose==1))
TripLeisure=DefineVariable('TripLeisure',1*(TripPurpose==3))
#other
Multi_trips = DefineVariable('Multi_trips', NbTrajects > 2)


# Utilities
## public transport
_Public_T = ASC_PT*one \
            +Beta_time_PT*(((pt_transp_time**LAMBDA)-1)/LAMBDA) \
            +Beta_time_PT_walk*(pt_walk_time+pt_wait_time )\
            +Beta_Cost* PT_cost*0.9 \
            +Beta_Age1*age1+Beta_Age2*age2+Beta_Age3*age3\
            +Beta_urb*urb\
            +Beta_TripWork*Tripwork+Beta_TripLeisure*TripLeisure\

## private mods
_Private_M = ASC_PM*one \
            + Beta_time_PM*car_time \
            + Beta_Cost* car_cost \
            + Beta_multi_trips*Multi_trips\
            + Beta_roman*roman \
            + Beta_german*german

## soft modes
_soft_M = ASC_SM*one \
         + Beta_Distance*distance_trip\
         + Beta_Age1_walk*age1+Beta_Age2_walk*age2+Beta_Age3_walk*age3\

V = {0: _Public_T,1: _Private_M ,2: _soft_M }
av = {0: one,1: pm_avail,2: bike_walk_avail}




#No need for estimating the model (it is already estimated). We want to obtain the individual probabilities and the market shares
probPT = bioLogit(V,av,0)
probPM = bioLogit(V,av,1)
probSM = bioLogit(V,av,2)
probChosen = bioLogit(V,av,Choice) #Instead of reporting the choice in the simulation file, the probability of the chosen can be printed

# Defines an itertor on the data
rowIterator('obsIter')

#Simulation output
simulate = {'Choice':Choice,
            '01 Prob. PT': probPT,
            '02 Prob. PM': probPM,
            '03 Prob. SM': probSM,
            }

BIOGEME_OBJECT.SIMULATE = Enumerate(simulate,'obsIter')

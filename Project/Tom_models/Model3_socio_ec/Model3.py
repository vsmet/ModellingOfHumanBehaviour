# Tom Suter
# 19.10.2017

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *


#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_PT = Beta('ASC_PT',0,-10000,10000,1)
ASC_PM =  Beta('ASC_PM ',0,-10000,10000,0)
ASC_SM = Beta('ASC_SM',0,-10000,10000,0)
Beta_time_PT= Beta('Beta_time_PT',0,-10000,10000,0)
Beta_time_PT_wait=Beta('Beta_time_PT_wait',0,-10000,10000,0)
Beta_time_PT_walk=Beta('Beta_time_PT_walk',0,-10000,10000,0)
Beta_time_PM= Beta('Beta_time_PM',0,-10000,10000,0)
Beta_Distance= Beta('Beta_Distance',0,-10000,10000,0)
Beta_Cost = Beta('Beta_Cost',0,-10000,10000,0)
#Beta_Income_car=Beta('Beta_Income_car',0,-10000,10000,0)  #useless
#Beta_Income_PT=Beta('Beta_Income_PT',0,-10000,10000,0)     #useless
Beta_Income=Beta('Beta_Income',0,-10000,10000,0)
Beta_Age=Beta('Beta_Age',0,-10000,10000,0)

# Define here arithmetic expressions for name that are not directly available from the data

one  = DefineVariable('one',1)
#----time
car_time  = DefineVariable('car_time', TimeCar )
pt_total_time = DefineVariable('pt_total_time', TimePT)
pt_wait_time = DefineVariable('pt_wait_time', WaitingTimePT)
pt_walk_time = DefineVariable('pt_walk_time',WalkingTimePT)
pt_transp_time= DefineVariable('pt_transp_time',InVehicleTime)

distance_trip=DefineVariable('distance_trip',distance_km)
reported_time=DefineVariable('reported_time',ReportedDuration)
#---cost
car_cost=DefineVariable('car_cost',CostCar)
PT_cost=DefineVariable('PT',MarginalCostPT)  #marginal tiens en compte le demi tarif etc
#socioeco
CalcIncome= DefineVariable('CalcIncome', CalculatedIncome )

# Utilities
## public transport
_Public_T = ASC_PT*one + Beta_time_PT*pt_transp_time+Beta_time_PT_walk*(pt_walk_time+pt_wait_time )\
            + Beta_Cost* PT_cost +Beta_Income*(CalcIncome)+Beta_Age*age
## private mods
_Private_M = ASC_PM*one + Beta_time_PM*car_time + Beta_Cost* car_cost +Beta_Income*(CalcIncome)
## soft modes
_soft_M = ASC_SM*one + Beta_Distance*distance_trip+Beta_Age*age

V = {0: _Public_T,1: _Private_M,2: _soft_M}
av = {0: one,1: one,2: one}



#Exclude
BIOGEME_OBJECT.EXCLUDE = Choice   ==  -1


# MNL (Multinomial Logit model), with availability conditions
logprob = bioLogLogit(V,av,Choice)

# Defines an iterator on the data
rowIterator('obsIter')

# Define the likelihood function for the estimation
BIOGEME_OBJECT.ESTIMATE = Sum(logprob,'obsIter')

# Optimization algorithm
BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "BIO"
BIOGEME_OBJECT.PARAMETERS['stopFileName'] = "STOP"

# Print some statistics:
nullLoglikelihood(av,'obsIter')
choiceSet = [0,1,2]
cteLoglikelihood(choiceSet,Choice,'obsIter')
availabilityStatistics(av,'obsIter')
BIOGEME_OBJECT.FORMULAS['Opt1'] = _Public_T
BIOGEME_OBJECT.FORMULAS['Opt2'] = _Private_M
BIOGEME_OBJECT.FORMULAS['Opt3'] = _soft_M
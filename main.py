import numpy as np
import inputs as ipt
from datetime import datetime, timedelta
from essentials.basic import Nurse

# Import inputs
days = ipt.DAY_OF_MONTH
nursesLength = ipt.AMOUNT_NURSES


# Making the matrix schedule
schedule = np.matrix(np.zeros((nursesLength, days)))


tempoTotal = 30

inicio = datetime(2017,1,1,0,0,0)
deltaT = timedelta(hours=8)

calendar = []

for i in (range(tempoTotal)):
    obj = {'data': inicio + i*deltaT,
           'nurses':[1,3,6,7]}
    calendar.append(obj)

for c in calendar:
    print 'DATA: ', c['data'], 'Enfermeira: ',c['nurses']
    #print c
#print schedule
#print 'dia 1', np.sum(schedule[:,0])


#n = Nurse(1, 'Patricia', 'Paleativos')
#print n

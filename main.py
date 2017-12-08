import numpy as np
import inputs as ipt

# Import inputs
days = ipt.DAY_OF_MONTH
nursesLength = ipt.AMOUNT_NURSES


# Making the matrix schedule
schedule = np.matrix(np.zeros((nursesLength, days)))



print schedule
print 'dia 1', np.sum(schedule[:,0])

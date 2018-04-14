#!-*- encoding: utf-8 -*-

import numpy as np
import inputs as ipt
from datetime import datetime, timedelta
from essentials.basic import Nurse
from essentials.basic import Calendar

# Import inputs
days = ipt.DAY_OF_MONTH
nursesLength = ipt.AMOUNT_NURSES

# Making the matrix schedule
schedule = np.matrix(np.zeros((nursesLength, days)))

calendario = Calendar(2017,01,01,0,0,0, 1, 30)

calendario.show2()



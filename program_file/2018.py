import datafuncs as f
import pandas as pd
import pywt
import plotly.graph_objs as go
from datetime import datetime, timedelta

"""#**2018 / Janeiro a Dezembro**

##ACE def


$Ace  Jan/Dez2018$
"""

ace, denoised_ace = f.Bz_data_processer('./Bz_data - DSCOVR - ACE - WIND/2018/Bz_data_ACE_20180101_a_20181231.txt', False, 'ACE')

"""##WIND def

$WIND Jun/Dez 2018$
"""

wind, denoised_wind = f.Bz_data_processer('./Bz_data - DSCOVR - ACE - WIND/2018/Bz_data_WIND_20180101_a_20181231.txt', False, 'WIND')

"""##DSCOVR def

$DSCOVR Jun/Dez 2018$
"""


dscovr, denoised_dscovr = f.Bz_data_processer('./Bz_data - DSCOVR - ACE - WIND/2018/Bz_data_WIND_20180101_a_20181231.txt', False, 'DSCOVR')

"""##COMBINAÇÂO DAS 3 def"""

combine = f.combiner(ace, denoised_ace, wind, denoised_wind, dscovr, denoised_dscovr)
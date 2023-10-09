import datafuncs as f
import pandas as pd
import pywt
import plotly.graph_objs as go
from datetime import datetime, timedelta

"""#**2020 / Janeiro a Dezembro**

##ACE def

$Ace  Jan/Dez2020$
"""

ace, denoised_ace = f.Bz_data_processer('./Bz_data - DSCOVR - ACE - WIND/2020/Bz_data_ACE_20200101_a_20201231.txt', True, 'ACE')

"""##WIND def

$WIND Jun/Dez 2020$
"""

wind, denoised_wind = f.Bz_data_processer('./Bz_data - DSCOVR - ACE - WIND/2020/Bz_data_WIND_20200101_a_20201231.txt', True, 'WIND')

"""##COMBINAÇÂO DAS 2 def"""

combine = f.combiner(ace, denoised_ace, wind, denoised_wind, 0, 0)

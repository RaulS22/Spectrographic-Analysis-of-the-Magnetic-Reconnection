import datafuncs as f

"""#**2021 / Janeiro a Dezembro**

##ACE def

$Ace  Jan/Dez2021$
"""

ace, denoised_ace = f.Bz_data_processer('./Bz_data - DSCOVR - ACE - WIND/2021/Bz_data_ACE_20210101_a_20211231.txt', True, 'ACE')

"""##WIND def

$WIND Jun/Dez 2021$
"""

wind, denoised_wind = f.Bz_data_processer('./Bz_data - DSCOVR - ACE - WIND/2021/Bz_data_WIND_20210101_a_20211231.txt', True, 'WIND')

"""##COMBINAÇÂO DAS 2 def"""

combine = f.combiner(ace, denoised_ace, wind, denoised_wind, 0, 0)
import datafuncs as f

"""#**2018 / Janeiro a Dezembro**

##ACE def


$Ace  Jan/Dez2018$
"""

ace, denoised_ace = f.Bz_data_processer('./Bz_data - DSCOVR - ACE - WIND/2017/Bz_data_ACE_20170101_a_20171231.txt', False, 'ACE')

"""##WIND def

$WIND Jun/Dez 2018$
"""

wind, denoised_wind = f.Bz_data_processer('./Bz_data - DSCOVR - ACE - WIND/2017/Bz_data_WIND_20170101_a_20171231.txt', False, 'WIND')


dscovr, denoised_dscovr = f.Bz_data_processer('./Bz_data - DSCOVR - ACE - WIND/2017/Bz_data_WIND_20170101_a_20171231.txt', False, 'DSCOVR')

"""##COMBINAÇÂO DAS 3 def"""

combine = f.combiner(ace, denoised_ace, wind, denoised_wind, dscovr, denoised_dscovr)
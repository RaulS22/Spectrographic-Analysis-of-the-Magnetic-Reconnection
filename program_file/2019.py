import datafuncs as f

"""#**2019 / Janeiro a Dezembro**

##ACE def


$Ace  Jan/Dez2019$
"""

ace, denoised_ace = f.Bz_data_processer('./Bz_data - DSCOVR - ACE - WIND/2019/Bz_data_ACE_20190101_a_20191231.txt', False, 'ACE')

"""##WIND def

$WIND Jun/Dez 2019$
"""

wind, denoised_wind = f.Bz_data_processer('./Bz_data - DSCOVR - ACE - WIND/2019/Bz_data_WIND_20190101_a_20191231.txt', False, 'WIND')

"""##COMBINAÇÂO DAS 2 def"""

combine = f.combiner(ace, denoised_ace, wind, denoised_wind, 0, 0)
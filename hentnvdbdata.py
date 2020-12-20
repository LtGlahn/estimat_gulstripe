"""
Script som henter data fra NVDB og lagrer som geopackage-fil (.gpkg), et moderne GIS-format

Scriptet forutsetter at vi har dette biblioteket her: https://github.com/LtGlahn/nvdbapi-V3
Filene apiforbindelse.py, nvdbapiv3.py og nvdbgeotricks.py er hentet derfra. 

Data som hentes: 
  - Vegnett 
  - Rekkverk som brukes til midtdeler eller midtrekkverk
  - Vegoppmerking som brukes til gulstripe
  - Vegbredde (tre ulike objekttyper i NVDB)

Datanedlasting tar ca 10-15 minutter på en grei bredbåndslinje (200mb) 
"""

import nvdbgeotricks

filnavn_gpkg = 'nvdbdata.gpkg'


mittfilter = { 'vegsystemreferanse' : 'Ev,Rv' }

# Henter Rekkverk (objekttype 5) med bruksområde = Midtdeler eller Midtrekkverk 
# Samtidig henter vi vegnettsdata (default vegnett=True)
mittfilter['egenskap'] = '(1248=11789 OR 1248=11788)'
nvdbgeotricks.nvdb2gpkg( 5, filnavn=filnavn_gpkg, mittfilter=mittfilter, vegsegmenter=True, geometri=False )

# Henter Vegoppmerking, langsgående (objekttype 99) med bruksområde = midtlinje
# henter ikke vegnett enda en gang 
mittfilter['egenskap'] = "4520=5342"
nvdbgeotricks.nvdb2gpkg( 99, filnavn=filnavn_gpkg, mittfilter=mittfilter, vegsegmenter=True, geometri=False, vegnett=False  )


# Henter data for vegbredde. Disse antar vi det blir en del fikling med før vi har  optimale terskelverdier for 
# de ulike variantene av vegbredde, så vi henter rubb og rake. 
mittfilter.pop('egenskap', None)
breddetyper = [647, 583,838]
nvdbgeotricks.nvdb2gpkg( breddetyper, filnavn=filnavn_gpkg, mittfilter = mittfilter, vegsegmenter=True, geometri=False, vegnett=False )
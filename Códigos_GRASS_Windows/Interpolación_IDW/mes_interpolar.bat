@echo off
setlocal enabledelayedexpansion

g.region vector=Zonainterpolar@PERMANENT

set /a control=2
set /a cont=0

for /L %%a in (2000, 1, 2019) do (
    for /L %%m in (1, 1, 12) do (
        set /a control+=1
	set /a cont+=1
        v.surf.idw --overwrite input=Precipitacionesmensual@PERMANENT column=dbl_!control! output=Prec_mes_%%a-%%m_!cont!
    )
)
@echo off
setlocal enabledelayedexpansion

g.region vector=Zonainterpolar@PERMANENT

set /a control=0

for /L %%a in (2000, 1, 2019) do (
    for /L %%m in (1, 1, 12) do (
        set /a control+=1
	r.colors --verbose map=Prec_mes_%%a-%%m_!control!@PERMANENT rules=C:\Users\moise\OneDrive\Escritorio\ColorMes_FactorR
    )
)
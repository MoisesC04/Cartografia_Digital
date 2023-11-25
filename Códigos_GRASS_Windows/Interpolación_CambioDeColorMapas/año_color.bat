@echo off
setlocal enabledelayedexpansion

g.region vector=Zonainterpolar@PERMANENT

for /L %%i in (3, 1, 22) do (
    set /a year=1997+%%i
    r.colors --verbose map=Prec_ano_!year!@PERMANENT rules=C:\Users\moise\OneDrive\Escritorio\Color_FactorR
)
@echo off
setlocal enabledelayedexpansion

g.region vector=Zonainterpolar@PERMANENT

for /L %%i in (3, 1, 22) do (
    set /a year=1997+%%i

    v.surf.idw --overwrite --verbose input=PrecipitacionesAnual@PERMANENT column=dbl_%%i output=Prec_ano_!year!
)

endlocal
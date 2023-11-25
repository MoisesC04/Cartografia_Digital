import arcpy

# Check licenses / TODAS LAS FUNCIONES LLEVAN TEXTO ""
arcpy.CheckOutExtension("Spatial")

# Check entorno / SIN LICENCIA 0
arcpy.env.parallelProcessingFactor = "0%"
arcpy.env.overwriteOutput = True

# Arguments
WorkspaceAno = arcpy.GetParameterAsText(0)
WorkspaceMes = arcpy.GetParameterAsText(1)
WorkspaceSalida = arcpy.GetParameterAsText(2)

# Local variables
arcpy.AddMessage("Creando variables...")
ano = []
mes = []
factorR = []


for i in range(20):
    if i < 10:
        ano.append('{}\\PAnual200{}.tif'.format(WorkspaceAno, i))
    else:
        ano.append('{}\\PAnual20{}.tif'.format(WorkspaceAno, i))
        
    for j in range(12):
        if j < 9:
            if i < 10:
                mes.append('{}\\PMes200{}_0{}.tif'.format(WorkspaceMes, i,j+1))
                factorR.append('{}\\FRMes200{}_0{}.tif'.format(WorkspaceSalida, i,j+1))
            else:
                mes.append('{}\\PMes20{}_0{}.tif'.format(WorkspaceMes, i,j+1))
                factorR.append('{}\\FRMes20{}_0{}.tif'.format(WorkspaceSalida, i,j+1))
        else:
            if i < 10:
                mes.append('{}\\PMes200{}_{}.tif'.format(WorkspaceMes, i,j+1))
                factorR.append('{}\\FRMes200{}_{}.tif'.format(WorkspaceSalida, i,j+1))
            else:
                mes.append('{}\\PMes20{}_{}.tif'.format(WorkspaceMes, i,j+1))
                factorR.append('{}\\FRMes20{}_{}.tif'.format(WorkspaceSalida, i,j+1))
arcpy.AddMessage("...Completado")

# Process: Raster Calculator
contador = 0
for i in range(20):        
    for j in range(12):
        arcpy.gp.RasterCalculator_sa('(1.735*(10 ^ (1.5* Log10(( ({}/25.4) ^ 2)/{})-0.8188))*17.02)*10000'.format(mes[contador], ano[contador]), factorR[contador])
        contador += 1

arcpy.gp.RasterCalculator_sa("(1.735*(10 ^ (1.5* Log10(( (\"%PAnual2007.tif%\" /25.4) ^ 2)/\"%PAnual2006.tif%\" )-0.8188))*17.02)*10000", log10_raster)
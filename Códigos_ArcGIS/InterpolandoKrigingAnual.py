import arcpy

# Check licenses / TODAS LAS FUNCIONES LLEVAN TEXTO ""
arcpy.CheckOutExtension("Spatial")

# Check entorno / SIN LICENCIA 0
arcpy.env.parallelProcessingFactor = "0%"
arcpy.env.overwriteOutput = True

# Arguments
Input_Datos = arcpy.GetParameterAsText(0)
Workspace = arcpy.GetParameterAsText(1)

# Local variables
arcpy.AddMessage("Creando variables...")
contenedor = []
exportar = []
varianza = ""

for i in range(20):
    col = 4 + i
    contenedor.append('F{}'.format(col))
    if i < 10:
        exportar.append('{}\\PAnual200{}.tif'.format(Workspace, i))
    else:
        exportar.append('{}\\PAnual20{}.tif'.format(Workspace, i))

arcpy.AddMessage("...Completado")

# Process: Kriging
for i in range(len(contenedor)):

    if i < 10:
        ano = '200{}'.format(i)
    else:
        ano = '20{}'.format(i)

    try:
    
        arcpy.AddMessage("{} Realizando interpolacion - Spherical ...".format(ano))

        # Process: Kriging
        arcpy.gp.Kriging_sa(Input_Datos, contenedor[i], exportar[i], "Spherical 172.418888", "100", "VARIABLE 12", varianza)

        arcpy.AddMessage("...Completed")
    except:
        arcpy.GetMessages('Error, verificar el año {}.'.format(ano))
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
ano = 2000
varianza = ""

for i in range(20):
    for j in range(12):
        if j < 9:
            contenedor.append('{}_0{}'.format(ano,j+1))
            if i < 10:
                exportar.append('{}\\PMes200{}_0{}.tif'.format(Workspace, i,j+1))
            else:
                exportar.append('{}\\PMes20{}_0{}.tif'.format(Workspace, i,j+1))
        else:
            contenedor.append('{}_{}'.format(ano,j+1))
            if i < 10:
                exportar.append('{}\\PMes200{}_{}.tif'.format(Workspace, i,j+1))
            else:
                exportar.append('{}\\PMes20{}_{}.tif'.format(Workspace, i,j+1))
    ano += 1

arcpy.AddMessage("...Completado")

# Process: Kriging
for i in range(len(contenedor)):
    try:
        arcpy.AddMessage("{} Realizando interpolacion - Spherical ...".format(contenedor[i]))
        arcpy.gp.Kriging_sa(Input_Datos, contenedor[i], exportar[i], "Spherical 172.418888", "100", "VARIABLE 12", varianza)
        arcpy.AddMessage("...Completed")
    except:
        arcpy.GetMessages("...Error")
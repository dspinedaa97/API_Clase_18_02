from urllib import response

import geopandas as gpd
import requests

def generar_limites(localidad):
    myGeojson = gpd.read_file("loca.geojson.json")
    #Buscar el polígono por LocCogido
    #Tener en cuenta que LocCodigo es una cadena de texto
    
    resultado = myGeojson[myGeojson["LocCodigo"].astype(int) == localidad]

    # Extraer los vértices de la geometría

    x1,y1,x2,y2 = resultado["geometry"].bounds
    return x1, y1, x2, y2
print (generar_limites(19))

def llamarAPI(localidad):
    url = "https://geoportal.jbb.gov.co/agc/rest/services/JBB/CensoArbol_v0/MapServer/0/query"
    xmin,ymin,xmax,ymax = generar_limites(localidad)
    params = {"where": "1=1",
              "geometry": f"{xmin, ymin, xmax, ymax}",
              "geometryType": "esriGeometryEnvelope",
              "spatialRel": "esriSpatialRelIntersects",
              "outFields": "*",
              "f": "geojson",
              "inSR": 4326,
              "outSR": 4326 
          }
    
    response = requests.get(url, params=params)

    return response
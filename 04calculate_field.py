#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ermiasbt
#
# Created:     14.10.2018
# Copyright:   (c) ermiasbt 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# typebebygg_dict = {"Gaarde": "Gård", "Gaard": "Gård"}


typebebygg_dict = {
"Adelige Sædegaarde": "Adelig Sædegård",
"Annekskirke": "Annekskirke",
"Annex Kirker": "Annekskirke",
"Annexer": "Anneks",
"Annexkirke": "Annekskirke",
"Batterichefs Gaard": "Batterichefs gård",
"Batterichefs Gaarde": "Batterichefs gård",
"Capelangaarde": "Kapelangård",
"Civil Embeds Gaard": "Sivil embeds gård",
"Civile Embeds Gaarde": "Sivil embeds gård",
"Compagnichefs Gaarde": "Kompagnichefs gård",
"Compagnichefs-Gaarde": "Kompagnichefs gård",
"Compagniechefsgaarde": "Kompagnichefs gård",
"Eskvadronchefs Gaarde": "Eskvadronchefs gård",
"Esqvadronchefs Gaarde": "Eskvadronchefs gård",
"Forhen adelig Sædegaard": "Forhen adelig Sædegård",
"Forhen adelige Sædegaarde": "Forhen adelig Sædegård",
"Gaard": "Gård",
"Gaarde": "Gård",
"Hoved Kirker": "Hovedkirke",
"Hovedkirke": "Hovedkirke",
"Hovedkirker": "Hovedkirke",
"Kapelangaard": "Kapelangård",
"Kapelangaarde": "Kapelangård",
"Kompagnichefs Gaard": "Kompagnichefs gård",
"Kompagnichefs Gaarde": "Kompagnichefs gård",
"Korpschefs Gaard": "Korpschefs gård",
"Korpschefs Gaarde": "Korpschefs gård",
"Præstegaard": "Prestegård",
"Præstegaarde": "Prestegård"
}

def typebebyggNorm(typebebygg):
    if typebebygg in typebebygg_dict.keys():
        return typebebygg_dict[typebebygg]
    else:
        return typebebygg


expression = "typebebyggNorm(!TypeBebygg!)"

codeblock = """
def typebebyggNorm(typebebygg):
    if typebebygg in typebebygg_dict.keys():
        return typebebygg_dict[typebebygg]
    else:
        return typebebygg"""

arcpy.AddField_management("Bebyggelse", "TypeBebyggNorm", "TEXT", "", "", "50")
arcpy.CalculateField_management("Bebyggelse", "TypeBebyggNorm",
                                expression, "PYTHON", codeblock)
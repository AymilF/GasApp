import datetime
import json
import os
import xml.etree.ElementTree as ET
import zipfile

import requests
from requests.exceptions import HTTPError


def refresh_data():
    # fetch the xml file from the updated flux
    url = "http://donnees.roulez-eco.fr/opendata/instantane"
    try:
        response = requests.get(url, verify=False)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

    with open("ZIP.zip", "wb") as ziped:
        ziped.write(response.content)

    with zipfile.ZipFile("ZIP.zip", 'r') as zip_ref:
        zip_ref.extractall("./")

    os.remove("ZIP.zip")
    xmlfile = 'PrixCarburants_instantane.xml'
    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # create empty list for pdv
    with open('conf_stations.json', 'r') as confile:
        conf_stations = json.load(confile)
    idents = [station["ident"] for station in conf_stations["stations"]]
    res = dict()
    reslst = []
    for pdv in root.findall('pdv'):
        ident = int(pdv.get('id'))
        # cp = pdv.find('cp').text
        # adresse = pdv.find('adresse').text
        # latitude = float(pdv.get('latitude'))
        # longitude = float(pdv.get('longitude'))
        if ident in idents:
            for station in conf_stations["stations"]:
                if station["ident"] == ident:
                    nom = station["nom"]
            for prix in pdv.findall('prix'):
                essence = prix.get('nom')
                if essence == "E10" or essence == "SP95":
                    valeur = float(prix.get('valeur'))
                    valmaj = prix.get('maj')
                    time = datetime.datetime.strptime(valmaj,
                                                      "%Y-%m-%d %H:%M:%S")
                    maj = time.strftime("%d/%m")
                    mydict = {
                        "nom": nom,
                        "essence": essence,
                        "prix": "{:.4} €".format(valeur),
                        "maj": maj
                        }
                    # print(nom, prix.get('nom'), float(prix.get('valeur')))
                    reslst.append(mydict)
    res.update({"stations": reslst})
    with open('gas.json', 'w') as json_file:
        print(res)
        json.dump(res, json_file, indent=4)
    return res

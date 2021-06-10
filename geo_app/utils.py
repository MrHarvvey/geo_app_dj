from . models import Town
import xml.etree.ElementTree as ET


def object_list_towns():
    try:
        town_file = ET.parse('csv_files/SIMC_Adresowy_2021-06-09.xml')
        mystreet = town_file.getroot()
        object_list = []
        for symbol, town_name in zip(mystreet.iter('SYM'), mystreet.iter('NAZWA')):
            object_list.append(Town(town_name.text, symbol.text))
    except Exception as error:
        print(str(error) + " Something went wrong")
        return error
    return object_list

town_list = object_list_towns()


def search_town(list_of_elements, searched_city):
    #takes only ist values
    for item in list_of_elements:
        if item.name == searched_city:
            return str(item.id_t)
    return False

def list_of_streets(id_town):
    #taking values
    try:
        street_file = ET.parse('csv_files/ULIC_Adresowy_2021-06-10.xml')
        mystreet = street_file.getroot()
        list_of_streets = []
        for symbol, street_name in zip(mystreet.iter('SYM'), mystreet.iter('NAZWA_1')):
                if str(symbol.text) == str(id_town):
                    list_of_streets.append(street_name.text)
    except Exception as error:
        print(str(error) + "  Unable do download streets")
        return error
    return list_of_streets

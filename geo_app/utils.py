from . models import Town
import xml.etree.ElementTree as ET


def object_list_towns():
    #function load data from xml file and save it into class Town object list
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




def search_town(list_of_elements, searched_city):
    #function search in list Town.objects if any contains 'searched_city' if not return False if yes returns id of that city
    for item in list_of_elements:
        if item.name == searched_city:
            return str(item.id_t)
    return False


def load_street_file():
    #loading xml file and load it to getrootobject
    try:
        street_file = ET.parse('csv_files/ULIC_Adresowy_2021-06-10.xml')
        my_street_xml = street_file.getroot()
    except Exception as error:
        print(str(error) + "  Unable do download streets")
        return error
    return my_street_xml

def list_of_streets(id_town, my_street_xml):
    #search if given id_town has any streets if yes it returns list of it if not returns empty list
    try:
        list_of_streets = []
        for symbol, street_name in zip(my_street_xml.iter('SYM'), my_street_xml.iter('NAZWA_1')):
                if str(symbol.text) == str(id_town):
                    list_of_streets.append(street_name.text)
    except Exception as error:
        print(str(error) + "  Unable do download streets")
        return error
    return list_of_streets

town_list = object_list_towns()
street_xml = load_street_file()


import xml.etree.ElementTree as ET

class Town:
    def __init__(self, town_name, id_t):
        self.name = town_name
        self.id_t = id_t
        self.street_list = []

def list_objects():
    try:
        town_file = ET.parse('csv_files/SIMC_Adresowy_2021-06-09.xml')
        mystreet = town_file.getroot()
        object_list = []
        for symbol, town_name in zip(mystreet.iter('SYM'), mystreet.iter('NAZWA')):
            object_list.append(Town(town_name.text, symbol.text))
    except Exception as error:
        print(str(error) + "  First Error")
        return error
    return object_list

object_list = list_objects()

def list_of_streets(id_town):
    #taking values
    try:
        street_file = ET.parse('csv_files/ULIC_Urzedowy_2021-06-09.xml')
        mystreet = street_file.getroot()
        list_of_streets = []
        for symbol, street_name in zip(mystreet.iter('SYM'), mystreet.iter('NAZWA_1')):
                if str(symbol.text) == str(id_town):
                    list_of_streets.append(street_name.text)
    except Exception as error:
        print(str(error) + "  First Error")
        return error
    return list_of_streets





def search_town(list_of_elements, searched_city):
    #takes only ist values
    for item in list_of_elements:
        if item.name == searched_city:
            return str(item.id_t)
    return False

def search_town_streets(town_id, obje):
    list_of_towns = []

id_town_1 = search_town(list_objects(), input("wpisz szukane miasto: "))



if id_town_1 is False:
    print('miasto nie ma ulic')
else:
    print(list_of_streets(id_town_1))






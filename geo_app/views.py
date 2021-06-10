from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .utils import search_town, list_of_streets, town_list, street_xml



@api_view(['POST'])
def street_search(request):
    #curl -X POST -H "Content-Type: application/json" -d @towns.json 127.0.0.1:8000/street/
    error_bad_req = {'error': "City does not exist in our database"}
    if request.method == 'POST':
        try:
            searched_city = request.data['city']
        except:
            error_bad_req = {'error': "You should use request with one parameter 'city' "}
            return Response(error_bad_req, status=status.HTTP_200_OK)
        try:
            searched_town = search_town(town_list, searched_city)
            if searched_town == False:
                return Response(error_bad_req, status=status.HTTP_200_OK)
            elif not list_of_streets(searched_town, street_xml):
                error_req_streets = {'error': "City does not have any streets"}
                return Response(error_req_streets, status=status.HTTP_200_OK)
            else:
                dict_1 = {'result': list_of_streets(searched_town, street_xml)}
            return Response(dict_1, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            error_bad_req = {'error': "Something went wrong "}
            return Response(error_bad_req, status=status.HTTP_400_BAD_REQUEST)
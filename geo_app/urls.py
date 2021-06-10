from django.urls import path
from .views import street_search

urlpatterns = [
	#Leave as empty string for base url
	path('street/', street_search, name="Finding Street"),
]


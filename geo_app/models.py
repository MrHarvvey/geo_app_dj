from django.db import models

# Create your models here.

class Town:
    def __init__(self, town_name, id_t):
        self.name = town_name
        self.id_t = id_t
        self.street_list = []

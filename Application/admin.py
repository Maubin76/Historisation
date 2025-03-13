from django.contrib import admin
from Application.models import Personne

class PersonneAdim(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'address']

admin.site.register(Personne, PersonneAdim)

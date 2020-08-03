from django.contrib import admin
from portfolio.models import *
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = "Devishi's Art"
    index_title = "Edit my artworks"

admin_site = MyAdminSite(name='myadmin')

admin_site.register(soulsearchingmodel)
admin_site.register(thirtyonedaysofmemodel)
admin_site.register(wanderlustmodel)
admin_site.register(innerconsciencemodel)
admin_site.register(regenerationmodel)
admin_site.register(theuntoldtruthmodel)
admin_site.register(thehumantrapmodel)
admin_site.register(series)
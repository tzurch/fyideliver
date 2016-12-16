from django.contrib import admin

# Register your models here.
from fyideliverapp.models import Business, Customer, Driver

admin.site.register(Business)
admin.site.register(Customer)
admin.site.register(Driver)

from django.contrib import admin
from .models import Snack,Snacknumber
# Register your models here.

@admin.register(Snack)
class Adminsnack (admin.ModelAdmin):

    pass

@admin.register(Snacknumber)
class Adminsnacknumbur (admin.ModelAdmin):
    list_display=['name','price','is_cool']

    

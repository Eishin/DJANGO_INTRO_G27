from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'status')
    search_fields = ('nombre',)
    list_filter = ('status',)

admin.site.register(Producto, ProductoAdmin)

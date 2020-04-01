from django.contrib import admin
from .models import *

admin.site.register(Datasource)
admin.site.register(Schema)
admin.site.register(Table)
admin.site.register(Attribute)
admin.site.register(Mapping)
from django.contrib import admin
from . models import Depts
# Register your models here.
class DeptsModelAdmin(admin.ModelAdmin):
    list_display=('id','deploy_name','created_at')
    ordering = ('id',)
    readonly_fields =('id','created_at')

admin.site.register(Depts,DeptsModelAdmin)
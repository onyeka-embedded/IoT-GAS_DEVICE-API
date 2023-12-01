from django.contrib import admin
from .models import Gas
from .models import User

# Register your models here.
class GasModelAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'co', 'nox', 'temp', 'hum')
    
    #def custom_name(self, obj):
       # return f'Custom Data: {obj.device_id}'
admin.site.register(Gas, GasModelAdmin)
       
       
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'email', 'gas')
    
    #def custom_name(self, obj):
     #   return obj.gas    
admin.site.register(User, UserModelAdmin)

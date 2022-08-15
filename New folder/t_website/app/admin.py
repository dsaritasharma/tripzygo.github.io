from django.contrib import admin
from django.contrib.auth.admin import admin
from .models import * 

@admin.register(myuser)
class myuserAdmin(admin.ModelAdmin):
    
    model = myuser
    list_display = ('pk','email','username','password','confirm_password')
    


@admin.register(contact)
class myuserAdmin(admin.ModelAdmin):
    
    model = contact
    list_display = ('pk','name','email','phone','next_destination','no_of_passanger',
                    'start_date','end_date','share_your_message')

@admin.register(package)
class myuserAdmin(admin.ModelAdmin):
    
    model = package
    list_display = ('pk','destination','description','price','image')

from django.contrib import admin
from .models import bankUser, bankNames, User
# Register your models here.
admin.site.register(bankUser)
admin.site.register(bankNames)
admin.site.register(User)
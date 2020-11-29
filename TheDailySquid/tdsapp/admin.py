from django.contrib import admin

from tdsapp.models import *

class AccountAdmin(admin.ModelAdmin):
    list_display = ('username','password','dob')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'category')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('image', 'bio')

admin.site.register(Account, AccountAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Article, ArticleAdmin)
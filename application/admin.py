from django.contrib import admin
from .models import (
    Profile, 
    Project, 
    Referee, 
    Education, 
    Experience,
    Contact,
)


# class activationAdmin(admin.ModelAdmin):
#     list_display = ('user', 'code', 'email')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("email", "git_link")
    prepopulated_fields = {"slug": ("email",)}

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project)
admin.site.register(Referee)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Contact)
from django.contrib import admin
from .models import Profile, Stat
from .forms import ProfileForm, StatForm

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name','username',"count")
    form = ProfileForm
@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('date',"count")
    form = StatForm

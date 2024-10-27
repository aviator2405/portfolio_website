from django.contrib import admin
from website.models import feedback

class feedbackadmin(admin.ModelAdmin):
    list_display=('name','email','message')
# Register your models here.
admin.site.register(feedback,feedbackadmin)

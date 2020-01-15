from django.contrib import admin
from .models import ask_question,Solution,Dicussion_Like

admin.site.register(ask_question)
admin.site.register(Solution)
admin.site.register(Dicussion_Like)

# Register your models here.

from django.contrib import admin

# Register your models here.
from .models import MyCompiler,Question,Testcases

admin.site.register(MyCompiler)


admin.site.register(Question)
admin.site.register(Testcases)

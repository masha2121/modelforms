from django.contrib import admin
from .models import students, Teachers, Parents,Post

#
admin.site.register(students)
admin.site.register(Teachers)
admin.site.register(Parents)
admin.site.register(Post)

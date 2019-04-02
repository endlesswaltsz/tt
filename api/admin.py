from django.contrib import admin
from api import models
# Register your models here.
# admin.register(models.CourseCategory)
admin.site.register(models.CourseCategory)
admin.site.register(models.PricePolicy)
admin.site.register(models.LightCourse)
admin.site.register(models.FreeCourse)
admin.site.register(models.UserInfo)
admin.site.register(models.Teacher)
admin.site.register(models.CourseDetail)

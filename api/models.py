from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=16)


class Token(models.Model):
    user = models.ForeignKey(to='UserInfo')
    token = models.CharField(max_length=128)
    expired_time = models.DateTimeField()


class FreeCourse(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(to='CourseCategory', null=True, blank=True)
    policy = GenericRelation(to='PricePolicy', object_id_field='course_id')
    detail = models.OneToOneField(to='CourseDetail', null=True)
    teacher = models.ForeignKey(to='Teacher', null=True)

    def __str__(self):
        return self.name


class CourseDetail(models.Model):
    slogan = models.CharField(max_length=32)
    recommend = models.ManyToManyField(to=FreeCourse, blank=True)
    image = models.FileField(upload_to='image')

    def __str__(self):
        return '%s' % self.slogan


class Teacher(models.Model):
    name = models.CharField(max_length=12)
    level_choice = ((0, '铜牌'), (1, '银牌'), (2, '金牌'))
    level = models.SmallIntegerField(choices=level_choice)

    def __str__(self):
        return '<%s>(%s)' % (self.name, self.get_level_display())


class LightCourse(models.Model):
    name = models.CharField(max_length=32)
    policy = GenericRelation(to='PricePolicy', object_id_field='course_id')
    teacher = models.ForeignKey(to='Teacher', null=True)

    def __str__(self):
        return self.name


class CourseCategory(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class PricePolicy(models.Model):
    content_type = models.ForeignKey(to=ContentType)
    period = models.CharField(max_length=12)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    course_id = models.SmallIntegerField(null=True)
    course = GenericForeignKey(fk_field='course_id')

    def __str__(self):
        return self.course.name

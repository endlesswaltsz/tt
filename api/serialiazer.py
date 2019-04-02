from rest_framework import serializers

from api import models


# from api.models import Course


class CategorySer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = '__all__'


class FreeCourseSer(serializers.ModelSerializer):
    class Meta:
        model = models.FreeCourse
        fields = ['name', 'teacher_name', 'image', 'cheapest_price','id']
    id=serializers.IntegerField()
    image = serializers.SerializerMethodField()
    name = serializers.CharField(max_length=12)
    teacher_name = serializers.SerializerMethodField()
    cheapest_price = serializers.SerializerMethodField()

    def get_image(self, obj):
        return str(obj.detail.image)

    def get_teacher_name(self, obj):
        return obj.teacher.name

    def get_cheapest_price(self, obj):
        all_price = obj.policy.all()
        res = min(all_price, key=lambda obj: obj.price)
        return {'period':res.period,'price': res.price}


class CourseDetailSer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseDetail
        fields = ['slogan', 'name', 'policy', 'teacher', 'recommend']

    name = serializers.SerializerMethodField()
    policy = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()
    recommend = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.freecourse.name

    def get_policy(self, obj):
        course = models.FreeCourse.objects.filter(detail=obj).first()
        policy_list = course.policy.all()
        return [{policy.period: policy.price} for policy in policy_list]

    def get_teacher(self, obj):
        return {'name': obj.freecourse.teacher.name, 'id': obj.freecourse.teacher.pk}

    def get_recommend(self, obj):
        recommends = obj.recommend.all()
        return [{'name': recommend.name, 'id': recommend.pk} for recommend in recommends]


class Response:
    def __init__(self):
        self.status = 100
        self.msg = None

    @property
    def response(self):
        return self.__dict__


response = Response()

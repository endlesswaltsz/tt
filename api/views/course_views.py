from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from api import models
from api.serialiazer import CategorySer, FreeCourseSer, CourseDetailSer
from api.serialiazer import response


class CourseCategory(APIView):
    def get(self, request, *args, **kwargs):
        categorys = models.CourseCategory.objects.all()
        ser = CategorySer(categorys, many=True)
        response.msg = ser.data
        return Response(response.response)


class Course(APIView):
    def get(self, request, *args, **kwargs):
        category = request.query_params.get('category')
        if category:
            course_list = models.FreeCourse.objects.filter(category_id=category).order_by('pk')
        else:
            course_list = models.FreeCourse.objects.all().order_by('pk')
        page = PageNumberPagination()
        page.page_size = 7
        page_list = page.paginate_queryset(course_list, request, self)
        ser = FreeCourseSer(page_list, many=True)
        response.msg = ser.data
        return Response(response.response)


class CourseDetail(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        detail = models.CourseDetail.objects.filter(freecourse__pk=pk).first()
        ser = CourseDetailSer(instance=detail, many=False)
        response.msg = ser.data
        return Response(response.response)

# class Test(APIView):
#     def get(self, request, *args, **kwargs):
#         obj=models.LightCourse.objects.filter(pk=1).first()
#         models.PricePolicy.objects.create(price=1000,period='7天',course=obj)
#         models.PricePolicy.objects.create(price=2000,period='15天',course=obj)
#         models.PricePolicy.objects.create(price=3888,period='30天',course=obj)
#         return Response(response.response())

from django.utils.deprecation import MiddlewareMixin


class CustomCors(MiddlewareMixin):
    def process_response(self, request, response):
        allowed = ['127.0.0.1']
        ip = request.META.get('REMOTE_ADDR')
        if ip in allowed:
            response['Access-Control-Allow-Origin'] = 'http://' + ip + ':8080'
            if request.method == 'OPTIONS':
                response['Access-Control-Allow-Headers'] = 'Content-Type'
                response['Access-Control-Allow-Methods'] = '*'
        return response

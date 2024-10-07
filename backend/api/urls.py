from django.urls import path
from django.http import JsonResponse

def sample_data(request):
    return JsonResponse({"message": "Hello from Django!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/data/', sample_data),
]

from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def status_view(request):
    return JsonResponse({"status": "Cosmus Trader está rodando com sucesso!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('status/', status_view),  # nova rota para verificar se está tudo ok
]
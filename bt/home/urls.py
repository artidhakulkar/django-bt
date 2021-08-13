
from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('cources/', views.cources, name="cources"),
    path('placement/', views.placement, name="placement"),
    path('programming/', views.programming, name="programming"),
    path('development/', views.development, name="development"),
    path('python_developer/', views.python_developer, name="python_developer"),
    path('machine_learning/', views.machine_learning, name="machine_learning"),
    path('quantitive_aptitude/', views.quantitive_aptitude, name="quantitive_aptitude"),
    path('django/', views.django, name="django"),
    path('flask/', views.flask, name="flask"),
    path('english_speaking/', views.english_speaking, name="english_speaking"),
    path('soft_skill/', views.soft_skill, name="soft_skill"),
    path('cad/', views.cad, name="cad"),



]
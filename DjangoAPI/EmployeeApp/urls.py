from django.urls import path
from EmployeeApp import views

urlpatterns=[
    path('department/',views.departmentApi),
   
]

# from django.conf.urls import url
# from EmployeeApp import views

# from django.conf.urls.static import static
# from django.conf import settings

# urlpatterns=[
#     url(r'^department$',views.departmentApi),
#     url(r'^department/([0-9]+)$',views.departmentApi),

#]
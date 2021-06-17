from django.urls import path
from .views import homeview, addprodcutview, showproductviews, updateproductview, deleteproductview,signupview, signinview, signoutview
urlpatterns = [path('hv/', homeview, name='home'),
               path('apv/', addprodcutview, name='addproduct'),
               path('spv/', showproductviews, name='showprod'),
               path('upv/<int:id>/', updateproductview, name='updteprod'),
               path('dpv/<int:id>/', deleteproductview, name='deltprod'),
               path('suv/', signupview, name='signup'),
               path('siv/', signinview, name='signin'),
               path('sov/', signoutview, name='signout'),
               ]
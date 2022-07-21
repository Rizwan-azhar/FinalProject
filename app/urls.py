from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm
urlpatterns = [
    # path('', views.home),
    path ('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('orders/', views.orders, name='orders'),
    path('bags/', views.BagView.as_view(), name='bags'),
    path('bags/<slug:data>', views.BagView.as_view(), name='bagsdata'),
    path('crossbody/', views.CrossBodyView.as_view(), name='crossbody'),
    path('crossbody/<slug:data>', views.CrossBodyView.as_view(), name='crossbodydata'),
    path('backpack/', views.BackPackView.as_view(), name='backpack'),
    path('backpack/<slug:data>', views.BackPackView.as_view(), name='backpackdata'),
    path('accounts/login/' , auth_views.LoginView.as_view(template_name = 'app/login.html' , authentication_form = LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('passwordchange/' ,  auth_views.PasswordChangeView.as_view(template_name = 'app/passwordchange.html', form_class= MyPasswordChangeForm), name='passwordchange'),

    # path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('registration/' , views.CustomerRegistrationView.as_view(), name ='customerregistration'),
    path('orderplaced/', views.orderplaced, name='orderplaced'),

] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

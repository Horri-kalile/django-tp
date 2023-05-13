from django.urls import path,include
from . import views
#from .views import CategoryAPIView      api
#from rest_framework import routers        api
#from magasin.views import ProductViewset, CategoryAPIView     api

from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns =[
    path('',views.index,name='index'),
    path('affichefou/',views.affichefou,name='affichefou'),
    path('edit_product/',views.edit_product,name='edit_product'),
    #path('edit_Fourni/',views.edit_Fourni,name='edit_Fourni'),
    path('produit_detail/',views.produit_detail,name='produit_detail'),
    path('post/edit/<int:id>/', views.edit_product, name='post-edit'),
    path('editFourni/edit/<int:id>/', views.edit_Fourni, name='edit-fourni'),
    path('deletepersonnel/delete/<int:pk>/', views.deleteProduit, name='delete-produit'),
    path('deletefournisseur/delete/<int:pk>/', views.deletefournisseur, name='delete-fournisseur'),
    path('produitdetail/<int:id>/', views.ProduitView.as_view(), name='produits'),
    path('addFournisseur/',views.addFournisseur,name='addFournisseur'),
    path('AddProd/',views.AddProd,name='AddProd'),
    path('register/',views.register, name = 'register'), 
    path('listcom/',views.listcom,name='listcom'),
    path('addCommande/',views.addCommande,name='addCommande'),
     path('password-reset/', PasswordResetView.as_view(template_name='magasin/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='magasin/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='magasin/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='magasin/password_reset_complete.html'),name='password_reset_complete'),

   # path('api-auth/', include('rest_framework.urls'))   api
   #  path('api/category/', CategoryAPIView.as_view())   api
   # path('api/', include(router.urls)),       api

]
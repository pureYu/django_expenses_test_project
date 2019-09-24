from django.urls import path
from .views import CostListView, CostDetailView, CostCreateView, CostUpdateView, CostDeleteView, UserCostListView

from . import views

urlpatterns = [
    # path('', views.home, name='tracker-home'),
    path('', CostListView.as_view(), name='tracker-home'),  # instead of 'views.home'
    path('user/<str:username>', UserCostListView.as_view(), name='user-costs'),
    path('cost/<int:pk>/', CostDetailView.as_view(), name='cost-detail'),
    path('cost/<int:pk>/update/', CostUpdateView.as_view(), name='cost-update'),
    path('cost/<int:pk>/delete/', CostDeleteView.as_view(), name='cost-delete'),
    path('cost/new/', CostCreateView.as_view(), name='cost-create'),
    path('about/', views.about, name='tracker-about'),
]

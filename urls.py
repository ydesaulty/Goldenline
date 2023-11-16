urlpatterns = [
    path('admin/', admin.site.urls),
    path('collecte/<int:id>/', views.graphique, name='graphique'),
    path('collecte/', include('collecte.urls')),
    re_path(r'^([0-9]+)/$', views.best),
]

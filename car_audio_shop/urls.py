from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('invoice-generator/', include('invoice_generator.urls', namespace='invoice_generator')),
    # Add more app-specific URL patterns here.
]

# Add URL patterns for any other apps you have in your project.
# For example, if you have another app named 'my_app', include its URL patterns like this:
# path('my-app/', include('my_app.urls', namespace='my_app'))

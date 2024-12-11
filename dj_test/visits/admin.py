from django.contrib import admin
from .models import Visit

# Register your models here.
@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "page",
        "username",
        "timestamp"
    ]
    search_fields = ["username", "page"]
    readonly_fields = ["timestamp"]
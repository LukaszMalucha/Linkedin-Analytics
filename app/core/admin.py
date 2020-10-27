from django.contrib import admin

from core import models


class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    search_fields = ['name', ]

    class Meta:
        model = models.Company

    list_filter = (
        'group',
    )

admin.site.register(models.Company, CompanyModelAdmin)

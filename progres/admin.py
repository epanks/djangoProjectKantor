from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Wilayah, Balai, Satker, Ppk, Paket, Progres, Kodeoutput, Satoutput, Lampiran, Satoutcome, Ks, \
    Sistem, Sycmyc, Ta, Tag
from .forms import SatkerCreateForm


class SatkerCreateAdmin(admin.ModelAdmin):
    list_display = ['kdsatker', 'nmsatker', 'phone', 'balai', 'wilayah']
    form = SatkerCreateForm
    list_filter = ['balai']
    search_fields = ['balai', 'nmsatker']


# Register your models here.
admin.site.register(Wilayah, ImportExportModelAdmin)
admin.site.register(Balai, ImportExportModelAdmin)
# admin.site.register(Satker, ImportExportModelAdmin)
admin.site.register(Satker, SatkerCreateAdmin)
admin.site.register(Tag)
admin.site.register(Ppk)
admin.site.register(Paket, ImportExportModelAdmin)
admin.site.register(Kodeoutput)
admin.site.register(Satoutput)
admin.site.register(Satoutcome)
admin.site.register(Sistem, ImportExportModelAdmin)
admin.site.register(Sycmyc)
admin.site.register(Ks)
admin.site.register(Ta)

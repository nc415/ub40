from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from repo.models import Company, BU, Year, PLstandard, PLtype


# Register your models here.
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
	list_display=('Company_Name',)
class BUAdmin(admin.ModelAdmin):
	list_display=('BU_Name',)
class YearAdmin(admin.ModelAdmin):
	list_display=('Year',)
class PLtypeAdmin(admin.ModelAdmin):
	list_display=('element',)
class PLstandardAdmin(admin.ModelAdmin):
	list_display=('BU', 'PLtype', 'Year', 'TotalRevenue',)

	#code to prepopulate the slug field when you type in a new category name
admin.site.register(Company, CompanyAdmin)
admin.site.register(BU, BUAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(PLtype, PLtypeAdmin)
admin.site.register(PLstandard, PLstandardAdmin)

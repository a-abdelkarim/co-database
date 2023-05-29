from django.contrib import admin
from .models import Company, Category, SubCategory

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'activity', 'category', 'created_by', 'created_at')
    list_filter = ('category', 'created_by', 'created_at')
    search_fields = ('name', 'activity', 'category__name', 'created_by__email')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, CategoryAdmin)
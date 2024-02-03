from django.contrib import admin
from .models import Product, Category, Allergen, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'price', 'rating', 'image', 'get_allergens')
    list_filter = ('category', 'rating')
    search_fields = ('name', 'description', 'category__name')

    def get_allergens(self, obj):
        return ", ".join([allergen.name for allergen in obj.allergens.all()])

    get_allergens.short_description = 'Allergens'

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')
    search_fields = ('name', 'friendly_name')


class AllergenAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    search_fields = ('product__name', 'user__username', 'rating')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Allergen, AllergenAdmin)
admin.site.register(Review, ReviewAdmin)

from django.contrib import admin
from phones.models import Phone, Review


# Register your models here.

# inline the reviews
class ReviewInline(admin.TabularInline):
	model = Review
	extra = 2

# Phone edit form
class PhoneAdmin(admin.ModelAdmin):
	list_display = ('model_number','manufacturer', 'system', 'processor')
	inlines = [ReviewInline]
	
# register the phone edit form
admin.site.register(Phone, PhoneAdmin)

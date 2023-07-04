from django.contrib import admin
from .models import Course, TeachRequest, Post

# Register your models here.
admin.site.register(Course)
admin.site.register(TeachRequest)
# admin.site.register(Post) 

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only assign user if the object is being created
            obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
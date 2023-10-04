from django.contrib import admin
from .models import Category,Post,Updates,Teachers,Uploads


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields= ('title',)
    
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content',)
    search_fields = ('title',)
    list_filter=  ('cat',)
    list_per_page=50


class UpdatesAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag','description','add_date')
    search_fields= ('title',)
    
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name','image_tag','role','phone_number','email')
    search_fields = ('name','role')
    
class UploadAdmin(admin.ModelAdmin):
    list_display = ('name','standard','roll_no','subject')
    search_fields = ('standard','subject')
    list_filter = ('standard','subject')
    

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Updates,UpdatesAdmin)
admin.site.register(Teachers,TeacherAdmin)
admin.site.register(Uploads,UploadAdmin)
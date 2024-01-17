from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from .models import Fillial, Advantages, Learners_count, CategoryCourse, Course, CategoryContent, Content, Teacher, About, Students

def thumbnail(image_field):
    if image_field:
        return mark_safe(f'<img src="{image_field.url}" width="50" height="50" />')
    return ""

@admin.register(Fillial)
class FillialAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Advantages)
class AdvantagesAdmin(admin.ModelAdmin):
    list_display = ['advantage', 'content']
    search_fields = ['advantage', 'content']

@admin.register(Learners_count)
class LearnersCountAdmin(admin.ModelAdmin):
    list_display = ['type', 'count']
    search_fields = ['type']

@admin.register(CategoryCourse)
class CategoryCourseAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'about', 'price', 'category', 'image_thumbnail']
    list_filter = ['category']
    search_fields = ['name', 'about']
    readonly_fields = ['img_webp', 'image_thumbnail']

    def image_thumbnail(self, obj):
        return thumbnail(obj.image)
    image_thumbnail.short_description = _('Rasm')

@admin.register(CategoryContent)
class CategoryContentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'fillial', 'category', 'image_thumbnail']
    list_filter = ['date', 'fillial', 'category']
    search_fields = ['title', 'content']
    readonly_fields = ['img_webp', 'image_thumbnail']

    def image_thumbnail(self, obj):
        return thumbnail(obj.image)
    image_thumbnail.short_description = _('Rasm')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'facebook', 'linkedin', 'telegram', 'filial', 'image_thumbnail']
    list_filter = ['filial']
    search_fields = ['name', 'about']
    readonly_fields = ['img_webp', 'image_thumbnail']

    def image_thumbnail(self, obj):
        return thumbnail(obj.image)
    image_thumbnail.short_description = _('Rasm')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['welcome', 'content']

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'active']
    list_filter = ['active', "filliallar"]
    search_fields = ['name', 'surname', 'phone']
    filter_horizontal = ['courses', 'teachers']

    
# Additional customizations and translations as needed

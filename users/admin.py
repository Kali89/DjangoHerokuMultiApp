from django.contrib import admin
from users.models import User, Post


class PostInLine(admin.StackedInline):
    model = Post
    extra = 5

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['title']}),
        ('Date information, {'fields: ['created'], 'classes': ['collapse']}),
    ]
    inlines = [PostInLine]

admin.site.register(User, UserAdmin)

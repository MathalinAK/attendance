from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import members
class membersAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')  
    search_fields = ('username', 'email')  
    readonly_fields = ('date_joined', 'last_login')  

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    actions = ['delete_selected'] 


    def delete_selected(self, request, queryset):
        count = queryset.count()
        queryset.delete()  
        self.message_user(request, f'Deleted {count} user(s) successfully.')

    delete_selected.short_description = "Delete selected users"  
admin.site.register(members, membersAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class UserAdmin(DefaultUserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'is_admin')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff','is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    list_display = ('username','email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username','email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(get_user_model(), UserAdmin)
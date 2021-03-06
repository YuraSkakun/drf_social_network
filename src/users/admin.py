from django.contrib import admin
from users.models import UserProfile, UserAddress, UserPhone


class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)


class UserAddressAdmin(admin.ModelAdmin):
    raw_id_fields = ('user_profile',)


class UserPhoneAdmin(admin.ModelAdmin):
    raw_id_fields = ('user_profile',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(UserPhone, UserPhoneAdmin)

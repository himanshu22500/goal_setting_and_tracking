from django.contrib import admin

from accounts.models.user_profile import SessionToken, UserProfile

admin.site.register(UserProfile)
admin.site.register(SessionToken)

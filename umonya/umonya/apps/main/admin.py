from django.contrib import admin
from models import Announcement, About

#~ Ensuring that admin is aware of this class
admin.site.register(Announcement)
admin.site.register(About)

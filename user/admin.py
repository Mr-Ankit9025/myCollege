from django.contrib import admin
from .models import *

class contactInfoAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Mobile','Msg')

admin.site.register(contactInfo,contactInfoAdmin)


######################################
class ugalleryAdmin(admin.ModelAdmin):
    list_display = ('id','gdes','picture')
admin.site.register(ugallery,ugalleryAdmin)
# register your models here.

##############################################
class stuplacementAdmin(admin.ModelAdmin):
    list_display = ('id','name','course','branch','stupic','designation','syear','cpic','rdate','cname','pcity')
admin.site.register(stuplacement,stuplacementAdmin)

###############(admin model)##########
class sturegisterAdmin(admin.ModelAdmin):
    list_display = ('rno','name','course','email','smobile','gmobile','pic','rdate',)

admin.site.register(sturegister,sturegisterAdmin)

##################Placement#######################
class cityAdmin(admin.ModelAdmin):
    list_display = ('id','cname','cdate')

admin.site.register(city,cityAdmin)


class companyAdmin(admin.ModelAdmin):
    list_display = ('id', 'cname', 'clogo')


admin.site.register(company, companyAdmin)

###################################################

class vgalleryAdmin(admin.ModelAdmin):
    list_display = ('id','vlink','vdes','vtitle','vdate')

admin.site.register(vgallery,vgalleryAdmin)

######################################
class mycourseAdmin(admin.ModelAdmin):
    list_display = ('id','cname','branch','seats','hod','duration','cpic','sdate','eligibilty','fee','hodpic',)

admin.site.register(mycourse,mycourseAdmin)

###########################################
class infrastructureAdmin(admin.ModelAdmin):
    list_display = ('iname','ipic')

admin.site.register(infrastructure,infrastructureAdmin)


###############################################
class teacherAdmin(admin.ModelAdmin):
    list_display = ('tname','tbranch','tpic')
admin.site.register(teacher,teacherAdmin)
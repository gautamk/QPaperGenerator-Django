from django.conf.urls.defaults import *
from QPaperGenerator import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^QuestionPaperFrom/', 'QPaperGenerator.QP.views.GenerateQuestionPaperGetDetails'),
    (r'^GenerateQPaper/','QPaperGenerator.QP.views.GenerateQuestionPaperFromDetails'),
    # Example:
    # (r'^QPaperGenerator/', include('QPaperGenerator.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$','QPaperGenerator.QP.views.root'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': '/home/gautam/Aptana Studio 3 Workspace/QPaperGenerator-Django/QPaperGenerator/media', 'show_indexes': True}),

)
#if settings.DEBUG:
#        urlpatterns += patterns('',
#                
#        )

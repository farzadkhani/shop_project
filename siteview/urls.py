from django.urls import path
from . import views as siteview_views
from django.conf import settings
from django.conf.urls.static import static
#from . import api
#from mysite.urls import router



#router.register(r'posts', api.PostViewSet)

urlpatterns = [
    path('', siteview_views.HomeView.as_view(), name='home'),
    #path('like_comment/<slug:post_pk>/', blog_views.like_comment, name='like_comment'),
    #path('post/<slug:slug>/', blog_views.PostDetail.as_view(), name='post_detail'),
    #path('json/comments/',api.comment_list, name='comment_list_api'),
    #path('json/posts/<int:pk>',api.PostdetailGeneric.as_view(), name='post_detail_api'),
    #path('json/posts/<int:pk>/',api.PostViewSet.as_view({
    #    'get':'retrieve',
    #    'put':'update',
    #    'delete':'destroy'
    #}), name='post_detail_api'),
        #attention:did not show actions in this type of url,need router




#    path('page/<int:pageno>', views.PostList.as_view(), name='PostList'),  #for paginator
#    path(r'^$', PostList.as_view(), name='file-exam-view'), 'page/<int:pageno>/', views.index, name='index'    #for pageinator
#    path('articles/2003/',views.special_case_2003),
#    path('articles/<int:year>/',views.year_archive),
#    path('articles/<int:year>/<int:month>/,views.month_archive);
#    path('articles/<int:year>/<int:month>/<slug:slug>/',views.articles_detail),
]
#urlpatterns = format_suffix_patterns(urlpatterns)



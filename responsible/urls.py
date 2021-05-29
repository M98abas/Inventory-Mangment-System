# I do the same here to made the app more dynamiclly 
from django.urls        import path
from responsible.views  import PdfRnader,respon_post_create,res_post_list,res_post_update,res_post_delete,showresp

urlpatterns = [
    path('new/response/',respon_post_create,name='addnewrespon'),
    path('response/<int:id>/delete/',res_post_delete,name='deleterespon'),
    path('response/<int:id>/update/',res_post_update,name='updaterespon'),
    path('response/<int:id>',showresp,name='showrespon'),
    path('response/list/',res_post_list,name='listresp'),
    path('response/list/pdf',PdfRnader.as_view(),name='listresppdf'),

]
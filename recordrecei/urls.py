# In this file i made it to put all urls inside it and call file from the main file 


from django.urls        import path
from recordrecei.views  import item_post_create,item_post_list,item_post_update,item_post_delete,showitem,PdfRnader

urlpatterns = [
	path('AddItem/',item_post_create,name='addnew'),
	path('report/',item_post_list,name='report'),
	path('report/pdf',PdfRnader.as_view(),name='reportpdf'),
	path('report/<int:id>',showitem,name='showitem'),
	path('report/<int:id>/edit',item_post_update,name='update'),
	path('report/<int:id>/delete',item_post_delete,name='delete'),

]
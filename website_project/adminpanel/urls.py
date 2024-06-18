from django.urls import path
from adminpanel import views

urlpatterns =[
    path('adminpanel',views.index,name='admin'),
    path('login',views.login_page,name='login_page'),
    path('reg',views.reg_page,name='reg_page'),
    path('logout_user',views.logout_page,name='logout_user'),
    path('change_password',views.change_pass,name='change_password'), 

    path('story_pic',views.Story_img,name='story_pic'),
    path('story',views.our_story1,name='story'),
    path('mission',views.our_mission1,name='mission'),
    path('donation',views.donation_founded,name='donation'),
    path('founded',views.founded_partn,name='founded'),
    path('volunteer',views.vel_donation,name='volunteer'),
    path('casuse_vlo',views.casuse_dese,name='casuse_vlo'),
    path('casuse_hed',views.casuse_head,name='casuse_hed'),

    path('add_slider',views.create_slider,name='add_slider'),
    path('slider_info_edit/<int:id>',views.edit_slider,name='slider_info_edit'),
    path('update_slider/<int:id>',views.update_slider,name='update_slider'),
    path('slider_delete/<int:id>',views.delete_slider,name='slider_delete'),
    path('trush',views.trush_slider,name='trush'),
    path('restore/<int:id>',views.restore_slider,name='restore'),
    path('delete_all',views.delete_all,name='delete_all'),
    path('del_permanent/<int:id>',views.del_permanent,name='del_permanent'),
    # path('del_forever/<int:id>',views.del_forever,name='del_forever'),

    path('welcome_text',views.create_welcome,name='welcome_text'),
    path('welcome_edit/<int:id>',views.edit_welcome,name='welcome_edit'),
    path('welcome_update/<int:id>',views.update_welcome_text,name='welcome_update'),
    path('welcome_del/<int:id>',views.delete_welcome,name='welcome_del'),
    path('welcome_trush',views.trush_welcome,name='welcome_trush'),
    path('welcome_restore/<int:id>',views.restore_welcome,name='welcome_restore'),
    path('del_chcckbox_wel',views.delete_wel_all,name='del_chcckbox_wel'),
    path('parmanent_del_welcome/<int:id>',views.del_wel_permanent,name='parmanent_del_welcome'),

    path('welcome_img01',views.welcome_img,name='welcome_image'),
    path('welcome_img_edit/<int:id>',views.welcome_img_edit,name='welcome_img_edit'),
    path('update_img_wel/<int:id>',views.update_img_welcome,name='update_img_wel'),
    path('delete_wel_img/<int:id>',views.delete_wel_img,name='delete_wel_img'),
    path('wel_img_trush',views.wel_img_trush,name='wel_img_trush'),
    path('welcome_img_restore/<int:id>',views.restore_welcome_img,name='welcome_img_restore'),
    path('del_chcckboximg_wel',views.delete_welimg_all,name='del_chcckboximg_wel'),
    path('parmanent_delimg_welcome/<int:id>',views.del_welimg_permanent,name='parmanent_delimg_welcome'),
    path('about_volun',views.about_volunteer,name='about_volun'),

    




    
]

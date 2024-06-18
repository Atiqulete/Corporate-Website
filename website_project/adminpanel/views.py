from django.shortcuts import render,redirect,HttpResponse
from adminpanel.models import User,slider,welcome,image_01,usertype,story_image,our_story,our_mission,founder_donation,founding_par,volinteer_donation,casuse,casuse_headline,volunteer_about
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
import sweetify

def index(request):
    if request.user.is_authenticated:
        return render(request,'adminpanel/index.html')
    else:
        return redirect('login_page')

def reg_page(request):
    if request.user.is_authenticated:
        user_type = usertype.objects.all()
        if request.method == 'POST':
            user_name = request.POST.get('name')
            email = request.POST.get('email')
            password_1 = request.POST.get('password')
            password_2 = request.POST.get('password_2')
            user_type = request.POST.get('user_type')
            if password_1 != password_2:
                return redirect('reg_page')
            else:
                user_reg = User.objects.create_user(user_name,email,password_1)
                # user_reg.last_name = 'Islam'
                user_reg.user_type_id = user_type
                user_reg.save()
                return redirect('login_page')
    else:
        return redirect('login_page')
    return render(request, 'adminpanel/reg_2.html',{'user_type':user_type})

def login_page(request):
    if request.method == 'POST':
         a = request.POST.get('name')
         b = request.POST.get('password')
         user = authenticate(username=a,password=b)
         user_type_check = User.objects.get(username = user)
         if user != None:    
            #  if request.user.user_type == 2:
            #  if User.objects.get(user_type_id = 1):
            #  if user_type_check.user_type.type_name =='Normal User':
             if user_type_check.user_type.type_name =='Admin':
                login(request,user)
                #  return HttpResponse('welcome To My Admin Palnel')
                return render(request,'adminpanel/index.html')
         else:
             return redirect('login_page')
    return render(request, 'adminpanel/login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')

def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            old_pass = request.POST.get('old_pass')
            new_pass = request.POST.get('new_pass')
            confirm_pass = request.POST.get('confirm_pass')
            xyz = User.objects.get(id=request.user.id)
            if xyz.check_password(old_pass) and new_pass == confirm_pass:
                xyz.set_password(new_pass)
                xyz.save()
                update_session_auth_hash(request,xyz)
                return redirect('logout_user')
        return render(request,'adminpanel/change_pass.html')
    else:
        return redirect('login_page')

def create_slider(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            slider_title = request.POST.get('slider_title')
            slider_desc = request.POST.get('slider_desc')
            slider_img = request.FILES['slider_img']
            slider_save = slider(
                slider_title = slider_title,
                slider_description = slider_desc,
                slider_image = slider_img
            )
            slider_save.save()
            # sweetify.success(request, 'You did it', text='Your Form has been Updated',persistent='Hell yeah')
            sweetify.toast(request,'save')
        slider_show = slider.objects.filter(is_delete = 0)
        # user_tabel = User.objects.all()
        # user_tabel = User.objects.filter(is_superuser = 1)
        user_tabel = User.objects.filter(is_superuser = 0)          
        return render(request,'adminpanel/slider/add_slider.html',{'slider_show':slider_show, 'user_tabel':user_tabel})
    else:  
        return redirect('add_slider')

def edit_slider(request,id):
    if request.user.is_authenticated:
        edit_info = slider.objects.filter(id=id)
        return render(request,'adminpanel/slider/edit_slider.html',{'edit_info':edit_info})
    else:
        return redirect('add_slider')
    
def update_slider(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            slider_title = request.POST.get('slider_title')
            slider_desc = request.POST.get('slider_desc')
            slider_img = request.FILES['slider_img']

            slider_store = slider.objects.filter(id=id)
            slider_store = slider(
                id=id,
                slider_title = slider_title,
                slider_description =slider_desc,
                slider_image = slider_img
            )
            slider_store.save()
        else:
            slider_title = request.POST.get('slider_title')
            slider_desc = request.POST.get('slider_desc')
            slider_img = request.POST.get('slider_img_1')

            slider_store = slider.objects.filter(id=id)
            slider_store = slider(
                id=id,
                slider_title = slider_title,
                slider_description =slider_desc,
                slider_image = slider_img
            )
            slider_store.save()
        return render(request,'adminpanel/slider/add_slider.html')
    else:
        return redirect('add_slider')

# def delete_slider(request,id):
#     slider_del = slider.objects.filter(id=id)
#     slider_del.delete()
#     return redirect('add_slider')

def delete_slider(request,id):
    slider_del = slider.objects.get(id=id)
    slider_del.is_delete = True
    slider_del.save()
    return redirect('add_slider')

def trush_slider(request):
    if request.user.is_authenticated:
        slider_show = slider.objects.filter(is_delete = 1)       
        return render(request,'adminpanel/slider/trush.html',{'slider_show':slider_show})
    else:
        return redirect('add_slider')

def restore_slider(request,id):
    slider_del = slider.objects.get(id=id)
    slider_del.is_delete = False
    slider_del.save()
    return redirect('trush')

def delete_all(request):
    del_sli = request.POST.getlist('slider_del')

    for i in del_sli:
        slider_all_del = slider(
            id = i 
        )
        slider_all_del.delete()
    return redirect('trush')
        
def del_permanent(request,id):
    parmanent_del_trush = slider.objects.get(id=id)
    parmanent_del_trush.delete()
    return redirect('trush')

# def del_forever(request,id):
#     del_final = slider.objects.get(id=id)
#     return render(request,'adminpanel/slider/del_forever.html',{'del_final':del_final})

def create_welcome(request): 
    if request.user.is_authenticated:
        if request.method == 'POST':
            welcome_title = request.POST.get('welcome_title')
            welcome_save = welcome(
                welcome_title = welcome_title
            )
            welcome_save.save()
        welcome_show = welcome.objects.filter(is_delete=0)
        return render(request,'adminpanel/welcome/welcome.html',{'welcome_show':welcome_show})
    else:
        return redirect('login_page')
    
def edit_welcome(request,id):
    if request.user.is_authenticated:
        edit_wel_info = welcome.objects.filter(id=id)
        return render(request,'adminpanel/welcome/edit_welcome.html',{'edit_wel_info':edit_wel_info})
    else:
        return redirect('welcome_text')
    
def update_welcome_text(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            welcome_update = request.POST.get('welcome_title')
            welcome_save = welcome.objects.filter(id=id)
            welcome_save = welcome(
                id=id,
                welcome_title = welcome_update,
            )
            welcome_save.save()       
        return render(request,'adminpanel/welcome/welcome.html')
    else:
        return redirect('welcome_text')

# def delete_welcome(request,id):
#     welcome_del = welcome.objects.filter(id=id)
#     welcome_del.delete()
#     return redirect('welcome_text')

def delete_welcome(request,id):
    welcome_del = welcome.objects.get(id=id)
    welcome_del.is_delete = True
    welcome_del.save()
    return redirect('welcome_text')

def trush_welcome(request):
    if request.user.is_authenticated:
        welcome_show = welcome.objects.filter(is_delete = 1)       
        return render(request,'adminpanel/welcome/trush.html',{'welcome_show':welcome_show})
    else:
        return redirect('welcome_text')

def restore_welcome(request,id):
    welcome_del = welcome.objects.get(id=id)
    welcome_del.is_delete = False
    welcome_del.save()
    return redirect('welcome_trush')

def delete_wel_all(request):
    del_wel_all = request.POST.getlist('welcome_del_checkbox')

    for i in del_wel_all:
        del_wel_all = welcome(
            id = i 
        )
        del_wel_all.delete()
    return redirect('welcome_trush')

def del_wel_permanent(request,id):
    parmanent_del_wel = welcome.objects.get(id=id)
    parmanent_del_wel.delete()
    return redirect('welcome_trush')

def welcome_img(request):
    if request.user.is_authenticated:
        if request.method == 'POST'and request.FILES:
            image_text1 = request.POST.get('image_text1')
            image_text2 = request.POST.get('image_text2')
            image_welcome = request.FILES['image_welcome']
            welcome_image_save = image_01(
                image_text1 = image_text1,
                image_text2 = image_text2,
                image_welcome = image_welcome
            )
            welcome_image_save.save()
        welcome_images = image_01.objects.filter(is_delete=0)
        return render(request,'adminpanel/welcome/wecomel_image.html',{'welcome_images':welcome_images })
    else:
        return redirect('login_page')

def welcome_img_edit(request,id):
    if request.user.is_authenticated:
        wel_img_edit = image_01.objects.filter(id=id)
        return render(request,'adminpanel/welcome/edit_welcome_image.html',{'wel_img_edit':wel_img_edit})
    else:
        return redirect('welcome_image')
    
def update_img_welcome(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            wel_img_title = request.POST.get('image_text1')
            wel_img_desc = request.POST.get('image_text2')
            wel_img_edit = request.FILES['image_welcome']

            wel_img_store = image_01.objects.filter(id=id)
            wel_img_store = image_01(
                id=id,
                image_text1 = wel_img_title,
                image_text2 = wel_img_desc,
                image_welcome = wel_img_edit
            )
            wel_img_store.save()
        else:
            wel_img_title = request.POST.get('image_text1')
            wel_img_desc = request.POST.get('image_text2')
            wel_img_edit = request.POST.get('image_welcome_1')

            wel_img_store = image_01.objects.filter(id=id)
            wel_img_store = image_01(
                id=id,
                image_text1 = wel_img_title,
                image_text2 = wel_img_desc,
                image_welcome = wel_img_edit
            )
            wel_img_store.save()   
        return render(request,'adminpanel/welcome/wecomel_image.html')
    else:
        return redirect('welcome_image')

# def delete_wel_img(request,id):
#     wecome_del_img = image_01.objects.filter(id=id)
#     wecome_del_img.delete()
#     return redirect('welcome_image')

def delete_wel_img(request,id):
    welcome_del = image_01.objects.get(id=id)
    welcome_del.is_delete = True
    welcome_del.save()
    return redirect('welcome_image')

def wel_img_trush(request):
    if request.user.is_authenticated:
        welcome_images = image_01.objects.filter(is_delete = 1)       
        return render(request,'adminpanel/welcome/welcome_img_trush.html',{'welcome_images':welcome_images})
    else:
        return redirect('wel_img_trush')
    
def restore_welcome_img(request,id):
    welcome_del_img = image_01.objects.get(id=id)
    welcome_del_img.is_delete = False
    welcome_del_img.save()
    return redirect('wel_img_trush')

def delete_welimg_all(request):
    del_welimg_all = request.POST.getlist('welcome_delimg_checkbox')

    for i in del_welimg_all:
        del_welimg_all = image_01(
            id = i 
        )
        del_welimg_all.delete()
    return redirect('wel_img_trush')

def del_welimg_permanent(request,id):
    parmanent_del_welimg = image_01.objects.get(id=id)
    parmanent_del_welimg.delete()
    return redirect('wel_img_trush')

def Story_img(request):
    if request.user.is_authenticated:
        if request.method == 'POST'and request.FILES:
            image_up = request.FILES['story_pic_upload']
            image_up_save = story_image(
               story_img = image_up
            )
            image_up_save.save()
        up_images_show = story_image.objects.all()
        return render(request,'adminpanel/story_mission/image.html',{'up_images_show':up_images_show})
    else:
        return redirect('login_page')

def our_story1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            story_hed = request.POST.get('story_headline')
            story_title = request.POST.get('story_tit')
            story_dese = request.POST.get('story_desc')

            story_save = our_story(
                story_headline = story_hed,
                story_title = story_title,
                story_description = story_dese
            )
            story_save.save()
        story_show = our_story.objects.all()
        return render(request,'adminpanel/story_mission/story_desc.html',{'story_show':story_show})
    else:
        return redirect('login_page')

def our_mission1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mission_hed = request.POST.get('mission_hed')
            mission_tit = request.POST.get('mission_tit')
            mission_theme = request.POST.get('mission_theme')
            mission_semantic = request.POST.get('mission_semantic')

            mission_save = our_mission(
                mission_title = mission_hed,
                mission_description = mission_tit,
                mission_theme = mission_theme,
                mission_semantic = mission_semantic
            )
            mission_save.save()
        mission_show = our_mission.objects.all()
        return render(request,'adminpanel/story_mission/our_mission.html',{'mission_show':mission_show })
    else:
        return redirect('login_page')

def donation_founded(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            number_tit = request.POST.get('number_hed')
            fou_tit = request.POST.get('founded_tit')
            view_tit = request.POST.get('view_title')
            don_tit = request.POST.get('donation_title')

            donation_save = founder_donation(
                number_title = number_tit,
                founded_title = fou_tit,
                founded_reg = view_tit,
                donation_title = don_tit 
            )
            donation_save.save()
        donation_show = founder_donation.objects.all()
        return render(request,'adminpanel/story_mission/donation.html',{'donation_show':donation_show})
    else:
        return redirect('login_page')
        
def founded_partn(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            image_fonu = request.FILES['founded_img']
            founded_title = request.POST.get('founded_title')
            founded_deg = request.POST.get('founded_deg')
            founded_info1 = request.POST.get('founded_info1')
            founded_info2 = request.POST.get('founded_info2')
            founded_twiter = request.POST.get('founded_twiter')
            founded_fb = request.POST.get('founded_fb')
            founded_ins = request.POST.get('founded_ins')

            founded_save = founding_par(
                founding_image = image_fonu,
                name_founding = founded_title,
                designation_founding = founded_deg,
                founding_info1 = founded_info1,
                founding_info2 = founded_info2,
                twiter_link = founded_twiter,
                facebook_link =founded_fb,
                instagram_link = founded_ins
            )
            founded_save.save()
        founded_show = founding_par.objects.all()
        return render(request,'adminpanel/founded/founded.html',{'founded_show':founded_show})
    else:
        return redirect('login_page')
    
def vel_donation(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            impact_title1 = request.POST.get('impact_title')
            live_title1 = request.POST.get('live_title')
            donation_title1 = request.POST.get('dontions_title')
            volunteer_title1 = request.POST.get('volunteer_title')

            vel_save = volinteer_donation(
                impact_title = impact_title1,
                save_live = live_title1,
                make_donation = donation_title1,
                be_volunteer = volunteer_title1
            )
            vel_save.save()
        vel_show = volinteer_donation.objects.all()
        return render(request,'adminpanel/volunteer/volunteer_donation.html',{'vel_show':vel_show})
    else:
        return redirect('login_page')

def casuse_dese(request):
    if request.user.is_authenticated:
        if request.method == 'POST'and request.FILES:

            cas_tit = request.POST.get('casuse_title')
            cas_desc = request.POST.get('casuse_desc')
            cas_rais = request.POST.get('casuse_raised1')
            rais_amo = request.POST.get('raised_amount1')
            cas_goal = request.POST.get('casuse_goal1')
            goal_amo = request.POST.get('goal_amount1')
            cas_img = request.FILES['casuse_image']
            cas_link = request.POST.get('casuse_link')
            casuse_save = casuse(
 
                casuse_image = cas_img,
                casuse_title = cas_tit,
                casuse_description = cas_desc,
                casuse_raised = cas_rais,
                raised_amount = rais_amo,
                casuse_goal = cas_goal,
                goal_amount = goal_amo,
                casuse_link = cas_link
            )
            casuse_save.save()
        casuse_show = casuse.objects.all()
        return render(request,'adminpanel/casuse/casuse.html',{'casuse_show':casuse_show })
    else:
        return redirect('login_page')
    
def casuse_head(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cas_hedline = request.POST.get('casuse_head')

            casuse_hed_save = casuse_headline(
                casuse_hed = cas_hedline
            )
            casuse_hed_save.save()
        casuse_hed_show = casuse_headline.objects.all()
        return render(request,'adminpanel/casuse/casuse_hed.html',{'casuse_hed_show':casuse_hed_show })
    else:
        return redirect('login_page')
    
def about_volunteer(request):
    if request.user.is_authenticated:
        if request.method == 'POST'and request.FILES:
            abu_tit = request.POST.get('about_title')
            abu_des = request.POST.get('about_desc')
            image_abu = request.FILES['about_img']
            image_abu_save = volunteer_about(
               about_tit = abu_tit,
               about_desc = abu_des,
               about_image =image_abu
            )
            image_abu_save.save()
        abu_images_show =volunteer_about.objects.all()
        return render(request,'adminpanel/about_volunteer/about_volunteer.html',{'abu_images_show':abu_images_show})
    else:
        return redirect('login_page')

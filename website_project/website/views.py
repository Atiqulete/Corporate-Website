from django.shortcuts import render,redirect
from adminpanel.models import slider,welcome,image_01,story_image,our_story,our_mission,founder_donation,founding_par,volinteer_donation,casuse,casuse_headline,volunteer_about
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    slider_info = slider.objects.all()
    welcome_text = welcome.objects.all()
    welcome_image = image_01.objects.all()
    story_up_img = story_image.objects.all()
    story_info = our_story.objects.all()
    mission_info = our_mission.objects.all()
    donation_info = founder_donation.objects.all()
    founding_info = founding_par.objects.all()
    volinteer_info = volinteer_donation.objects.all()
    causes_info = casuse.objects.all()
    causes_head = casuse_headline.objects.all()
    about_volun = volunteer_about.objects.all()

    

    context = {
        'slider_info': slider_info,
        'welcome_text': welcome_text,
        'welcome_image': welcome_image,
        'story_up_img':story_up_img,
        'story_info':story_info,
        'mission_info':mission_info,
        'donation_info':donation_info,
        'founding_info':founding_info,
        'volinteer_info':volinteer_info,
        'causes_info':causes_info,
        'causes_head':causes_head,
        'about_volun':about_volun
        
    }
    return render(request,'website/index.html',context)

def volunteer_Email(request):
    if request.method == 'POST':
        name = request.POST.get('volunteer_name')
        email = request.POST.get('volunteer_email')
        subject = request.POST.get('volunteer_subject')
        message = request.POST.get('volunteer_message')
        final_massage = message + ' '+ name + ' ' +email
        from_email = settings.EMAIL_HOST_USER
        to_email = ['atiqulete@gmail.com','atiqul736@gmail.com']
        send_mail(subject,final_massage,from_email,to_email)
        return redirect('home')


   
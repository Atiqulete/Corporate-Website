from django.db import models

# from django.contrib.auth import get_user_model
# User = get_user_model()

from django.contrib.auth.models import AbstractUser



class usertype(models.Model):
    type_name = models.CharField(max_length=200)

class User(AbstractUser):
    user_type = models.ForeignKey(usertype,on_delete=models.CASCADE,default = 1)

class slider(models.Model):
    slider_title = models.CharField(max_length=200)
    slider_description = models.CharField(max_length=200)
    slider_image  = models.ImageField(upload_to='slider/', blank= True,null=True)
    is_delete = models.BooleanField(default=False)

class welcome(models.Model):
    welcome_title = models.CharField(max_length=200)
    is_delete = models.BooleanField(default=False)

class image_01(models.Model):
    image_text1 = models.CharField(max_length=200)
    image_text2 = models.CharField(max_length=200)
    image_welcome  = models.ImageField(upload_to='welcome_image/', blank= True,null=True)
    is_delete = models.BooleanField(default=False)

class story_image(models.Model):
    story_img  = models.ImageField(upload_to='story_img/', blank= True,null=True)

class our_story(models.Model):
    story_headline = models.CharField(max_length=200)
    story_title = models.CharField(max_length=200)
    story_description = models.CharField(max_length=1000)

class our_mission(models.Model):
    mission_title = models.CharField(max_length=200)
    mission_description = models.CharField(max_length=200)
    mission_theme = models.CharField(max_length=200)
    mission_semantic = models.CharField(max_length=200)

class founder_donation(models.Model):
    number_title = models.IntegerField()
    founded_title = models.CharField(max_length=200)
    founded_reg = models.CharField(max_length=200)
    donation_title = models.CharField(max_length=200)

class founding_par(models.Model):
    founding_image = models.ImageField(upload_to='founding_partner/', blank= True,null=True)
    name_founding= models.CharField(max_length=200)
    designation_founding= models.CharField(max_length=200)
    founding_info1 = models.CharField(max_length=1000)
    founding_info2 = models.CharField(max_length=1000)
    twiter_link = models.CharField(max_length=500)
    facebook_link = models.CharField(max_length=500)
    instagram_link = models.CharField(max_length=500)

class volinteer_donation(models.Model):
    impact_title = models.CharField(max_length=200)
    save_live = models.CharField(max_length=200)
    make_donation = models.CharField(max_length=200)
    be_volunteer = models.CharField(max_length=200)

class casuse_headline(models.Model):
    casuse_hed = models.CharField(max_length=200)

class casuse(models.Model):
    casuse_title = models.CharField(max_length=200)
    casuse_description = models.CharField(max_length=1000)
    casuse_raised = models.CharField(max_length=200)
    raised_amount = models.IntegerField()
    casuse_goal = models.CharField(max_length=200)
    goal_amount = models.IntegerField()
    casuse_link = models.CharField(max_length=200)
    casuse_image = models.ImageField(upload_to='casuse_image/', blank= True,null=True)

class volunteer_about(models.Model):
    about_tit = models.CharField(max_length=200)
    about_desc = models.CharField(max_length=200)
    about_image = models.ImageField(upload_to='casuse_image/', blank= True,null=True)


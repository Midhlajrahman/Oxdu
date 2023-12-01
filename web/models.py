from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(db_index=True,auto_now_add=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=120,blank=True,null=True)
    subject = models.CharField(max_length=120,blank=True,null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.name)


class Course(models.Model):
    duration = models.IntegerField()
    fees = models.IntegerField()
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    slug = models.SlugField(unique=True , max_length=100)
    def __str__(self):
        return self.course_name
    
    
class CourseFeatures(models.Model):
    course=models.ForeignKey("web.Course",on_delete=models.CASCADE,blank=True,null=True)
    course_feature = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return self.course_feature
   

class OurFacualty(models.Model):
    facualty_image = models.FileField(upload_to="media" ,blank=True,null=True)
    facualty_name = models.CharField(max_length=100 , blank=True,null=True)
    facualty_position=models.CharField(max_length=100 , blank=True,null=True)
    instagram=models.URLField(blank=True,null=True)
    linkedin=models.URLField(blank=True,null=True)
    twitter=models.URLField(blank=True,null=True) 
    
    def __str__(self):
        return self.facualty_name
    
class Event(models.Model):
    event_image = models.FileField(upload_to="media")
    event_date = models.IntegerField()
    event_month = models.CharField(max_length=50)
    event_cordinator = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    event_title = models.CharField(max_length=100)
    event_description = models.TextField()
    slug = models.SlugField(unique=True , max_length=100)
    
    def __str__(self):
        return self.event_title
  
class EventPoints(models.Model):
    event=models.ForeignKey("web.Event" , on_delete=models.CASCADE,blank=True,null=True)
    event_points =  models.CharField(max_length=100, blank=True,null=True)

class Faq(models.Model):
    faq_question = models.CharField(max_length=300)
    faq_answer =models.CharField( max_length=300)
    
    def __str__(self):
        return self.faq_question
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial_content = models.CharField(max_length=300)
    position = models.CharField(max_length=200)
   
    def __str__(self):
       return self.name
   

class Register(models.Model):
    full_name =  models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    contact_number =  models.CharField(max_length=50)
    
    def __str__(self):
        return self.full_name
    

class CourseRegistration(models.Model):
    course = models.ForeignKey("web.Course",on_delete=models.CASCADE, blank=True,null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    
    def __str__(self):
        return self.name
    

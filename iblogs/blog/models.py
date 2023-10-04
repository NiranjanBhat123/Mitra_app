from django.db import models
from django.utils.html import format_html


# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True,null=True)
    
    def image_tag(self):
        return format_html('<img src = "/media/{}" style= "width:100px;height:50px;" />'.format(self.pic))
    
    def __str__(self):
        return self.title
    
    
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    
    
    def __str__(self):
        return self.title
    
    


#updates model
class Updates(models.Model):
    update_id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='updates/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    
    def image_tag(self):
        return format_html('<img src = "/media/{}" style= "width:100px;height:50px;" />'.format(self.image))
    
    def __str__(self):
        return self.title
    
class Teachers(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=30,default="assistant teacher")
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    image = models.ImageField(upload_to='teacher_photos')
    url = models.CharField(max_length=100)
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    
    def image_tag(self):
        return format_html('<img src = "/media/{}" style= "width:75px;height:75px;" />'.format(self.image))
    
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.role
    
class Uploads(models.Model):
    upload_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    standard = models.CharField(max_length=25)
    roll_no = models.CharField(max_length=25)
    subject = models.CharField(max_length=25)
    image = models.FileField(upload_to='student_uploads/')
    add_date = models.DateTimeField(auto_now_add=True,null= True)
    
    
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.roll_no
    
    def __str__(self):
        return self.standard
    def __str__(self):
        return self.subject
        
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

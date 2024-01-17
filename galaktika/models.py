from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

        
class Fillial(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ism")
    
    def __str__(self):
        return self.name
    



class Advantages(models.Model):
    
    advantage = models.CharField(max_length=200, verbose_name="ustunlik")
    content = models.CharField(max_length=400, verbose_name="qanday")
    
    def __str__(self):
        return self.advantage
    
    class Meta:
        verbose_name = "ustunlik"
        verbose_name_plural = "ustunlik"
        
    
class Learners_count(models.Model):
    
    
    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistika"
        
    
    type = models.CharField(max_length=50, verbose_name="Turkumi")
    count = models.IntegerField(verbose_name="Soni")
    def __str__(self):
        return self.type
    
  
  
class CategoryCourse(models.Model):
    name  = models.CharField(max_length=200, verbose_name="nomi")
   
    def is_root(self):
        return True if self.parent else False
    
    def __str__(self):
        return self.name


class Course(models.Model):
    
    class Meta:
        verbose_name = "Kurslar"
        verbose_name_plural = "Kurslar"
    
    
    name = models.CharField(max_length=100, verbose_name="Kurs ismi")
    about = models.TextField(max_length=1000, verbose_name='Haqida')
    price = models.FloatField()
    category = models.ForeignKey(CategoryCourse, on_delete=models.SET_NULL, null=True)
    
    
    image = models.ImageField(upload_to="index/courses/img", verbose_name="rasm")
    img_webp = models.ImageField(blank=True, upload_to="index/courses/img_webp")
    
    def get_img(self):
        return self.img_webp.url
    
    def save(self, *args, **kwargs):
        # Convert image to WebP and save
        if self.image:
            # Open the image using Pillow
            pil_image = Image.open(self.image)
            # Convert the image to RGB mode if it's not
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            # Save the image in a BytesIO object
            image_io = BytesIO()
            pil_image.save(image_io, format='WEBP')
            # Create a Django-friendly ContentFile
            webp_image = ContentFile(image_io.getvalue())
            # Save to img_webp field
            self.img_webp.save(f'{self.image.name.split(".")[0]}.webp', webp_image, save=False)

        super().save(*args, **kwargs)
    def __str__(self):
        return self.name




class CategoryContent(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name



class Content(models.Model):
    
    
    def get_img(self):
        return self.img_webp.url
    
    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Content"
    
    fillial = models.ForeignKey(Fillial,null=True, on_delete=models.SET_NULL,verbose_name='fillial')
 
    category = models.ForeignKey(CategoryContent,null=True, on_delete=models.SET_NULL,verbose_name='turi')
    title = models.CharField(max_length=100, verbose_name='sarlavha')
    date = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=1000, verbose_name='maqola')
    image = models.ImageField(upload_to='index/events/img', verbose_name='rasm')
    img_webp = models.ImageField(blank=True, upload_to="index/events/img_webp")
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        # Convert image to WebP and save
        if self.image:
            # Open the image using Pillow
            pil_image = Image.open(self.image)
            # Convert the image to RGB mode if it's not
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            # Save the image in a BytesIO object
            image_io = BytesIO()
            pil_image.save(image_io, format='WEBP')
            # Create a Django-friendly ContentFile
            webp_image = ContentFile(image_io.getvalue())
            # Save to img_webp field
            self.img_webp.save(f'{self.image.name.split(".")[0]}.webp', webp_image, save=False)

        super().save(*args, **kwargs)







class Teacher(models.Model):
    
    def get_img(self):
        return self.img_webp.url
    class Meta:
        verbose_name = "O'qituvchilar"
        verbose_name_plural = "O'qituvchilar"
    
    
    
    facebook = models.CharField(blank=True, null=True, max_length=400)
    linkedin = models.CharField(blank=True, null=True, max_length=400)
    telegram = models.CharField(blank=True, null=True, max_length=400)
    
    filial = models.ForeignKey(Fillial, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, verbose_name='ism')
    about = models.TextField(max_length=1000, verbose_name='haqida')
    image = models.ImageField(upload_to="index/teachers/img", verbose_name='rasm')
    img_webp = models.ImageField(blank=True, upload_to="index/teachers/img_webp")
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Convert image to WebP and save
        if self.image:
            # Open the image using Pillow
            pil_image = Image.open(self.image)
            # Convert the image to RGB mode if it's not
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            # Save the image in a BytesIO object
            image_io = BytesIO()
            pil_image.save(image_io, format='WEBP')
            # Create a Django-friendly ContentFile
            webp_image = ContentFile(image_io.getvalue())
            # Save to img_webp field
            self.img_webp.save(f'{self.image.name.split(".")[0]}.webp', webp_image, save=False)

        super().save(*args, **kwargs)



class About(models.Model):
    def __str__(self):
        return self.welcome
    
    welcome = models.CharField(max_length = 50, verbose_name='xush kelibsiz')
    content = models.TextField(max_length = 1000, verbose_name='haqida')
    
    class Meta:
        verbose_name = "Haqida"
        verbose_name_plural = "Haqida"

   


class Students(models.Model):
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Studentlar"
    
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50, verbose_name='student ismi')
    surname = models.CharField(max_length=50, verbose_name='student familiyasi')
    phone = models.CharField(max_length=13, verbose_name='nomer')
    courses = models.ManyToManyField(Course, blank=True,  verbose_name="yozilgan kurslari")
    teachers = models.ManyToManyField(Teacher, null=True, blank=True, verbose_name="o'qituvchilari")
    active = models.BooleanField(blank=True, default=False, verbose_name="O'qimoqda")
    filliallar = models.ManyToManyField(Fillial, blank=True, verbose_name="filliallar")

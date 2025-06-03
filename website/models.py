from django.db import models


class ImageSlider(models.Model): #slider de imagens da home
  image = models.ImageField(upload_to='slider_images/')
  title = models.CharField(max_length=100, blank=True, null=True)
  class Meta: #personalizar texto na página admin
    verbose_name = "Carrossel de Imagem"
    verbose_name_plural = "Carrossel de Imagens"

class TeamMember(models.Model): #pagina de equipe
  name = models.CharField(max_length=150)
  role = models.CharField(max_length=100)
  image = models.ImageField(upload_to='team_images/',blank=True,null=True)
  def __str__(self):
    return self.name
  
class ContactMessage(models.Model): #pagina para receber msg contato
  name = models.CharField(max_length=150)
  email = models.EmailField()
  subject = models.CharField(max_length=200, blank=True, null=True)
  message = models.TextField(null=True)
  received_at = models.DateTimeField(auto_now=True)

class HomeSection(models.Model): #secoes da home
  title = models.CharField(max_length=200)
  content = models.TextField()

class AboutSection(models.Model): #secoes da pagina sobre
  title = models.CharField(max_length=200)
  content = models.TextField()
  def __str__(self):
    return self.title


from django.shortcuts import render
from .models import AboutSection, HomeSection, TeamMember, ContactMessage,ImageSlider


def home(request):
  sliders = ImageSlider.objects.all()
  sections = HomeSection.objects.all()
  return render(request,'home.html',{'sliders':sliders,'sections':sections})

def about(request):
  sections = AboutSection.objects.all()
  return render(request,'about.html',{'sections':sections})

def products(request):
  produtos = [
    {
      "nome": "Botijão de Gás 13kg",
      "descricao": "Ideal para uso doméstico. Entrega rápida!",
      "preco": "79,90",
      "imagem_url": "/static/produtos1.png",
      "link": "/comprar/13kg"
    },
    {
      "nome": "Botijão de Gás 45kg",
      "descricao": "Perfeito para empresas e uso contínuo.",
      "preco": "295,00",
      "imagem_url": "/static/produtos2.png",
      "link": "/comprar/45kg"
    },
    {
      "nome": "Kit Gás + Instalação",
      "descricao": "Inclui 1 botijão 13kg + instalação técnica.",
      "preco": "149,90",
      "imagem_url": "/static/produtos3.png",
      "link": "/comprar/kit"
    },
  ]
  return render(request, 'products.html', {'produtos': produtos})

def missao(request):
  return render(request, 'missao.html')
def team(request):
  team_members = TeamMember.objects.all()
  return render(request,'team.html',{'team_members':team_members})

def contact(request):
  if request.method == 'POST':
    ContactMessage.objects.create(
      name = request.POST['name'],
      email = request.POST['email'],
      #subject = request.POST['subject'],
      message = request.POST['message']
    )
    return render(request,'contact.html',{'message': 'Mensagem enviada com sucesso!'})
  return render(request, 'contact.html')
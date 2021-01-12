from django.shortcuts import render
from .models import SideBarElements
from .models import Products
from .models import Materials
from .models import Recipes
from .models import Orders
from .models import Retailors
from django.contrib.auth.models import User

# Create your views here.
    
def index(request):

    
   
   
    #///////SideBar Elements\\\\\\\\
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'
    
    #////////\\\\\\\\\
    
    return render(request,'index.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7})


def hammaddeler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'
   
    materials = Materials.objects.all()
    return render(request,'hammaddeler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'materials':materials})

def urunler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'
   

    products = Products.objects.all()

    return render(request,'urunler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'products':products})

def receteler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'

    

    recipes = Recipes.objects.all()
    

    return render(request,'receteler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'recipes':recipes})

def siparisler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'

    

    
    
    orders = Orders.objects.all()    
    return render(request,'siparisler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'orders':orders})

def bayiler(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'

    
    
    retailors = Retailors.objects.all()   
    
    return render(request,'bayiler.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'retailors':retailors,})

def siparisgecmisleri(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'
    
    
    
    return render(request,'siparisgecmisleri.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,})

def finans(request):
    element1 = SideBarElements()
    element1.elementName = 'Anasayfa'
    element2 = SideBarElements()
    element2.elementName = 'Ürünler'
    element3 = SideBarElements()
    element3.elementName = 'Hammaddeler'
    element4 = SideBarElements()
    element4.elementName = 'Reçeteler'
    element5 = SideBarElements()
    element5.elementName = 'Siparişler'
    element6 = SideBarElements()
    element6.elementName = 'Bayiler'
    element7 = SideBarElements()
    element7.elementName = 'Finans'
    
    names = []
    data = []
    queryset = Products.objects.order_by('-productPrice')[:5]
    for product in queryset:
        names.append(product.productName)
        data.append(product.productPrice)

 
    
    return render(request,'finans.html',{'element1':element1,'element2':element2,'element3':element3,'element4':element4,'element5':element5,'element6':element6,'element7':element7,'names': names,'data': data,})
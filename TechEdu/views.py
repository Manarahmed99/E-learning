from django.shortcuts import get_object_or_404,render,redirect

from django.http import HttpResponse
from django.template import loader
from .models import Items,ItemDetails,Cart
from django.core.paginator import Paginator 
from django.http import Http404
from .forms  import CreateUserForm,LoginUserForm
from django.contrib.auth import login, logout , authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


#-------------------------------------------------
def BasePage(request):
    current_user = request.user
    cart_items = Cart.objects.filter(Id_user=current_user.id)
    return render(request, 'Base.html', {'current_user': current_user, 'cart_items': cart_items})


def landingPage(request):
    item_details = ItemDetails.objects.all()
    items_per_page = 3
    paginator = Paginator(item_details, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'LandingPage.html', {'page_obj': page_obj})
  
def AboutusPage(request):
    current_user = request.user
    cart_items = Cart.objects.filter(Id_user=current_user.id)
    return render(request, 'AboutUsPage.html', {'current_user': current_user, 'cart_items': cart_items})

def ConnectWithUs_Page(request):
    current_user = request.user
    cart_items = Cart.objects.filter(Id_user=current_user.id)
    return render(request, 'ConactUspage.html', {'current_user': current_user, 'cart_items': cart_items})

def show_cart(request):
    current_user = request.user
    cart_items = Cart.objects.filter(Id_user=current_user.id)
    return render(request, 'CartPage.html', {'current_user': current_user, 'cart_items': cart_items})

    


#-----------------------------------------------------
@csrf_exempt
def Login_Page(request):
    form=LoginUserForm()
    if request.method=="POST":
          form=LoginUserForm(data=request.POST)
          if form.is_valid():
              username=form.cleaned_data['username']
              password=form.cleaned_data['password']

              user=authenticate(username=username,password=password)
              if user:
                   if user.is_active:
                        login(request,user)
                        return render(request,'LandingPage.html')
    context={'form':form}
    return render(request,'auth_login.html',context)

@csrf_exempt
def Register_Page(request):
      template=loader.get_template('auth_register.html')
      form=CreateUserForm()
      if request.method=="POST":
           form=CreateUserForm(request.POST)
           if form.is_valid():
                form.save()
                return redirect('Auth_login_Page')
      context={'registerform':form}
      return HttpResponse(template.render(context=context))

@csrf_exempt
def auth_logout(request):
    if request.method == "POST":
        logout(request)
        
        if request.user.is_authenticated:
            Cart.objects.filter(Id_user=request.user.id).delete()
        
        return redirect('/')  
    
#---------------------------------------------------------------
@csrf_exempt
def course_list (request):
    category = request.GET.get('category')
    item_details = ItemDetails.objects.all()
    
    if category:
        item_details = item_details.filter(itemsid__name=category)
    
    return render(request, 'CoursesPage.html', {'item_details': item_details})
    
  
    
def Details(request, id):
    current_user = request.user
    course = get_object_or_404(ItemDetails.objects.select_related('itemsid'), id=id)  
    context = {
        'item_details': course, 
    }
    return render(request, 'CoursesDetailsPage.html', context)
  



#---------------------------------------------------------------
#ِAdd To Cart
def add_to_cart(requset,id):
     currentuser=requset.user
     discount=2
     state=False
     course=ItemDetails.objects.select_related('itemsid').filter(id=id)
    
     for item in course:
           net=item.total-discount
     cart = Cart(
      Id_product=item.id,
      Id_user=currentuser.id,
      price=item.price,
      title=item.title,
      image=item.image,
      itemsid=item.itemsid,
      tax=item.tax,
      total=item.total,
      discount=discount,
      net=net,
      status=state
)
     currentuser=requset.user.id
     count=Cart.objects.filter(Id_user=currentuser).count()
     print(count)
     cart.save()
     requset.session['countcart']=count
     return redirect("/Courses")



def delete_item(request, item_id):
    item = get_object_or_404(Cart, id=item_id)
    item.delete()
    return redirect('cartpage') 



@login_required(login_url='/auth_login/')
def checkout(request):
       template=loader.get_template('CheckoutPage.html')
       current_user = request.user.id
       cart=Cart.objects.all().filter(Id_user=current_user).first()
       product=Items.objects.get(id=cart.Id_product)
       context={
            'cart':cart,
            'productname':product,
             'request':request
            
       }
       return HttpResponse(template.render(context=context)) 

  


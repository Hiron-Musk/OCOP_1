from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Carbonpoint, Greenpoint, Userpoint
from .forms import CarbonForm, GreenForm, AddPointForm, AddGreenForm, Savecarbonpoint

from django.views.decorators.http import require_POST
from .cart import Cart, Cartgreen
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@staff_member_required(login_url='OCOP:login')
def Createcarbon(request):
    """
    admin계정만 들어와서 포인트 종류 입력 가능
    """
    if request.method == 'POST':
        form = CarbonForm(request.POST)
        if form.is_valid():
            carbonpoint = form.save(commit=False)
            carbonpoint.create_date = timezone.now()
            carbonpoint.save()
            return redirect('point:carbonlist')
    else:
        form = CarbonForm()

    context = {'form': form}
    return render(request, 'point/carbonform.html', context)

@staff_member_required(login_url='OCOP:login')
def Creategreen(request):
    """
    admin계정만 들어와서 포인트 종류 입력 가능
    """
    if request.method == 'POST':
        form = GreenForm(request.POST)
        if form.is_valid():
            greenpoint = form.save(commit=False)
            greenpoint.create_date = timezone.now()
            greenpoint.save()
            return redirect('point:greenlist')
    else:
        form = GreenForm()

    context = {'form': form}
    return render(request, 'point/greenform.html', context)

def Carbonlist(request):
    """
    탄소포인트, 그린포인트 목록을 보여주고 수정 추가 삭제 가능
    """
    carbonlist = Carbonpoint.objects.order_by('create_date')
    context = {'carbonlist': carbonlist}
    return render(request, 'point/carbonlist.html', context)

def Greenlist(request):
    """
    탄소포인트, 그린포인트 목록을 보여주고 수정 추가 삭제 가능
    """
    greenlist = Greenpoint.objects.order_by('create_date')
    context = {'greenlist': greenlist}
    return render(request, 'point/greenlist.html', context)

@staff_member_required(login_url='OCOP:login')
def Carbon_Modify(request, Carbonpoint_id):
    """
    admin계정만 들어와서 포인트 수정 가능
    """
    carbon = get_object_or_404(Carbonpoint, pk=Carbonpoint_id)

    if request.method == 'POST':
        form = CarbonForm(request.POST, instance = carbon)
        if form.is_valid():
            carbonpoint = form.save(commit=False)
            carbonpoint.modify_date = timezone.now()
            carbonpoint.save()
            return redirect('point:carbonlist')
    else:
        form = CarbonForm(instance=carbon)

    context = {'form': form}
    return render(request, 'point/carbonmodify.html', context)

@staff_member_required(login_url='OCOP:login')
def Green_Modify(request, Greenpoint_id):
    """
    admin계정만 들어와서 포인트 수정 가능
    """
    green = get_object_or_404(Greenpoint, pk=Greenpoint_id)

    if request.method == 'POST':
        form = GreenForm(request.POST, instance = green)
        if form.is_valid():
            greenpoint = form.save(commit=False)
            greenpoint.modify_date = timezone.now()
            greenpoint.save()
            return redirect('point:greenlist')
    else:
        form = GreenForm(instance=green)

    context = {'form': form}
    return render(request, 'point/greenmodify.html', context)

@staff_member_required(login_url='OCOP:login')
def Carbon_Delete(request, Carbonpoint_id):
    """
    admin계정만 탄소포인트 삭제
    """
    carbon = get_object_or_404(Carbonpoint, pk = Carbonpoint_id)

    carbon.delete()
    return redirect('point:carbonlist')

@staff_member_required(login_url='OCOP:login')
def Green_Delete(request, Greenpoint_id):
    """
    admin계정만 그린포인트 삭제
    """
    green = get_object_or_404(Greenpoint, pk = Greenpoint_id)

    green.delete()
    return redirect('point:greenlist')




#장바구니 기능
def Carbonpage(request):
    """
    탄소페이지 보여줌
    """
    carbon_list = Carbonpoint.objects.order_by('create_date')
    addcart = AddPointForm(initial={'quantity': 1})
    context = {'carbon_list': carbon_list, 'addcart':addcart}

    return render(request, 'point/carbon.html', context)

def Greenpage(request):
    """
    그린페이지 보여줌
    """
    green_list = Greenpoint.objects.order_by('create_date')
    gaddcart = AddGreenForm(initial={'quantity': 1})
    context = {'green_list': green_list, 'gaddcart':gaddcart}
    return render(request, 'point/green.html', context)

def Detail(request):
    # if HttpResponse(None):
    #     return redirect('point:carbonpage')
    # else:
    cart = Cart(request)
        # for i in range(0, cart.cartcount(),):
    for point in cart:
        point = AddPointForm(initial={'quantity':point['quantity'], 'is_update':True})
        # print(cart.cartcount())
        context = {'point': point, 'cart': cart}
        return render(request, 'point/cartdetail.html', context)

def Detailgreen(request):
    print('Detailgreen')

    cart = Cartgreen(request)
    print('Detailgreen1')
    # for i in range(0, cart.cartcount(),):
    for point in cart:
        print('Detailgreen2')
        point = AddGreenForm(initial={'quantity':point['quantity'], 'is_update':True})
        print('Detailgreen3')
        # print(cart.cartcount())
        context = {'point': point, 'cart': cart}
        print('Detailgreen4')
        return render(request, 'point/cartgreen.html', context)

@require_POST
def Add(request, Carbonpoint_id):
    cart = Cart(request)
    carbonpoint = get_object_or_404(Carbonpoint, id=Carbonpoint_id)

    # 클라이언트 -> 서버로 데이터를 전달
    # 유효성검사, injection 전처리
    form = AddPointForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(carbonpoint=carbonpoint, quantity=cd['quantity'], is_update=cd['is_update'])

        return redirect('point:detail')

@require_POST
def Addgreen(request, Greenpoint_id):
    cart = Cartgreen(request)
    greenpoint = get_object_or_404(Greenpoint, id=Greenpoint_id)

    # 클라이언트 -> 서버로 데이터를 전달
    # 유효성검사, injection 전처리
    form = AddGreenForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(greenpoint=greenpoint, quantity=cd['quantity'], is_update=cd['is_update'])

        return redirect('point:detailgreen')

def Remove(request, Carbonpoint_id):
    cart = Cart(request)
    point = get_object_or_404(Carbonpoint, id=Carbonpoint_id)
    cart.remove(point)
    return redirect('point:detail')

def Removegreen(request, Greenpoint_id):
    cart = Cartgreen(request)
    point = get_object_or_404(Greenpoint, id=Greenpoint_id)
    cart.remove(point)
    return redirect('point:detailgreen')

@require_POST
def Saveusercarbon(request):
    cart=Cart(request)
    userpoint = Userpoint()
    userpoint.user=request.user
    print('user1', userpoint.user)
    userpoint.carbonpoint=cart.get_total_point
    # print('carbon1', userpoint.carbonpoint)
    userpoint.create_date=timezone.now()
    print('date1', userpoint.create_date)
    userpoint.save()
    print('userpoint1', userpoint.user, userpoint.carbonpoint, userpoint.create_date)
    return render(request, 'point/carbon.html')

@require_POST
def Saveusergreen(request):
    cart = Cartgreen(request)
    userpoint = Userpoint()
    userpoint.user = request.user
    print('user1', userpoint.user)
    userpoint.greenpoint = cart.get_total_gpoint
    # print('carbon1', userpoint.carbonpoint)
    # userpoint.totalpoint = userpoint.carbonpoint*userpoint.greenpoint
    userpoint.create_date = timezone.now()
    print('date1', userpoint.create_date)
    userpoint.save()
    print('userpoint1', userpoint.user, userpoint.carbonpoint, userpoint.create_date)
    return render(request, 'point/green.html')


    # cart = Cart(request)
    # print('cart1', cart)
    #
    # form = Savecarbonpoint(request.POST)
    # print('form1', form.user)
    # if form.is_valid():
    #     form = form.save(commit=False)
    #     form.carbonpoint = cart.get_total_point
    #     form.crate_date = timezone.now()
    #     form.save()
    #
    #     print('form2', form)
    #
    #     return render('point/carbon.html')
    # cart = Cart(request)
    # if request.method == 'POST':
    #     form = Saveusercarbon(request.POST)
    #     print('form1', form)
    #     if form.is_valid():
    #         form = cart.save(commit=False)
    #         print('form2', form)
    #         form.user = User.username
    #         print('user1',form.user )
    #         form.carbonpoint = cart.get_total_point
    #         print('cart1', cart)
    #         form.create_date = timezone.now()
    #         form.save()
    #         return redirect('point:detail')
    #     else:
    #         form = cart()
    #
    # content = {'cart':cart, 'form':form}
    # return render(request, 'point/carbon.html', content)

    # if request.method == 'POST':
    #     form = CarbonForm(request.POST)
    #     if form.is_valid():
    #         carbonpoint = form.save(commit=False)
    #         carbonpoint.create_date = timezone.now()
    #         carbonpoint.save()
    #         return redirect('point:carbonlist')
    # else:
    #     form = CarbonForm()
    #
    # context = {'form': form}
    # return render(request, 'point/carbonform.html', context)
    # if request.method == 'POST':
    #     print('save6')
    #     form = Savecarbonpoint(request.POST)
    #     if form.is_valid():
    #         info = form.save()
    #         print('save5', info)
    #         info.user = User.username
    #         print('save3', info.user)
    #         print('save4', User.username)
    #         info.carbonpoint = cart.get_total_point
    #         info.create_date = timezone.now()
    #         info.save()
    #         return redirect('mypage:,mypage')
    # else:
    #     form = Savecarbonpoint()





# def Addcarbon(request, Carbonpoint_id):
#     """
#     add cart 연습
#     """
#     addpoint = Carbonpoint.objects.get(pk=Carbonpoint_id)
#
#     try:
#         cart = Cartcarbon.objects.get(point_id = Carbonpoint.id, user_id=request.user.pk)
#         if cart:
#             if cart.carbonpoint.pointtype == addpoint.pointtype:
#                 cart.quantity +=1
#                 cart.save()
#     except Cartcarbon.DoesNotExist:
#         user = User.objects.get(pk=request.user.pk)
#         cart = Cartcarbon(user=user, carbonpoint=addpoint, quantity=1)
#         cart.save()
#     return redirect('point:usercarbon')
#
# def Usercarbon(request):
#     """
#     add cart 연습
#     """
#     cartpoint=Cartcarbon.objects.filter(user_id=request.user.pk)
#
#     total_point=0
#     for each_total in cartpoint:
#         total_point += each_total.carbonpoint.cpoint * each_total.quantity
#     if cartpoint is not None:
#         context = {
#             'cartpoint':cartpoint,
#             'total_point': total_point,
#         }
#     return render(request, 'cartlist.html', context)













#
# def add_carbon(request):
#     selpoint = Carbonpoint.objects.get(id=Carbonpoint.id)
#
#     try:
#
# def my_carbon():

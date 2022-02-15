from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Carbonpoint, Greenpoint, Userpoint

from .forms import CarbonForm, GreenForm, AddPointForm, AddGreenForm,CarForm,AddCarForm,Savecarbonpoint,Formcarbonpoint


from django.views.decorators.http import require_POST
from .cart import Cart, Cartgreen
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.core.exceptions import BadRequest
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
    carboncart = Formcarbonpoint()
    context = {'carbon_list': carbon_list, 'addcart':addcart, 'carboncart':carboncart}

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
    #
    # addcarbon = Formcarbonpoint(initial={'carbon':['carbon'], 'is_update':True})
    cart = Cart(request)
    # form = Formcarbonpoint(instance=cart.addcarbon)
        # for i in range(0, cart.cartcount(),):
    for point in cart:
        point['quantity_form'] = AddPointForm(initial={'quantity':point['quantity'], 'is_update':True})
        # print(cart.cartcount())

    # for cpoint in cart:
    #     cpoint = Formcarbonpoint(initial={'cpoint':cpoint['cpoint'], 'is_update':True})
    #     print('cpoint', cpoint)
        context = {'point': point, 'cart': cart}
        return render(request, 'point/cartdetail.html', context)

def Detailgreen(request):
    print('Detailgreen')

    cart = Cartgreen(request)
    print('Detailgreen1')
    # for i in range(0, cart.cartcount(),):
    for point in cart:
        print('Detailgreen2')
        point['quantity_form']  = AddGreenForm(initial={'quantity':point['quantity'], 'is_update':True})
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
    return redirect('point:carbonpage')

def Removegreen(request, Greenpoint_id):
    cart = Cartgreen(request)
    point = get_object_or_404(Greenpoint, id=Greenpoint_id)
    cart.remove(point)
    return redirect('point:greenpage')

def Carpage(request):
    """
    carpoint 입력값 받기
    """
    form=AddCarForm()
    return render(request,'point/car.html',{'form':form})

@require_POST
def Saveusercarbon(request):
    cart = Cart(request)
    # form = Formcarbonpoint(request.POST)
    userpoint = Userpoint()
    # if form.is_valid():
    #     userpoint = form.save(commit=False)
    #     userpoint.carbonpoint = cart.get_total_point
    #
    #         form.save()
    userpoint.user=request.user
    print('user1', userpoint.user)
    userpoint.carbonpoint = cart.get_total_point
    # print('carbon1', userpoint.carbonpoint)
    userpoint.create_date=timezone.now()
    print('date1', userpoint.create_date)
    userpoint.save()
    print('userpoint1', userpoint.user, userpoint.carbonpoint, userpoint.create_date)
    return render(request, 'OCOP/main_page.html')

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
    return render(request, 'OCOP/main_page.html')

@require_POST
def Usercarbon(request):
    form = Formcarbonpoint(request.POST)

    userpoint = Userpoint()
    print('form1', form)
    userpoint.user = request.user
    print('user1', userpoint.user)
    userpoint.carbonpoint = form.cleaned_data['cpoint']
    print('cpoint',userpoint.carbonpoint)
    # print('carbon1', userpoint.carbonpoint)
    # userpoint.totalpoint = userpoint.carbonpoint*userpoint.greenpoint
    userpoint.create_date = timezone.now()
    print('date1', userpoint.create_date)
    userpoint.save()
    print('userpoint1', userpoint.user, userpoint.carbonpoint, userpoint.create_date)
    context = {'userpoint':userpoint}
    return render(request, 'point/carbon.html', context)

# def Removecarbon(request):
#     carbon = get_object_or_404(Userpoint)
#     carbon.delete()
#     return render(request, 'point/carbon.html')



    # if request.method == 'POST':
    #     form = CarbonForm(request.POST, instance = carbon)
    #     if form.is_valid():
    #         carbonpoint = form.save(commit=False)
    #         carbonpoint.modify_date = timezone.now()
    #         carbonpoint.save()
    #         return redirect('point:carbonlist')
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






def Carcalculation(request):
    # 참여시점 총 누적 주행거리
    start_total_mileage = request.POST.get('start_total_mileage')
    start_total_mileage=float(start_total_mileage)
    print(start_total_mileage)

    # 참여시점 총 누적 주행거리 제출일자
    start_date_year = request.POST.get('start_date_year')
    start_date_year=int(start_date_year)
    start_date_month = request.POST.get('start_date_month')
    start_date_month = int(start_date_month)
    start_date_day = request.POST.get('start_date_day')
    start_date_day = int(start_date_day)
    print(start_date_year,start_date_month,start_date_day)

    # 차량등록일자
    start_register_date_year = request.POST.get('start_register_date_year')
    start_register_date_year = int(start_register_date_year)
    start_register_date_month = request.POST.get('start_register_date_month')
    start_register_date_month = int(start_register_date_month)
    start_register_date_day = request.POST.get('start_register_date_day')
    start_register_date_day = int(start_register_date_day)
    print(start_register_date_year,start_register_date_month,start_register_date_day)

    # 사업종료시 총 누적 주행거리
    end_total_mileage = request.POST.get('end_total_mileage')
    end_total_mileage=float(end_total_mileage)
    print(end_total_mileage)

    # 사업종료시 총 누적 주행거리 제출일자
    end_date_year = request.POST.get('end_date_year')
    end_date_year = int(end_date_year)
    end_date_month = request.POST.get('end_date_month')
    end_date_month = int(end_date_month)
    end_date_day = request.POST.get('end_date_day')
    end_date_day = int(end_date_day)
    print(end_date_year,end_date_month,end_date_day)

    # 참여신청시 총 누적 주행거리 제출일자 - 차량등록일자

    if start_register_date_day > start_date_day:
        avg_result_month = (start_date_month - start_register_date_month - 1)*30
        avg_result_day = 30 + start_date_day - start_register_date_day
        avg_result_year = (start_date_year - start_register_date_year) * 365
    else:
        avg_result_month = (start_date_month - start_register_date_month)*30
        avg_result_day = start_date_day - start_register_date_day
        avg_result_year = (start_date_year - start_register_date_year) * 365

    res = avg_result_month + avg_result_day + avg_result_year
    print(res)

    # 일평균주행거리 = 참여신청시 총 누적 주행거리 / (참여신청시 총 누적 주행거리 제출일자 - 차량등록일자)
    average_daily_mileage = start_total_mileage / res
    print(average_daily_mileage)

    # 참여기간 = 사업종료시 총 누적 주행거리 제출일자 - 사업참여시 총 누적 주행거리 제출일자
    if start_date_day > end_date_day:
        participation_result_month = (end_date_month - start_date_month - 1)*30
        participation_result_day = 30 + end_date_day - start_date_day
        participation_result_year = (end_date_year - start_date_year) * 365
    else:
        participation_result_month = (end_date_month - start_date_month)*30
        participation_result_day = end_date_day - start_date_day
        participation_result_year = (end_date_year - start_date_year) * 365

    participation_period = participation_result_year + participation_result_month + participation_result_day
    print(participation_period)

    # 기준주행거리=일평균주행거리 * 참여기간
    standard_mileage = average_daily_mileage * participation_period
    standard_mileage = round(standard_mileage, 2)
    print(standard_mileage)

    # 확인주행거리=사업종료시 총 누적 주행거리 - 참여신청시 총 누적 주행거리
    confirmation_mileage = end_total_mileage - start_total_mileage
    print(confirmation_mileage)

    # 감축거리=기준주행거리-확인주행거리
    reduced_distance = standard_mileage - confirmation_mileage
    print(reduced_distance)

    # 감축율=(기준주행거리-확인주행거리)/기준주행거리*100
    reduction_rate = (standard_mileage - confirmation_mileage)/(standard_mileage * 100)
    reduction_rate = round(reduction_rate)
    print(reduction_rate)

    # 총포인트
    if 0 <= reduction_rate < 10:
        carpoint = 20000
    elif reduction_rate < 20:
        carpoint = 40000
    elif reduction_rate < 30:
        carpoint = 60000
    elif reduction_rate < 40:
        carpoint = 80000
    else:
        carpoint = 100000

    #수정
    pointcar = {'carpoint': carpoint}
    if request.method == 'POST':
        form = CarForm(request.POST)
        print('form111',form)
        if form.is_valid():
            # carpoint = form.save(commit=False)
            form = pointcar.values
            print('form222', form)
            # carpoint.create_date = timezone.now()
            form.save()
            return redirect('pybo:index')
    else:
        form = CarForm()
    context = {'form': form}
    return render(request, 'point/car_calculation.html', context)

    # print(carpoint)
    # pointcar={'carpoint': carpoint}
    # print('pointcar', pointcar)
    # form = CarForm()
    # form["carpoint"]=pointcar
    # print('form111', form)
    # context = {'carpoint': carpoint}
    # return render(request, 'point/car_calculation.html', context)

@require_POST
def Carsave(request):
    form = CarForm(request.POST)
    userpoint = Userpoint()
    print(form)
    print(userpoint)

    userpoint.user = request.user
    print('user1', userpoint.user)
    userpoint.carpoint = form.cleaned_data['carpoint']
    # print('carpoint', form.cleaned_data['carpoint'])
    print('carpoint',userpoint.carpoint)
    # print('carbon1', userpoint.carbonpoint)
    # userpoint.totalpoint = userpoint.carbonpoint*userpoint.greenpoint
    userpoint.create_date = timezone.now()
    print('date1', userpoint.create_date)
    userpoint.save()
    print('userpoint1', userpoint.user, userpoint.carpoint, userpoint.create_date)
    return render(request, 'mypage/mypage.html')
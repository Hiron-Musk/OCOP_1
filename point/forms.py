from django import forms
from point.models import Carbonpoint, Greenpoint, Userpoint,Carpoint
from django.utils.safestring import mark_safe
from django.core.validators import MinValueValidator

class CarbonForm(forms.ModelForm):
    class Meta:
        model = Carbonpoint
        fields = ['pointtype', 'cpoint']

        labels = {
            'pointtype':'포인트 종류',
            'cpoint':'포인트량',
        }


class GreenForm(forms.ModelForm):
    class Meta:
        model = Greenpoint
        fields = ['pointtype', 'gpoint']

        labels = {
            'pointtype': '포인트 종류',
            'gpoint': '포인트량',
        }

# 클라이언트 화면에 입력폼을 만들어주기 위함
# 클라이언트가 입력한 데이터에 대한 전처리
# 모델이 있는 상태에서 입력받을때는 ModelForm 아닐때는 From

class AddPointForm(forms.Form):
    quantity = forms.IntegerField(label='수량')
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    class Meta:
        fields = ['quantity']

        labels = {
            'quantity': '수량',
        }

class AddGreenForm(forms.Form):
    quantity = forms.IntegerField(label='수량')
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    class Meta:
        fields = ['quantity']

        labels = {
            'quantity': '수량',
        }

class Savecarbonpoint(forms.ModelForm):
    class Meta:
        model = Userpoint
        fields = ['user', 'carbonpoint', 'greenpoint', 'vehiclepoint', 'totalpoint', 'create_date']

class Formcarbonpoint(forms.Form):
    cpoint = forms.IntegerField(label='포인트량')
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class Formcarpoint(forms.ModelForm):
    class Meta:
        model = Carpoint
        fields = ['carpoint']

class CarForm(forms.Form):
    class Meta:
        fields = ['carpoint']

        labels = {
            'carpoint': '포인트량',
        }

class AddCarForm(forms.Form):
    start_total_mileage =forms.FloatField(label='참여시점의 총 누적 주행거리(km)')

    start_date_year=forms.IntegerField(label='참여시점의 총 누적 주행 거리 제출일자(년)')
    start_date_month=forms.IntegerField(label='참여시점의 총 누적 주행 거리 제출일자(월)')
    start_date_day=forms.IntegerField(label='참여시점의 총 누적 주행 거리 제출일자(일)')

    start_register_date_year=forms.IntegerField(label='차량 최초 등록 일자(년)')
    start_register_date_month=forms.IntegerField(label='차량 최초 등록 일자(월)')
    start_register_date_day=forms.IntegerField(label='차량 최초 등록 일자(일)')

    end_total_mileage=forms.FloatField(label='사업종료시 총 누적 주행 거리(km)')

    end_date_year=forms.IntegerField(label='사업종료시 총 누적 주행거리 제출일자(년)')
    end_date_month = forms.IntegerField(label='사업종료시 총 누적 주행거리 제출일자(월)')
    end_date_day = forms.IntegerField(label='사업종료시 총 누적 주행거리 제출일자(일)')

    class Meta:
        fields = ['start_total_mileage','start_date_year','start_date_month','start_date_day',
                  'start_register_date_year','start_register_date_month','start_register_date_day','end_total_mileage',
                  'end_date_year','end_date_month','end_date_day']

        labels = {
            'start_total_mileage':'참여시점의 총 누적 주행거리(km)',
            'start_date_year':'참여시점의 총 누적 주행 거리 제출일자(년)',
            'start_date_month': '참여시점의 총 누적 주행 거리 제출일자(월)',
            'start_date_day': '참여시점의 총 누적 주행 거리 제출일자(일)',
            'start_register_date_year':'차량 최초 등록 일자(년)',
            'start_register_date_month': '차량 최초 등록 일자(월)',
            'start_register_date_day': '차량 최초 등록 일자(일)',
            'end_total_mileage':'사업종료시 총 누적 주행 거리(km)',
            'end_date_year':'사업종료시 총 누적 주행거리 제출일자(년)',
            'end_date_moth': '사업종료시 총 누적 주행거리 제출일자(월)',
            'end_date_day': '사업종료시 총 누적 주행거리 제출일자(일)',
        }

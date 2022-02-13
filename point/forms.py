from django import forms
from point.models import Carbonpoint, Greenpoint, Userpoint
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
        fields = ['quantiy']

        labels = {
            'quantity': '수량',
        }

class AddGreenForm(forms.Form):
    quantity = forms.IntegerField(label='수량')
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    class Meta:
        fields = ['quantiy']

        labels = {
            'quantity': '수량',
        }

# class UserpointForm(forms.ModelForm):
#     class Meta:
#         model = Userpoint
#         fields = ['user', 'carbonpoint', 'greenpoint', 'vehiclepoint', 'totalpoint']
#
#         labels = {
#             'pointtype':'포인트 종류',
#             'carbonpoint':'탄소포인트',
#             'greenpoint': '그린포인트',
#             'vehiclepoint': '자동차탄소포인트',
#             '토탈포인트': '포인트 종류',
#         }
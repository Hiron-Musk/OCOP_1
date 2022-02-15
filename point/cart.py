from decimal import Decimal
from django.conf import settings
from .models import Carbonpoint, Greenpoint



class Cart(object):
    def __init__(self, request):
        """
        초기화작업
        """
        self.session = request.session #장고뷰에서 사용했던 리퀘스트, 안에 세션 정보가 들어있을것
        cart = self.session.get(settings.CART_ID)  #settings안에 CART_ID를 만들어줘야함
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart

    def __len__(self):
        """
        이터레이터 같은것 쓸데 몇개가 들어있냐 알수있게....
        """
        return sum(item['quantity'] for item in self.cart.values())



    def __iter__(self):
        """
        for문등을 사용할때 어떤 요소들을 건네줄건지 작업할때...
        """

        points_ids = self.cart.keys()

        points = Carbonpoint.objects.filter(id__in=points_ids)

        for carbonpoint in points:
            self.cart[str(carbonpoint.id)]['carbonpoint'] = carbonpoint

        for item in self.cart.values():
            item['cpoint'] = Decimal(item['cpoint'])
            item['total_cpoint'] = item['cpoint']*item['quantity']

            yield item

    def add(self, carbonpoint, quantity=1, is_update=False):
        carbonpoint_id = str(carbonpoint.id)
        if carbonpoint_id not in self.cart:
            self.cart[carbonpoint_id]={'quantity':0, 'cpoint':str(carbonpoint.cpoint)}

        if is_update:
            self.cart[carbonpoint_id]['quantity'] = quantity
        else:
            self.cart[carbonpoint_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def remove(self, Carbonpoint):
        carbonpoint_id = str(Carbonpoint.id)
        if carbonpoint_id in self.cart:
            del(self.cart[carbonpoint_id])
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = {}
        self.session.modified = True

    @property
    def get_total_point(self):
        return sum(int(item['cpoint'])*int(item['quantity'])for item in self.cart.values())


class Cartgreen(object):
    def __init__(self, request):
        """
        초기화작업
        """
        self.session = request.session #장고뷰에서 사용했던 리퀘스트, 안에 세션 정보가 들어있을것
        cart = self.session.get(settings.CART_IDG)  #settings안에 CART_ID를 만들어줘야함

        if not cart:
            cart = self.session[settings.CART_IDG] = {}
        self.cart = cart

    def __len__(self):
        """
        이터레이터 같은것 쓸데 몇개가 들어있냐 알수있게....
        """
        return sum(gitem['quantity'] for gitem in self.cart.values())

    def __iter__(self):
        """
        for문등을 사용할때 어떤 요소들을 건네줄건지 작업할때...
        """
        points_ids = self.cart.keys()

        points = Greenpoint.objects.filter(id__in=points_ids)
        for greenpoint in points:
            self.cart[str(greenpoint.id)]['greenpoint'] = greenpoint

        for gitem in self.cart.values():

            gitem['gpoint'] = Decimal(gitem['gpoint'])
            gitem['total_gpoint'] = gitem['gpoint']*gitem['quantity']

            yield gitem

    def add(self, greenpoint, quantity=1, is_update=False):
        greenpoint_id = str(greenpoint.id)
        if greenpoint_id not in self.cart:
            self.cart[greenpoint_id]={'quantity':0, 'gpoint':str(greenpoint.gpoint)}

        if is_update:
            self.cart[greenpoint_id]['quantity'] = quantity
        else:
            self.cart[greenpoint_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_IDG] = self.cart
        self.session.modified = True

    def remove(self, Greenpoint):
        greenpoint_id = str(Greenpoint.id)
        if greenpoint_id in self.cart:
            del(self.cart[greenpoint_id])
            self.save()

    def clear(self):
        self.session[settings.CART_IDG] = {}
        self.session.modified = True

    @property
    def get_total_gpoint(self):
        return sum(int(gitem['gpoint'])*int(gitem['quantity'])for gitem in self.cart.values())
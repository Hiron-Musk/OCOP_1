from decimal import Decimal
from django.conf import settings
from .models import Carbonpoint, Greenpoint



class Cart(object):
    def __init__(self, request):
        """
        초기화작업
        """
        # if not self.request.session:
        #     cart = []
        #     return (request, cart)
        self.session = request.session #장고뷰에서 사용했던 리퀘스트, 안에 세션 정보가 들어있을것
        # print('Cartgreen2', request.session)
        cart = self.session.get(settings.CART_ID)  #settings안에 CART_ID를 만들어줘야함
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart

        # print('Cartgreen3', self.cart.values())

    def __len__(self):
        """
        이터레이터 같은것 쓸데 몇개가 들어있냐 알수있게....
        """
        return sum(item['quantity'] for item in self.cart.values())

    # def cartcount(self):
    #     cartlist = []
    #     for item in self.cart.values():
    #         item['cpoint'] = Decimal(item['cpoint'])
    #         cartlist = item['quantity']
    #     context = {'list': cartlist}
    #     # print(context)
    #     return context


    def __iter__(self):
        """
        for문등을 사용할때 어떤 요소들을 건네줄건지 작업할때...
        """

        points_ids = self.cart.keys()

        points = Carbonpoint.objects.filter(id__in=points_ids)

        for carbonpoint in points:
            self.cart[str(carbonpoint.id)]['carbonpoint'] = carbonpoint

        # print('__iter__5 ', self.cart.values())
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


    # def addcarbon(self, cpoint=1, is_update=False):
    #     carbonp=str(cpoint)
    #     print('add', carbonp)
    #     if carbonp not in self.cart:
    #         self.cart[carbonp]={'cpoint':str(cpoint), 'quantity':1}
    #
    #     if is_update:
    #         self.cart[carbonp]['quantity'] = cpoint
    #         print('carbon2',carbonp)
    #     else:
    #         self.cart[carbonp]['quantity'] += cpoint
    #     print('add2', carbonp)
    #     self.save()

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

        # print('Cartgreen1')
        self.session = request.session #장고뷰에서 사용했던 리퀘스트, 안에 세션 정보가 들어있을것
        # print('Cartgreen2', request.session.session_key)
        # self.session ={}
        # self.session = request.session.clear_expired()
        cart = self.session.get(settings.CART_IDG)  #settings안에 CART_ID를 만들어줘야함
        # print('Cartgreen3')
        if not cart:
            cart = self.session[settings.CART_IDG] = {}
        self.cart = cart

        # self.cart = {}
        # print('Cartgreen3', self.cart.values())

    def __len__(self):
        """
        이터레이터 같은것 쓸데 몇개가 들어있냐 알수있게....
        """
        return sum(gitem['quantity'] for gitem in self.cart.values())

    # def cartcount(self):
    #     cartlist = []
    #     for item in self.cart.values():
    #         item['cpoint'] = Decimal(item['cpoint'])
    #         cartlist = item['quantity']
    #     context = {'list': cartlist}
    #     # print(context)
    #     return context

    def __iter__(self):
        """
        for문등을 사용할때 어떤 요소들을 건네줄건지 작업할때...
        """
        # print('__iter__1')
        points_ids = self.cart.keys()

        points = Greenpoint.objects.filter(id__in=points_ids)
        # print('__iter__2')
        for greenpoint in points:
            self.cart[str(greenpoint.id)]['greenpoint'] = greenpoint
            # print('__iter__3 ', greenpoint.id )

        # self.cart = {}
        # print('__iter__4 ', self.cart.values() )

        for gitem in self.cart.values():
            # print('__iter__4 ', gitem['gpoint'])

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
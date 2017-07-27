import re
import unittest


def sub_by_re(input_str):

    """ symbol class \w must be extended if we want to use other kind of symbol
    for example [\w|+|-]"""

    pattern = '(\(\w*)*$'
    return re.sub(pattern, '', input_str)


def sub_by_code(input_str):
    close_par_search = input_str.rfind(')') + 1
    open_par_search = input_str[close_par_search:].find('(')
    if open_par_search != -1:
        input_str = input_str[:close_par_search + open_par_search]

    return input_str


class TestSubBy(unittest.TestCase):

    def test_by_re(self):
        self.assertEqual(sub_by_re('esdfd((esdf)(esdf'), 'esdfd((esdf)')
        self.assertEqual(sub_by_re('esdfd((esdf)(esdf(esd)asd'),
                         'esdfd((esdf)(esdf(esd)asd')
        self.assertEqual(sub_by_re('esdfd((esdf(esd)(esdf'),
                         'esdfd((esdf(esd)')
        self.assertEqual(sub_by_re('esdfd)((esdf(esd)(esdf(esd'),
                         'esdfd)((esdf(esd)')

    def test_by_code(self):
        self.assertEqual(sub_by_code('esdfd((esdf)(esdf'), 'esdfd((esdf)')
        self.assertEqual(sub_by_code('esdfd((esdf)(esdf(esd)asd'),
                         'esdfd((esdf)(esdf(esd)asd')
        self.assertEqual(sub_by_code('esdfd((esdf(esd)(esdf'),
                         'esdfd((esdf(esd)')
        self.assertEqual(sub_by_code('esdfd)esd)((esdf(esd)(esdf(esd'),
                         'esdfd)esd)((esdf(esd)')


if __name__ == '__main__':
    unittest.main()
    # type_res = input('Type string, please:')
    #
    # print(sub_by_re(type_res))
    # print(sub_by_code(type_res))


# q_1 = Product.objects.filter(price__gte=100).values('category__name').\
#     annotate(GoodCount = Sum('category'))
#
# q_2 = Product.objects.filter(price__gte=100).values('category__name').\
#     annotate(GoodCount = Sum('category')).filter(GoodCount__gt = 10)
#
# product_qs = Product.objects.all()#Получен не вычисленный queryset
#
# if product_qs.exist():#Первый запрос к базе данных на выборку 1 строки
#
#     '''Второй запрос к базе данных, если она не пуста,
#      данные читаются частями (используем метод .iterator()),
#       чтобы не переполнить кэш queryset'''
#
#     for i in product_qs.iterator():
#         print('Category: %s | Product: %s | Price: %s' % (i.category, i.name, i.price))
#
# '''Здесь конечно приведено 2 запроса к БД, однако если бы использовалась не вся '''
#
#
#
# SELECT disc_kind.id FROM public."AD_updater_discountkind" disc_kind
# WHERE disc_kind.id IN (SELECT disc.disc_kind_id from public."AD_updater_discounts" disc
# WHERE disc.disc_start  <= '2017-06-29' AND disc.disc_stop  >= '2017-06-29')
#
# SELECT goods.good_name, goods.price, disc_kind.disc_name, MAX(disc_kind.disc_size) disc_size,  ((100 - MAX(disc_kind.disc_size))*goods.price)/100 discounted_price FROM public."AD_updater_goods" goods LEFT OUTER JOIN "AD_updater_discountkind" disc_kind ON (goods.group_id = disc_kind.group_id
#   OR goods.brend_id = disc_kind.brend_id OR goods.id = disc_kind.group_id) WHERE disc_kind.id IN (SELECT disc.disc_kind_id from public."AD_updater_discounts" disc WHERE disc.disc_start  <= '2017-06-29' AND disc.disc_stop  >= '2017-06-29')
# GROUP BY goods.good_name, goods.price, disc_kind.disc_name
#
# SELECT goods.good_name, goods.price, discounts.disc_name, MAX(discounts.disc_size) disc_size,  ((100 - MAX(discounts.disc_size))*goods.price)/100 discounted_price FROM public."AD_updater_goods" AS goods
#   LEFT OUTER JOIN
#   (SELECT disc_kind.* FROM public."AD_updater_discountkind" AS disc_kind  WHERE disc_kind.id IN
#         (SELECT disc.disc_kind_id FROM public."AD_updater_discounts" AS disc WHERE disc.disc_start  <= '2017-06-29' AND disc.disc_stop  >= '2017-06-29')) discounts
#     ON (goods.group_id = discounts.group_id OR goods.brend_id = discounts.brend_id OR goods.id = discounts.group_id)
# GROUP BY goods.good_name, goods.price, discounts.disc_name


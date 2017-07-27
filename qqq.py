class Clients(models.Model):
    client_name = models.CharField(max_length=100, verbose_name='Клиент')

    def __str__(self):
        return r'%s' % self.client_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Brends(models.Model):
    brend_name = models.CharField(max_length=100,
                                  verbose_name='Наименование бренда')

    def __str__(self):
        return r'%s' % self.brend_name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class GoodsGroups(models.Model):
    group_name = models.CharField(max_length=100,
                                  verbose_name='Наименование группы')

    def __str__(self):
        return r'%s' % self.group_name

    class Meta:
        verbose_name = 'Группа товаров'
        verbose_name_plural = 'Группы товаров'


class Goods(models.Model):
    good_name = models.CharField(max_length=100,
                                 verbose_name='Наименование товара')
    group = models.ForeignKey(GoodsGroups,
                              verbose_name='Группа Товаров', default=4)
    brend = models.ForeignKey(Brends, verbose_name='Бренд')
    price = models.DecimalField(max_digits=15, decimal_places=2,
                                verbose_name='Цена', default=0)

    def __str__(self):
        return r'%s' % self.good_name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class DiscountKind(models.Model):
    disc_name = models.CharField(max_length=100, verbose_name='Наименование')
    group = models.ForeignKey(GoodsGroups, blank=True, null=True)
    brend = models.ForeignKey(Brends, blank=True, null=True)
    good = models.ForeignKey(Goods, blank=True, null=True)
    disc_size = models.IntegerField()

    def __str__(self):
        return r'%s' % self.disc_name

    class Meta:
        verbose_name = 'Вид скидки'
        verbose_name_plural = 'Виды скидки'


class Discounts(models.Model):
    disc_kind = models.ForeignKey(DiscountKind, verbose_name='Вид скидки')
    disc_start = models.DateField(verbose_name='Начало подписки')
    disc_stop = models.DateField(verbose_name='Окончание подписки')

    def __str__(self):
        return r'%s' % self.disc_kind

    class Meta:
        verbose_name = 'Скидки'
        verbose_name_plural = 'Скидки'

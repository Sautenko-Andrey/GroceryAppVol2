class MutualContext:

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

def make_list(count,pos):
    '''Метод для создания вложенного списка для обучающей выборки в тестовой НС'''
    res=[[0 for x in range(count)]]
    res[0][pos]=1
    return res


def price_updating_data(price):
    price = price[:5]
    try:
        price = float(price.replace(',', '.'))
    except Exception:
        print('Короткая цена!')
        price=float(price[:2])
    return price

# result=make_list(10,0)
# print(result)
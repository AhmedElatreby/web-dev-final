from django.http import JsonResponse
from django.shortcuts import get_object_or_404,render

from fresher.models import Recipe

from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        recipe_id = int(request.POST.get('recipeid'))
        recipe_qty = int(request.POST.get('recipeqty'))
        recipe = get_object_or_404(Recipe, id=recipe_id)
        basket.add(recipe=recipe, qty=recipe_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response    


# def basket_delete(request):
#     basket = Basket(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('productid'))
#         basket.delete(product=product_id)

#         basketqty = basket.__len__()
#         baskettotal = basket.get_total_price()
#         response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
#         return response


# def basket_update(request):
#     basket = Basket(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('productid'))
#         product_qty = int(request.POST.get('productqty'))
#         basket.update(product=product_id, qty=product_qty)

#         basketqty = basket.__len__()
#         baskettotal = basket.get_total_price()
#         response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
#         return response


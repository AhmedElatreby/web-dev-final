from decimal import Decimal

from fresher.models import Recipe


class Basket():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, recipe, qty):
        """
        Adding and updating the users basket session data
        """
        recipe_id = str(recipe.id)

        if recipe_id in self.basket:
            self.basket[recipe_id]['qty'] = qty
        else:
            self.basket[recipe_id] = {'price': str(recipe.price), 'qty': qty}

        self.save()    
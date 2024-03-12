#to get a key value pair

def dummy(request):
    return {"msg":"hello django"}


def basket_count(request):
    if request.user.is_authenticated:
        count=request.user.cart.cart_item_count
        return {"cart_count":count}
    else:
        return {"cart_count":0}
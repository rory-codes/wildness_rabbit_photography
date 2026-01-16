try:
    from cart.cart import Cart  
except ImportError:
    Cart = None  


def cart_count(request):
    """
    Exposes {{ cart_count }} to all templates.
    If Cart or session isn't available, returns 0.
    """
    if Cart is None:
        return {"cart_count": 0}

    try:
        return {"cart_count": Cart(request).count()}
    except Exception:
        return {"cart_count": 0}
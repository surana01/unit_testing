def compute_discounted_price(price, discount_provider):
    """
    Compute a discounted price using a provided discount provider.

    Parameters
    ----------
    price : float
        The original price.
    discount_provider : callable
        A function that returns the discount percentage as a float between 0 and 1.

    Returns
    -------
    float
        The final price after applying the discount.
    """
    discount = discount_provider()
    return price * (1 - discount)
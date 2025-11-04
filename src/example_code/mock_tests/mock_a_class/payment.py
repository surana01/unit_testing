class PaymentGateway:
    """Simulates a third-party payment gateway."""

    def charge(self, amount):
        """Charge a given amount. In production, this would hit an external API."""
        raise NotImplementedError("This method should be implemented by subclasses.")


def process_payment(amount, gateway):
    """
    Process a payment using a given payment gateway instance.

    Parameters
    ----------
    amount : float
        The payment amount.
    gateway : PaymentGateway
        An instance of a payment gateway.

    Returns
    -------
    str
        "success" if charge succeeds, "failure" otherwise.
    """
    try:
        gateway.charge(amount)
        return "success"
    except Exception:
        return "failure"
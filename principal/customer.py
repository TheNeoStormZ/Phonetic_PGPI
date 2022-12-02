import stripe

def create_customer(user):
    customer = stripe.Customer.create(
        description=user.username #Una simple descripción del usuario
    )
    return customer
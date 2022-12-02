import stripe
from phonetic import settings

stripe.api_key = settings.STRIPE_SECRET_KEY
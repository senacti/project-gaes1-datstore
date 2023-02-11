# Set your secret key. Remember to switch to your live secret key in production.


intent = stripe.PaymentIntent.create(
  amount=1099,
  currency='usd',
  # Verify your integration in this guide by including this parameter
  metadata={'integration_check': 'accept_a_payment'},
)
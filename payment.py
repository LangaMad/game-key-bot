from yookassa import Payment
from yookassa.domain.request import PaymentRequest
import uuid


async def create_payment(amount,description,chat_id,currency='RUB'):
    id_key = str(uuid.uuid4())
    payment = Payment.create(
        {
            'amount': {
                'value': str(amount),
                'currency': currency
            },
            'payment_method_data': {
                'type': 'bank_card'
            },
            'confirmation': {
                'type': 'redirect',
                'return_url': 'https://webhook.site/c8089bc2-0664-4438-877f-991717a10f59'
            },
            "capture": True,
                "description": description,
                "metadata": {
                'chat_id': chat_id
        },
        },id_key)
    
    return payment.confirmation.confirmation_url, payment.id


async def get_payment(payment_id):
    payment = Payment.find_one(payment_id)
    return payment.status


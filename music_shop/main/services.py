from main.models import Customer

def get_order_by_id(user, o_id):
    customer = Customer.objects.get(user=user)
    order = customer.orders.filter(id=o_id).first()
    return {
        'first_name': order.first_name,
        'last_name': order.last_name,
        'address': order.address,
        'phone': order.phone,
        'buying_type': order.buying_type,
        'comment': order.comment,
        'order_date': str(order.order_date)
    }
balance=100
def process_payment(
        payment_id: int | str,
        amount: int | float,
        payment_status : str,
)-> dict | None:
    
    print(f'processing payment for {payment_id}')

    if amount > 0:
        if balance >=amount:
          return {"Transaction_id": payment_id, "amount": amount, "payment_status":payment_status, "message":"The payment processed successfully."}
    return None
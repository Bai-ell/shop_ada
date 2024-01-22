from account.send_email import  send_confirmation_password, send_confirmation_email, send_activaton_sms
from order.send_emal import sender_order_notification
from .celery import app 

@app.task()
def send_confiramtion_email_task(email,code):
    send_confirmation_email(email, code)
    
@app.task()
def send_confiramtion_password_task(email,code):
    send_confirmation_password(email, code)
    
@app.task()
def sender_order_notification_task(user_email,order_id):
    sender_order_notification(user_email, order_id)
    
    
        
@app.task()
def send_activation_sms_task(phone_number,activation_code):
    send_activaton_sms(phone_number, activation_code)
    

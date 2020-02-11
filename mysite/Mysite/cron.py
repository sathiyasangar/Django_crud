
def my_cron_job():
    from django.core.mail import send_mail 
    # your functionality goes here
    print('######################################')  // this is added because I want to see if terminal / console would print this out as I would know at least the function did at least run but never seen this got printed
    send_mail(
        'cron job test',
        'Here is the message.',
        'sathiyasangar.p.s.0@gmail.com',  // using real email locally
        ['sathiyasangar.p.s@gmail.com'],  // using real email locally 
        fail_silently=False,
    )
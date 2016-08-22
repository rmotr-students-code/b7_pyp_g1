for user in users:
    seven_days_ago = datetime.now() - timedelta(days=7)
    if user.last_login_day <= seven_days_ago:
        send_email(blalblal)


class Email(object):
    SUBJECT = None
    BODY = None

    def condition(self):
        pass
    
    def send(self):
        if self.condition():
            send_email(self.SUBJECT, self.BODY)
            
class SevenDaysUserEmail(Email):
    def __init__(self, user):
        self.user = user
    
    def condition(self):
        return self.user.last_login <= datetime.now() - timedelta(days=7)


[SevenDaysUserEmail(u).send() for u in users]



from models import User
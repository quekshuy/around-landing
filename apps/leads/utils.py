import requests
from django.conf import settings

class MailGunEmailer(object):
    '''
        This class sends out emails to anyone, via the
        mailgun service.
    '''

    def __init__(self, 
            domain=settings.MAILGUN_DOMAIN,
            apikey=settings.MAILGUN_API_KEY,
            apiurl=settings.MAILGUN_API_URL):
        self.send_url = '/'.join([apiurl, domain, 'messages'])
        self.apikey = apikey

    def post_message(self, from_email, to_emails, subject, text):
        r = requests.\
                post(self.send_url,
                        auth=('api', self.apikey),
                        data={
                                'from': from_email,
                                'to': to_emails,
                                'subject': subject,
                                'text': text
                                }
                )
        return r
        

default_mailer = MailGunEmailer()


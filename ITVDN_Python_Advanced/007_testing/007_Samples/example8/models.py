import uuid
from utils import send_mail

SUBJECT_REGISTRATION = 'Welcome, {name}!'
BODY_REGISTRATION = 'You are welcome!'


class User:

    def __init__(self, email, first_name, last_name, uid=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = uid or uuid.uuid4()

    def get_full_name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name,
            last_name=self.last_name
        )

    def send_mail(self):
        send_mail(
            self.email,
            SUBJECT_REGISTRATION.format(name=self.get_full_name()),
            BODY_REGISTRATION
        )

    def __str__(self):
        return 'User: <{id}: {name}>'.format(
            id=self.id,
            name=self.get_full_name()
        )

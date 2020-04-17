def send_mail(email: str, subject: str, body: str):
    print(email, subject, body)


def concat_name(first_name: str, last_name: str):
    return '{first_name} {last_name}'.format(
        first_name=first_name,
        last_name=last_name
    )


def set_user_meta(instance, value: dict):
    instance.meta = value

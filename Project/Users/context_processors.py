import datetime

from Users.models import User

def extras(request):
    now = datetime.date.today()
    users = User.objects.filter(
        birthday_date__month=now.month,
        birthday_date__day=now.day,
    )
    return {'users_with_birthday': users}

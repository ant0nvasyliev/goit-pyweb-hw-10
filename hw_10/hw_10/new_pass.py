from django.contrib.auth.models import User

# Отримуємо всіх суперкористувачів
superusers = User.objects.filter(is_superuser=True)

# Виводимо їх імена користувачів
for user in superusers:
    print(user.username)
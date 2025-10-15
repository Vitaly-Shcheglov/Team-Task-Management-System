from django.core.management.base import BaseCommand, CommandError
from users.models import User
import getpass

class Command(BaseCommand):
    help = 'Регистрирует нового суперпользователя'

    def add_arguments(self, parser):
        parser.add_argument('--email', type=str, required=True,
            help="Электронная почта суперпользователя (логин)")
        parser.add_argument('--first_name', type=str, required=True,
            help="Имя суперпользователя")
        parser.add_argument('--middle_name', type=str, default='',
            help="Отчество суперпользователя (необязательно)")
        parser.add_argument('--last_name', type=str, required=True,
            help="Фамилия суперпользователя")
        parser.add_argument('--password', type=str,
            help="Пароль суперпользователя (если не указан, будет запрошен)")

    def handle(self, *args, **options):
        email = options['email']
        first_name = options['first_name']
        middle_name = options.get('middle_name', '')
        last_name = options['last_name']
        password = options.get('password')
        if not password:
            password = getpass.getpass("Введите пароль: ")

        try:
            user = User.objects.create_superuser(
                email=email,
                password=password,
                extrafields={
                    "first_name": first_name,
                    "middle_name": middle_name,
                    "last_name": last_name,
                }
            )
        except Exception as e:
            raise CommandError(f"Ошибка при создании суперпользователя: {e}")

        self.stdout.write(self.style.SUCCESS(
            f"Суперпользователь {user.email} успешно зарегистрирован."
        ))

from django.core.management.base import BaseCommand, CommandError
from django.core import mail
from core.models import Email


class Command(BaseCommand):
    help = 'Help text'

    # def add_arguments(self, parser):
    #     parser.add_argument('mail', nargs='*', type=str)

    def handle(self, *args, **options):
        print(args)
        print(options)

        try:
            emails = Email.objects.all()
            for email in emails:
                print(email.email)
                with mail.get_connection() as connection:
                    mail.EmailMessage(
                        'Subscriber greeting',
                        'Thank you for subscribe me.',
                        'jill@example.com',
                        [email.email],
                        connection=connection,
                    ).send()
        except Exception:
            raise CommandError("Error!")
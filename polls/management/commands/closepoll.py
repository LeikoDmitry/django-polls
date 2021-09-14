from abc import ABC
from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll


class Command(BaseCommand, ABC):
    help = 'Closes the specified poll for voting'
    OPTION_POLL_IDS_KEY = 'poll_ids'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument(self.OPTION_POLL_IDS_KEY, nargs='+', type=int)
        parser.add_argument('--delete', action='store_true', help='Delete poll instead of closing it',)

    def handle(self, *args, **options):
        for poll_id in options[self.OPTION_POLL_IDS_KEY]:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError(f'Polls {poll_id} does not exist')
            if options['delete']:
                poll.delete()
            poll.opened = False
            poll.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully closed poll'))



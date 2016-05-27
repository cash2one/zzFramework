
import os
from KWD.models import Action, Browser

os.environ['DJANGO_SETTINGS_MODULE'] = 'Keyworddriven.settings'


Action.objects.create(action='openbrowser')
Action.objects.create(action='get')
Action.objects.create(action='sendkeys')
Action.objects.create(action='click')
Action.objects.create(action='clear')
Action.objects.create(action='wait')
Action.objects.create(action='quit')

Browser.objects.create(browser='firefox')
Browser.objects.create(browser='chrome')
Browser.objects.create(browser='ie')
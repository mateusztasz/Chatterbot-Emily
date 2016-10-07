
from django.views import generic
import Chatterbot.settings


class MainPageView(generic.ListView):
    template_name = 'Chatterbot/index.html'
    context_object_name = 'AppList'

    def get_queryset(self):
        return [app for app in Chatterbot.settings.INSTALLED_APPS if "django" not in app]



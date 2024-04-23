import logging
import requests
import user_agents
from django.http import HttpResponse
from django.conf import settings

logger = logging.getLogger('fancy-shop-logger')

class SetUserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        request.user_agent = user_agents.parse(request.META.get("HTTP_USER_AGENT"))
        logger.info("Current user-agent for {} is {}".format(request.user, request.user_agent))
        return self.get_response(request)


class BlockEdgeBrowserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
         if request.user_agent.is_mobile == 'mobile':
             logger.error("Mobile browsers are not allowed")
             return HttpResponse("<h3>Mobile browsers are not allowed</h3>", status=400)
         return self.get_response(request)


class ErrorHandlerHelperMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        return self.get_response(request)

    def process_exceptions(self, request, exception):
        if settings.DEBUG:
            exception_classname = exception.__class__.__name__
            intitle = '{}: {}'.format(exception_classname)

            url = "http://api.stackexchange.com/2.3/search"
            params = {
                "order": "desc",
                "sort": "votes",
                "pagesize": 3,
                "site": "stackoverflow",
                "intitle": intitle,
                "tagged": "django"
            }
            resp = requests.get(url, params=params)
            if resp.ok:
                questions = resp.json

            for question in questions["items"]:
                print(question["title"])
                print(question["link"])
                print(" ")
        return None
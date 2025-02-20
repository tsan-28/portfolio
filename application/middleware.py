from django.conf import settings
from django.core.cache import cache
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin



class LimitLoginAttemptsMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path == reverse('login'):
            username = request.POST.get('username')
            if username:
                cache_key = f'failed_logins_{username}'
                failed_attempts = cache.get(cache_key, 0)

                # Redirect if too many attempts
                if failed_attempts >= settings.LOGIN_ATTEMPT_LIMIT:
                    return redirect('/')

    def process_response(self, request, response):
        return response
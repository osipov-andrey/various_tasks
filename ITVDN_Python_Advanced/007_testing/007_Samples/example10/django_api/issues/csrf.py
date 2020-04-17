class DisableCSRF(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

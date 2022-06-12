from .models import AcademicSession, AcademicTerm

class SiteWideConfigs:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            current_session = AcademicSession.objects.get(current=True)
            current_term = AcademicTerm.objects.get(current=True)
        except:
            current_session = AcademicSession.objects.filter(current=False)
            current_term = AcademicTerm.objects.get(current=False)

        request.current_session = current_session
        request.current_term = current_term

        response = self.get_response(request)

        return response

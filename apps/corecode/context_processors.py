from .models import AcademicSession, AcademicTerm, SiteConfig


def site_defaults(request):
    try:
        current_session = AcademicSession.objects.get(current=True)
    except:
        current_session = AcademicSession.objects.filter(current=False)
    print(current_session) 
    current_term = AcademicTerm.objects.get(current=True)
    vals = SiteConfig.objects.all()
    contexts = {
        "current_session": current_session.name,
        "current_term": current_term.name,
    }
    for val in vals:
        contexts[val.key] = val.value

    return contexts

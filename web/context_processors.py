from .models import Event

def main_context(request):
    events=Event.objects.all()
    
    context = {
       'events' : events, 
    }
    
    return context
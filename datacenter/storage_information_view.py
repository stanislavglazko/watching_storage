from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []

    active_visits = Visit.objects.filter(leaved_at = None)
    for visit in active_visits:
        passcard = visit.passcard
        name = passcard.owner_name
        entered_at = localtime(visit.entered_at)
        duration = visit.format_duration()
        is_strange = visit.is_visit_long()
        non_closed_visit = {
          'who_entered': name,
          'entered_at': entered_at,
          'duration': duration,
          'is_strange': is_strange,
        }
        non_closed_visits.append(non_closed_visit)
      
      
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

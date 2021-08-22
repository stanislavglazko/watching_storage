from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        entered_at = visit.entered_at
        duration = visit.format_duration()
        is_strange = visit.is_visit_long()
        this_passcard_visit = {
          'entered_at': entered_at,
          'duration': duration,
          'is_strange': is_strange,
        }
        this_passcard_visits.append(this_passcard_visit)
    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

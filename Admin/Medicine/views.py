from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django_hosts import reverse

from core.Medicine.tasks import (
    extract_allergy_cause,
    extract_allergy_types,
    extract_allergy_reaction,
    load_icd10,
)
from core.Medicine.models import AllergyType, AllergyCause, AllergyReaction, ICD10


@login_required()
def medicine_home_view(request):
    allergy_type_count = AllergyType.objects.all().count()
    allergy_cause_count = AllergyCause.objects.all().count()
    allergy_reaction_count = AllergyReaction.objects.all().count()
    icd_10_count = ICD10.objects.all().count()
    context = {
        'allergy_type_count': allergy_type_count,
        'allergy_cause_count': allergy_cause_count,
        'allergy_reaction_count': allergy_reaction_count,
        'icd_10_count': icd_10_count,
    }
    return render(request, 'Admin/Medicine/home.html', context=context)


@login_required
def allergy_cause_sync(request):
    try:
        extract_allergy_cause.apply_async(kwargs={'user_id': request.user.id})
        messages.success(request, _('Command to load allergy causes launched!'))
    except Exception as e:
        messages.error(request, _('Command to load allergy causes failed! Exception raised: %s') % e)
    return redirect(reverse('medicine:home', host='admin'))


@login_required
def allergy_reaction_sync(request):
    try:
        extract_allergy_reaction.apply_async(kwargs={'user_id': request.user.id})
        messages.success(request, _('Command to load allergy reactions launched!'))
    except Exception as e:
        messages.error(request, _('Command to load allergy reactions failed! Exception raised: %s') % e)
    return redirect(reverse('medicine:home', host='admin'))


@login_required
def allergy_type_sync(request):
    try:
        extract_allergy_types.apply_async(kwargs={'user_id': request.user.id})
        messages.success(request, _('Command to load allergy types launched!'))
    except Exception as e:
        messages.error(request, _('Command to load allergy types failed! Exception raised: %s') % e)
    return redirect(reverse('medicine:home', host='admin'))


@login_required
def icd10_sync(request):
    try:
        load_icd10.apply_async(kwargs={'user_id': request.user.id})
        messages.success(request, _('Command to load ICD-10 launched!'))
    except Exception as e:
        messages.error(request, _('Command to load ICD-10 failed! Exception raised: %s') % e)
    return redirect(reverse('medicine:home', host='admin'))

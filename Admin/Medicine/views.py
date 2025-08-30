from django.contrib.auth.decorators import login_required
from django.shortcuts import render
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

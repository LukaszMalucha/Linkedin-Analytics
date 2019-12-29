from django.shortcuts import get_object_or_404

from core import models


def my_profile(user):
    """compile user profile for the view"""

    my_profile = get_object_or_404(models.MyProfile, owner=user)

    context = {'user': user, 'my_profile': my_profile}

    return context

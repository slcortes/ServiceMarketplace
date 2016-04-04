####### views.py #######

from django.db.models import Avg
from market.models import Review




def is_owner(request=None, service=None, username=None,
             args=None, if_true=None):
    '''
        is_owner(request, args, if_true)

        Args:
            request (request): request obj from view function
            service (Service model): Service to check if request.user
                is the client
            username (str): username to compate to request.user
            args (dict): arguments being passed to template
            if_true (dict): info that are going to be added to args if
                is_owner is true
        Returns:
            True/False
    '''
    # If required arguements aren't provided
    if request is None:
        return False
    elif service is None and username is None:
        return False

    # Get result (True/False)
    if service is not None:
        result = request.user == service.client
    elif username is not None:
        result = request.user.username == username

    # Add entries to args
    if args is not None:
        args['is_owner'] = result
        if if_true is not None:
            for key, value in if_true.items():
                args[key] = value

    return result




def get_avg_rating(request, username, mode):
    '''
        get_avg_rating(request, username)

        Args:
            request (request): request object from view function
            username (str): username to get ratings from
            mode (str): 'client'|'provider'. reviews from clients or providers
        Returns:
            Float. The average rating
    '''
    ratings = Review.objects.filter(user=username, account_type=mode)
    avg_rating = ratings.aggregate(Avg('rating'))
    return format(avg_rating.get('rating__avg'), '.1f')

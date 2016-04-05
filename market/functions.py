####### views.py #######

from django.db.models import Avg
from market.models import Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




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
    
    if avg_rating.get('rating__avg') is None:
        return 0
    else:
        return format(avg_rating.get('rating__avg'), '.2f')
    
    
    
    
def paginate(request, objects_list, per_page=1):
    '''
        paginate(request, objects_list, per_page)

        Args:
            request (request): request object from view function
            objects_list (list/tuple/QuerySet...): a sliceable object with a count() or __len__() methods
            per_page (int): max number of objects to be displayed per page. default is 1
        Returns:
            Page. a Page object with given page index (i.e. paginator.page(1) will return a Page obj with index/page 1)
    '''
    paginator = Paginator(objects_list, per_page)  
        
    page = request.GET.get('page', '1')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)

    return objects

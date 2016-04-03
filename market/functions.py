####### views.py #######


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

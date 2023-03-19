from django.http import JsonResponse
from main.models import Restaurant
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from main.exceptions.UserException import UserException

import json


@csrf_exempt
def restaurants(request, id=None):
    try:
        if request.method == 'GET' and id != None:
            restaurant = restaurant_exists(id)
            return JsonResponse({'data': list(Restaurant.objects.filter(id=id).values())})

        elif request.method == 'GET':
            return JsonResponse({'data': list(Restaurant.objects.all().values())})

        elif request.method == 'POST':
            restaurant_information = validate_restaurant_data(request)
            restaurant = Restaurant(**restaurant_information)
            restaurant.save()
            return JsonResponse({'data': model_to_dict(restaurant)})

        elif request.method == 'PUT':
            restaurant_information = validate_restaurant_data(request)
            restaurant = restaurant_exists(id)
            restaurant.update(**restaurant_information)
            return JsonResponse({'data': list(restaurant.values())[0]})

        elif request.method == 'DELETE':
            restaurant = restaurant_exists(id)
            restaurant.delete()
            return JsonResponse({'message': 'Restaurant with id: ' + id + ' deleted succesfully'})

    except Exception as e:
        if isinstance(e, UserException):
            return JsonResponse({'error': e.message}, status=e.status)
        else:
            return JsonResponse({'error': 'Internal server error'}, status=500)


def statistics(request):
    return JsonResponse(data)


def validate_restaurant_data(request):
    restaurant_information = json.loads(request.body.decode('utf-8'))

    if None in restaurant_information.values() or not set(['id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng']).issubset(restaurant_information.keys()):
        raise UserException(
            'Make sure all of the following information is present: id,rating, name, site, email, phone, street, city, state, lat, lng', 400)

    return restaurant_information


def restaurant_exists(id):
    if id == None:
        raise UserException('You must provide a restaurant id', 400)

    restaurant = Restaurant.objects.filter(id=id)

    if len(restaurant) == 0:
        raise UserException(
            'The restaurant you are looking for does not exist', 404)

    return restaurant

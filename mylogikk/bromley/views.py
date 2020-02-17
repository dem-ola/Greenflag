from django.shortcuts import render
from django.http import JsonResponse
import urllib3

def total(request):
    ''' sums up a range of numbers from an api endpoint
        assumptions:
        api = '/total?range= <int:positive integer>' <- inclusive 
        e.g. range=4 sums up 1, 2, 3, 4
        else if no 'range' then returns 0 

        >>> total(urllib3.PoolManager().request('GET',"https://localhost:8000/total?range=4"))
        10
    '''
    total = 0
    print(request)
    rng = request.GET.get('range')
    if rng is not None:
        total = sum(list(range(int(rng)+1)))
    data = {'total':total}
    return JsonResponse(data)


if __name__ == "__main__":
    # could not get doctest to work as would  
    # recognise neither requests nor urllib3 modules 
    import doctest
    doctest.testmod()
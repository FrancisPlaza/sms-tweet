from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from xml.dom import minidom


@csrf_exempt
def process(request):
    dom = minidom.parseString(request.body)
    xmlList = dom.getElementsByTagName('param')
    s = ''
    for i in xmlList:
        name = i.getElementsByTagName('name')[0].childNodes[0]
        try:
            value = i.getElementsByTagName('value')[0].childNodes[0]
        except IndexError:
            s += '%s: None\n' % name.nodeValue
        else:
            s += '%s: %s\n' % (name.nodeValue, value.nodeValue)
    return HttpResponse(s)

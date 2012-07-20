from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from xml.dom import minidom
from smstweet.models import *

def updateIncomingText(entry):
    new = IncomingText(msgType = entry['messageType'],
                    msgId = entry['id'],
                    source = entry['source'],
                    target = entry['target'],
                    msg = entry['msg'],
                    udh = entry['udh'])
    new.save()
    return new.id

@csrf_exempt
def process(request):
    if request.method != 'POST':
        raise Http404
    dom = minidom.parseString(request.body)
    xmlList = dom.getElementsByTagName('param')
    entry = {}
    for i in xmlList:
        name = i.getElementsByTagName('name')[0].childNodes[0]
        try:
            value = i.getElementsByTagName('value')[0].childNodes[0]
        except IndexError:
            entry[name.nodeValue] = ''
        else:
            entry[name.nodeValue] = value.nodeValue
    updateIncomingText(entry)
    return HttpResponse('Success')

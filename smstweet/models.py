from django.db import models

class IncomingSMS(models.Model):
    msgType = CharField('Message Type', max_length=5)
    msgId = CharField('Message ID', max_length=50)
    source = CharField('Source', max_length=11)
    target = CharField('Target', max_length=8)
    msg = CharField('Message', max_length=200)
    udh = CharField('User Data Header', max_length=200)

    def __unicode__(self):
        return u'(%s) %s' % (self.source, self.msgType)

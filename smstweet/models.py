from django.db import models

class IncomingSMS(models.Model):
    msgType = models.CharField('Message Type', max_length=5)
    msgId = models.CharField('Message ID', max_length=50)
    source = models.CharField('Source', max_length=11)
    target = models.CharField('Target', max_length=8)
    msg = models.CharField('Message', max_length=200)
    udh = models.CharField('User Data Header', max_length=200)
    timestamp = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u'(%s) %s' % (self.source, self.msgType)

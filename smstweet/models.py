from django.db import models

class IncomingText(models.Model):
    msgType = models.CharField('Message Type', max_length=5)
    msgId = models.CharField('Message ID', max_length=50)
    source = models.CharField('Source', max_length=11)
    target = models.CharField('Target', max_length=8)
    msg = models.TextField('Message', blank=True)
    udh = models.TextField('User Data Header', blank=True)
    timestamp = models.DateTimeField('Timestamp', auto_now_add=True)

    def __unicode__(self):
        return u'(%s) %s' % (self.source, self.msgType)

Globe SMS Tweet Application
===========================

sms-tweet is a Django powered application that processes XML
POST from Globe Labs SMS API

How to use
----------

1. Assuming you have latest versions of Python and Django installed,
you can run this as your typical Django application.

2. Deploy this application to a publicly accessible server. If you
don't have a personal server you can use GAE or Heroku.

3. Tell Globe Labs of your callback URL. If you have not changed
anything in the urls.py, it should be something like http://yourserver.tld/process/

4. Test the application by sending an SMS to your Globe Labs assigned
number. It should be something 2373 + assigned number. Go to your
Django homepage and it should display the message(s) sent.

Example
-------

Using Globe Labs SMS API to send to a special number 23737390,
Globe Labs will send an XML POST request to the callback URL
http://sms-tweet.herokuapp.com/process/



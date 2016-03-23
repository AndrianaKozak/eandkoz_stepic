#bind='0.0.0.0:8000'
#accesslog='/home/box/web/gunicorn_access.log'
#errorlog='/home/box/web/gunicorn_error.log'
#pythonpath='/usr/bin/python2.7'
#pidfile='home/box/web/gupid.pid'

CONFIG = {
    #'mode': 'wsgi',
    'working_dir': '/home/box/web/ask/ask',
    'args': (
        '--bind=0.0.0.0:8000',
        #'--workers=2',
        #'--timeout=60',
        '--log-level=debug',
        #'--python-path=/home/box/web/ask/ask',
        'wsgi:application',
    ),
    }

import os

config = {
    'secret': os.environ.get('OPENSHIFT_SECRET_TOKEN'),
    'log_level': 'DEBUG',
    'system_plugins': ['tiddlywebwiki'],
    'twanager_plugins': ['tiddlywebwiki'],
    'server_store': ['text', {
        'store_root': os.path.join(
            os.environ.get('OPENSHIFT_DATA_DIR'), 'store'}],
    'server_host': {
        'scheme': 'http',
        'host': os.environ.get('OPENSHIFT_APP_DNS'),
        'port': os.environ.get('OPENSHIFT_PYTHON_PORT'),
    },
}

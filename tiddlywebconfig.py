import os

config = {
# Packages from which default tiddlers are copied into the instance.
    'instance_pkgstores': ['tiddlywebplugins.console', 'tiddlywebwiki'],
# Used when generating auth cookies. Only comes into play if users are
# created and policies on bags and recipes defined.
    'secret': os.environ.get('OPENSHIFT_SECRET_TOKEN'),
# Write details of activity to a tiddlyweb.log file.
    'log_level': 'DEBUG',
# Ensure the tiddlywebwiki plugin is present.
    'system_plugins': ['tiddlywebwiki'],
    'twanager_plugins': ['tiddlywebwiki'],
# Establish the location of the tiddler store in the
# OPENSHIFT_DATA_DIR.
    'server_store': ['text', {
        'store_root': os.path.join(
            os.environ.get('OPENSHIFT_DATA_DIR'), 'store')}],
# Set the hostname the service will know itself as.
    'server_host': {
        'scheme': 'http',
        'host': os.environ.get('OPENSHIFT_APP_DNS'),
        'port': '80'
    },
}

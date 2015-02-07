
This provides the basic workings for running TiddlyWeb and
TiddlyWebWiki on OpenShift without requiring any specific
configuration. The deployment process configures things properly and
then creates the necessary recipes, bags and tiddlers using a deploy
action hook in `.openshift/action_hooks/deploy`.

The files here are:

* requirements.txt
  * Lists the required Python packages. Sub dependencies are handled
    automatically.
* setup.py
  * This is where you list information. I've made no changes here.
* tiddlywebconfig.py
  * The config used by TiddlyWeb.
* wsgi.py
  * A copy of `wsgiapp.py` from the [TiddlyWeb
    repo](https://github.com/tiddlyweb/tiddlyweb). This replaces the
    pre-existing wsgi.py.
* .openshift/action_hooks/deploy
  * Installs the necessary entities.
  
Look in the files themselves for additional comments.

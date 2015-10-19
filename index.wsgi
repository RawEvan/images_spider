import sae
from simpleWeb import wsgi
	
application = sae.create_wsgi_app(wsgi.application)
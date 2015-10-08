import sae

def app(environ, start_response):
	status = '200 OK'
	resonse_headers = [('content-type', 'text/plain')]
	start_response(status, resonse_headers)
	return ['Hello evan']
	
application = sae.create_wsgi_app(app)
# Run static server
import staitic
from gevent.pywsgi import WSGIServer

http_server = WSGIServer(('0.0.0.0', 8080), staitic.app)
http_server.serve_forever()
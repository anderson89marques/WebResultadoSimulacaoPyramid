from pyramid.config import Configurator
from pyramid.renderers import JSONP

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('teste', '/')
    config.add_route('home', 'home')
    config.add_route('ajaxteste', 'resposta_ajax')
    config.scan(".views")
    return config.make_wsgi_app()

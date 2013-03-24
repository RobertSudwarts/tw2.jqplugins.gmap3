import tw2.core as twc
from tw2.core.resources import encoder
from tw2.jquery import jquery_js

gmap3_js = twc.JSLink(modname=__name__, 
                      filename='static/gmap3v5.0b/gmap3.min.js'
                      )
google_map_api_js = twc.JSLink(link='http://maps.googleapis.com/maps/api/js?sensor=false')



class gmap3(twc.Widget):
    #template = "genshi:tw2.tw2.jqplugins.gmap3.templates.tw2.jqplugins.gmap3"
    template = "mako:tw2.jqplugins.gmap3.templates.gmap3"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [jquery_js, google_map_api_js, gmap3_js]

    css_class = "gmap3"

    @classmethod
    def post_define(cls):
        pass
        # put custom initialisation code here

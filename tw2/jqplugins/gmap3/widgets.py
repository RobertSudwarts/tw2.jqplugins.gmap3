import tw2.core as twc
from tw2.core.resources import encoder
from tw2.jquery import jquery_js


gmap3_js = twc.JSLink(modname=__name__, 
                      filename='static/gmap3v5.0b/gmap3.min.js'
                      )
google_map_api_js = twc.JSLink(link='http://maps.googleapis.com/maps/api/js?sensor=false')



class gmap3(twc.Widget):
    
    template = "mako:tw2.jqplugins.gmap3.templates.gmap3"

    resources = [jquery_js, google_map_api_js, gmap3_js]

    # Important! Google maps requires a non-null 
    # height and width div, rather than adding these
    # via css (and an additional CSSSource) this is 
    # accomplished via params passed to the template.
    width = twc.Param('width', default="600px")
    height = twc.Param('height', default="300px")

    options = twc.Param("Configurations options for gmap3", default={})

    css_class = "gmap3"

    def prepare(self):
        self.options = encoder.encode(self.options)
        super(gmap3, self).prepare()
            

    @classmethod
    def post_define(cls):
        pass
        # put custom initialisation code here

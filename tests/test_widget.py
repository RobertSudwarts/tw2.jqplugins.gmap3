from tw2.core.testbase import WidgetTest
from tw2.tw2.jqplugins.gmap3 import *

class TestTw2.jqplugins.gmap3(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = Tw2.jqplugins.gmap3
    # Initilization args. go here 
    attrs = {'id':'tw2.jqplugins.gmap3-test'}
    params = {}
    expected = """<div id="tw2.jqplugins.gmap3-test"></div>"""

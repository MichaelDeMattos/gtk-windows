#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import os
import base64
import zlib

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

ui = Gtk.Builder()
jn_b64_decode = base64.b64decode(b'eJydVcFu2zAMvfcrOF0H12mHAjvELtBDuwFFL2vR3QLZpm2usuRJdNPs60fHS5vUHtLkEgjie7QeycfML18aA8/oAzmbqLPTmQK0uSvIVol6uL+OvqrL9GT+KYrgBi16zVjAkriGyugC4cvp+fnpGUSRgMgy+lLnmJ4AzD3+7shjAENZoip++qzePiS0mYrXOJf9wpwhNzqERN3w0yPZwi0VUJGoRpNdLIeLHi341rsWPa/A6gYT1f+qdIDM401wGptruyhd3gWVXmsTcB+eiQ0qYK9tMJp1ZuRyhUL/hsY4eHTGF3Bz9xDffr97+LkvXYGl7gyLnoJrlZ5fXHyUUSNVNfeU2T4K5c4uhqLotjWUa5aKh2jdHIs84geqrDavHwzs3UpBrW1h0CdKu0XeZ/ELbBZBk1cQlpIZpTvWDT2ULHlNphjO/ZuMTEHtTIF+A4i3EO/Qowm4ci9D+6tMThvcWOszBZKeqPTed6NmHjMAUxznCS2vq6hSGWCWYphJ4o6qaWW3OkMzaDPr4zb8CIHHipziNdpX4jaDpUzaaDT3sPwwoIfS2LWHkzLH7JoDeEOpp3wMvXshhrV/gQKsXOeh7FtefDS7rAJqA/2RNjVUiGv+S9TMnrKOMewGtkP/kpbOciRuzGVpatPJzQ95PFyJp+BstrHdKz2eTj2PhwncuWt1/iTrfY+ol1Y2wGGDV5IxhzFaF2gw1mivbQSMXruzSd5L3Aq+Bebx1j/TX/iEJ1w=')
jn_decompress = zlib.decompress(jn_b64_decode)
ui.add_from_string(jn_decompress.decode("utf-8"))

"""
Base64 code generated with mattos-codec-base64 Copyright (C) 
Copying and distribution of this file, with or without modification,
are permitted in any medium without royalty provided the copyright
notice and this notice are preserved.  This file is offered as-is,
without any warranty.

Author: Michael de Mattos
github: https://github.com/MichaelDeMattos/mattos-codec-base64
"""

class Handler(object):

    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # --> carrega estilo da aplicação
        self.style_application()
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # --> Destrui aplicação
    def ao_clicar_em_sair(self, *args):
        print("clicou em sair", args)
        Gtk.main_quit()
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # --> Estilo da aplicação         
    def style_application(self, *args):
        style = "/home/michael/gtk-windows/style/class.css"
        #style = "C:\\gtk-windows\\style\\class.css"
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(style)
        screen = Gdk.Screen()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen.get_default(),
                                              css_provider,
                                              Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

ui.connect_signals(Handler())
window = ui.get_object("main_window")
window.show_all()

if __name__ == '__main__':
    Gtk.main()

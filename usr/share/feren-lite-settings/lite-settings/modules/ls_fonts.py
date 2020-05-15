#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from GSettingsWidgets import *


class Module:
    name = "fonts"
    category = "appear"
    comment = _("Configure system fonts")

    def __init__(self, content_box):
        keywords = _("font, size, small, large")
        sidePage = SidePage(_("Fonts"), "preferences-desktop-font", keywords, content_box, module=self)
        self.sidePage = sidePage

    def on_module_selected(self):
        if not self.loaded:
            print("Loading Fonts module")

            page = SettingsPage()
            self.sidePage.add_widget(page)

            settings = page.add_section(_("Font Selection"))

            global widgetend1
            global widgetend2
            global widgetend3
            global widgetend4
            global widgetend5
            global widgetend6
            global fontdialog1
            global fontdialog2
            global fontdialog3
            
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Default font")
            widgetend1 = Gtk.Button()
            fontdialog1 = Gtk.FontChooserDialog('Pick a Font')
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xsettings Gtk FontName")
            fontdialog1.set_font(widgetstate)
            widgetend1.set_label(widgetstate)
            widgetend1.connect('clicked', self.btn_defaultfont_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend1, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Monoscape font")
            widgetend2 = Gtk.Button()
            fontdialog2 = Gtk.FontChooserDialog('Pick a Font')
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xsettings Gtk MonospaceFontName")
            fontdialog2.set_font(widgetstate)
            widgetend2.set_label(widgetstate)
            widgetend2.connect('clicked', self.btn_monofont_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend2, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Window title font")
            widgetend3 = Gtk.Button()
            fontdialog3 = Gtk.FontChooserDialog('Pick a Font')
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general title_font")
            fontdialog3.set_font(widgetstate)
            widgetend3.set_label(widgetstate)
            widgetend3.connect('clicked', self.btn_wmfont_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend3, False, True, 0)
            settings.add_row(widget)

            settings = page.add_section(_("Font Settings"))

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Enable anti-aliasing")
            widgetend4 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xsettings Xft Antialias")
            if int(widgetstate) == 1:
                widgetend4.set_state(True)
            else:
                widgetend4.set_state(False)
            widgetend4.connect('state-set', self.btn_antialiasswitch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend4, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Hinting")
            widgetstart.set_tooltip_text(_("Hinting allows for producing clear, legible text on screen."))
            widgetend5 = Gtk.ComboBoxText()
            widgetend5.append_text('None')
            widgetend5.append_text('Slight')
            widgetend5.append_text('Medium')
            widgetend5.append_text('Full')
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xsettings Xft HintStyle")
            if widgetstate == "hintnone":
                widgetstate = 0
            elif widgetstate == "hintslight":
                widgetstate = 1
            elif widgetstate == "hintmedium":
                widgetstate = 2
            elif widgetstate == "hintfull":
                widgetstate = 3
            widgetend5.connect('changed', self.on_hinting_changed)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend5, False, True, 0)
            settings.add_row(widget)
            widgetend5.set_active(int(widgetstate))

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("RGBA Order")
            widgetstart.set_tooltip_text(_("The order of subpixel elements on an LCD screen"))
            widgetend6 = Gtk.ComboBoxText()
            widgetend6.append_text('None')
            widgetend6.append_text('RGB')
            widgetend6.append_text('BGR')
            widgetend6.append_text('Vertical RGB')
            widgetend6.append_text('Vertical BGR')
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xsettings Xft RGBA")
            if widgetstate == "none":
                widgetstate = 0
            elif widgetstate == "rgb":
                widgetstate = 1
            elif widgetstate == "bgr":
                widgetstate = 2
            elif widgetstate == "vrgb":
                widgetstate = 3
            elif widgetstate == "vbgr":
                widgetstate = 4
            widgetend6.connect('changed', self.on_rgborder_changed)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend6, False, True, 0)
            settings.add_row(widget)
            widgetend6.set_active(int(widgetstate))

    def btn_defaultfont_click(self, button):
        global widgetend1
        global fontdialog1
        response = fontdialog1.run()
        fontdialog1.show()
        new_font = fontdialog1.get_font()
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xsettings","Gtk","FontName",str(new_font)])
        widgetend1.set_label(str(new_font))
        fontdialog1.hide()

    def btn_monofont_click(self, button):
        global widgetend2
        global fontdialog2
        response = fontdialog2.run()
        fontdialog2.show()
        new_font = fontdialog2.get_font()
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xsettings","Gtk","MonospaceFontName",str(new_font)])
        widgetend2.set_label(str(new_font))
        fontdialog2.hide()

    def btn_wmfont_click(self, button):
        global widgetend3
        global fontdialog3
        response = fontdialog3.run()
        fontdialog3.show()
        new_font = fontdialog3.get_font()
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","title_font",str(new_font)])
        widgetend3.set_label(str(new_font))
        fontdialog3.hide()

    def on_hinting_changed(self, dropdown):
        global widgetend5
        option=widgetend5.get_active()
        if option == 0:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xsettings","Xft","HintStyle","hintnone"])
        elif option == 1:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xsettings","Xft","HintStyle","hintslight"])
        elif option == 2:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xsettings","Xft","HintStyle","hintmedium"])
        elif option == 3:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xsettings","Xft","HintStyle","hintfull"])

    def on_rgborder_changed(self, dropdown):
        global widgetend6
        option=widgetend6.get_active()
        if option == 0:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xsettings","Xft","RGBA","none"])
        elif option == 1:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xsettings","Xft","RGBA","rgb"])
        elif option == 2:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xsettings","Xft","RGBA","bgr"])
        elif option == 3:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xsettings","Xft","RGBA","vrgb"])
        elif option == 4:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xsettings","Xft","RGBA","vbgr"])

    def btn_antialiasswitch_click(self, switch, toggled):
        global widgetend4
        if str(not widgetend4.get_state()).lower() == "true":
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xsettings","Xft","Antialias","1"])
        else:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xsettings","Xft","Antialias","0"])

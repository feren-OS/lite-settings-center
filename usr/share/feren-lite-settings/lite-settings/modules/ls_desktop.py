#!/usr/bin/python3

from gi.repository import Gio

from GSettingsWidgets import *

DESKTOP_SCHEMA = "org.nemo.desktop"
LAYOUT_KEY = "desktop-layout"
ORPHANS_KEY = "show-orphaned-desktop-icons"

DESKTOPS_ON_PRIMARY = "true::false"
DESKTOPS_ON_ALL = "true::true"
DESKTOPS_ON_NON_PRIMARY = "false::true"
DESKTOPS_ON_NONE = "false::false"


class Module:
    name = "desktop"
    category = "prefs"
    comment = _("Manage your desktop icons")

    def __init__(self, content_box):
        keywords = _("desktop, home, button, trash")
        sidePage = SidePage(_("Desktop"), "preferences-desktop-tweaks", keywords, content_box,
                            module=self)
        self.sidePage = sidePage

    def _loadCheck(self):
        if "org.nemo" in Gio.Settings.list_schemas():
            return True
        return False

    def on_module_selected(self):
        if self.loaded:
            return

        print("Loading Desktop module")

        page = SettingsPage()
        self.sidePage.add_widget(page)

        desktop_layout_options = [[DESKTOPS_ON_NONE,         _("No desktop icons")],
                                  [DESKTOPS_ON_PRIMARY,      _("Show desktop icons on primary monitor only")],
                                  [DESKTOPS_ON_NON_PRIMARY,  _("Show desktop icons on non-primary monitor(s) only")],
                                  [DESKTOPS_ON_ALL,          _("Show desktop icons on all monitors")]]

        widget = GSettingsComboBox("", DESKTOP_SCHEMA, LAYOUT_KEY, desktop_layout_options)

        settings = page.add_section(_("Icons Settings"))

        global combo1
        global widgetend2
        global widgetend3
        global widgetend4
        global widgetend5
        global widgetend6
        widget = SettingsWidget()
        widgetstart = Gtk.Label()
        widgetstart.set_markup("Icon Type")
        combo1 = Gtk.ComboBoxText()
        combo1.append_text('No Icons')
        combo1.append_text('Minimised Application Icons')
        combo1.append_text('File and Launcher Icons')
        widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfce4-desktop desktop-icons style")
        combo1.connect('changed', self.on_desktop_style_changed)
        widget.pack_start(widgetstart, False, False, 0)
        widget.pack_end(combo1, False, True, 0)
        settings.add_row(widget)
        combo1.set_active(int(widgetstate))

        widget = SettingsWidget()
        widgetstart = Gtk.Label()
        widgetstart.set_markup("Icon Size")
        ad = Gtk.Adjustment(0, 8, 192, 1, 0, 0)
        widgetend2 = Gtk.SpinButton(adjustment=ad, climb_rate=1, digits=0)
        widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfce4-desktop desktop-icons icon-size")
        widgetend2.set_value(int(widgetstate))
        widgetend2.connect('value-changed', self.btn_sizespin_click)
        widget.pack_start(widgetstart, False, False, 0)
        widget.pack_end(widgetend2, False, True, 0)
        settings.add_row(widget)

        widget = SettingsWidget()
        widgetstart = Gtk.Label()
        widgetstart.set_markup("Use custom font size")
        widgetend3 = Gtk.Switch()
        widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfce4-desktop desktop-icons use-custom-font-size")
        if widgetstate.upper() == "FALSE":
            widgetend3.set_state(False)
        else:
            widgetend3.set_state(True)
        widgetend3.connect('state-set', self.btn_customfontswitch_click)
        widget.pack_start(widgetstart, False, False, 0)
        widget.pack_end(widgetend3, False, True, 0)
        settings.add_row(widget)

        widget = SettingsWidget()
        widgetstart = Gtk.Label()
        widgetstart.set_markup("Custom Font Size")
        ad = Gtk.Adjustment(0, 0, 144, 1, 0, 0)
        widgetend4 = Gtk.SpinButton(adjustment=ad, climb_rate=1, digits=0)
        if widgetstate.upper() == "FALSE":
            widgetend4.set_sensitive(False)
        else:
            widgetend4.set_sensitive(True)
        widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfce4-desktop desktop-icons font-size")
        widgetstate = widgetstate[:widgetstate.index('.')]
        widgetstate = ( int(widgetstate) // 1 )
        widgetend4.set_value(int(widgetstate))
        widgetend4.connect('value-changed', self.btn_customfontspin_click)
        widget.pack_start(widgetstart, False, False, 0)
        widget.pack_end(widgetend4, False, True, 0)
        settings.add_row(widget)

        widget = SettingsWidget()
        widgetstart = Gtk.Label()
        widgetstart.set_markup("Use custom font size")
        widgetend5 = Gtk.Switch()
        widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfce4-desktop desktop-icons show-tooltips")
        if widgetstate.upper() == "FALSE":
            widgetend5.set_state(False)
        else:
            widgetend5.set_state(True)
        widgetend5.connect('state-set', self.btn_icontooltipsswitch_click)
        widget.pack_start(widgetstart, False, False, 0)
        widget.pack_end(widgetend5, False, True, 0)
        settings.add_row(widget)

        widget = SettingsWidget()
        widgetstart = Gtk.Label()
        widgetstart.set_markup("Custom Font Size")
        ad2 = Gtk.Adjustment(0, 0, 256, 1, 0, 0)
        widgetend6 = Gtk.SpinButton(adjustment=ad2, climb_rate=1, digits=0)
        if widgetstate.upper() == "FALSE":
            widgetend6.set_sensitive(False)
        else:
            widgetend6.set_sensitive(True)
        widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfce4-desktop desktop-icons tooltip-size")
        widgetstate = widgetstate[:widgetstate.index('.')]
        widgetstate = ( int(widgetstate) // 1 )
        widgetend6.set_value(int(widgetstate))
        widgetend6.connect('value-changed', self.btn_icontooltipsspin_click)
        widget.pack_start(widgetstart, False, False, 0)
        widget.pack_end(widgetend6, False, True, 0)
        settings.add_row(widget)

        settings = page.add_reveal_section(_("Desktop Icons"),
                                           DESKTOP_SCHEMA,
                                           LAYOUT_KEY,
                                           [DESKTOPS_ON_PRIMARY, DESKTOPS_ON_NON_PRIMARY, DESKTOPS_ON_ALL])

        options = [
            ("computer-icon-visible", _("Computer")),
            ("home-icon-visible", _("Home")),
            ("trash-icon-visible", _("Trash")),
            ("volumes-visible", _("Mounted volumes")),
            ("network-icon-visible", _("Network"))
        ]

        for key, label in options:
            settings.add_row(GSettingsSwitch(label, DESKTOP_SCHEMA, key))

        settings = page.add_reveal_section(_("Options"),
                                           DESKTOP_SCHEMA,
                                           LAYOUT_KEY,
                                           [DESKTOPS_ON_PRIMARY, DESKTOPS_ON_NON_PRIMARY, DESKTOPS_ON_ALL])

        switch = GSettingsSwitch(_("Allow icons from missing monitors to be displayed on the existing ones"),
                                 DESKTOP_SCHEMA,
                                 ORPHANS_KEY)

        settings.add_row(switch)

    def on_desktop_style_changed(self, dropdown):
        global combo1
        option=combo1.get_active()
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfce4-desktop","desktop-icons","style",str(option)])
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfce4-desktop","desktop-icons","style",str(option)])

    def btn_sizespin_click(self, spinbutton):
        global widgetend2
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfce4-desktop","desktop-icons","icon-size",str(int(widgetend2.get_value()))])

    def btn_customfontswitch_click(self, switch, toggled):
        global widgetend3
        global widgetend4
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfce4-desktop","desktop-icons","use-custom-font-size",str(not widgetend3.get_state()).lower()])
        if str(not widgetend3.get_state()).upper() == "FALSE":
            widgetend4.set_sensitive(False)
        else:
            widgetend4.set_sensitive(True)

    def btn_customfontspin_click(self, spinbutton):
        global widgetend4
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfce4-desktop","desktop-icons","font-size",str(int(widgetend4.get_value()))])

    def btn_icontooltipsswitch_click(self, switch, toggled):
        global widgetend5
        global widgetend6
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfce4-desktop","desktop-icons","show-tooltips",str(not widgetend5.get_state()).lower()])
        if str(not widgetend5.get_state()).upper() == "FALSE":
            widgetend6.set_sensitive(False)
        else:
            widgetend6.set_sensitive(True)

    def btn_icontooltipsspin_click(self, spinbutton):
        global widgetend6
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfce4-desktop","desktop-icons","tooltip-size",str(int(widgetend6.get_value()))])

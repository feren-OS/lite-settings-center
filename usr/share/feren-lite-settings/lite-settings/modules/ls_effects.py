#!/usr/bin/python3

from gi.repository.Gtk import SizeGroup, SizeGroupMode

from GSettingsWidgets import *

import subprocess

KEY_TEMPLATE = "desktop-effects-%s-%s"

class Module:
    name = "effects"
    category = "appear"
    comment = _("Control XFWM4 visual effects.")

    def __init__(self, content_box):
        keywords = _("effects, fancy, window")
        sidePage = SidePage(_("Effects"), "wmtweaks", keywords, content_box, module=self)
        self.sidePage = sidePage

    def on_module_selected(self):
        if not self.loaded:
            print("Loading Effects module")

            self.sidePage.stack = SettingsStack()
            self.sidePage.add_widget(self.sidePage.stack)

            page = SettingsPage()
            self.sidePage.stack.add_titled(page, "effects", _("Effects"))

            settings = page.add_section(_("Customise settings"))

            global widgetend1
            global widgetend2
            global widgetend3
            global widgetend4
            global widgetend5
            global widgetend6
            global widgetend7
            global widgetend8
            global widgetend9
            global widgetend10
            global widgetend11
            global widgetend12
            
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Enable display compositing")
            widgetend1 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general use_compositing")
            if widgetstate.upper() == "FALSE":
                widgetend1.set_state(False)
            else:
                widgetend1.set_state(True)
            widgetend1.connect('state-set', self.btn_compositeswitch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend1, False, True, 0)
            settings.add_row(widget)
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Display fullscreen overlay windows directly")
            widgetend2 = Gtk.Switch()
            if str(widgetend1.get_state()).upper() == "FALSE":
                widgetend2.set_sensitive(False)
            else:
                widgetend2.set_sensitive(True)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general unredirect_overlays")
            if widgetstate.upper() == "FALSE":
                widgetend2.set_state(False)
            else:
                widgetend2.set_state(True)
            if widgetstate.upper() == "FALSE":
                widgetend2.set_state(False)
            else:
                widgetend2.set_state(True)
            widgetend2.connect('state-set', self.btn_widget2switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend2, False, True, 0)
            settings.add_row(widget)
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Synchronize drawing to the vertical blank")
            widgetend3 = Gtk.Switch()
            if str(widgetend1.get_state()).upper() == "FALSE":
                widgetend3.set_sensitive(False)
            else:
                widgetend3.set_sensitive(True)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general sync_to_vblank")
            if widgetstate.upper() == "FALSE":
                widgetend3.set_state(False)
            else:
                widgetend3.set_state(True)
            if widgetstate.upper() == "FALSE":
                widgetend3.set_state(False)
            else:
                widgetend3.set_state(True)
            widgetend3.connect('state-set', self.btn_widget3switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend3, False, True, 0)
            settings.add_row(widget)
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Show window's preview in place of icons when cycling through windows")
            widgetend4 = Gtk.Switch()
            if str(widgetend1.get_state()).upper() == "FALSE":
                widgetend4.set_sensitive(False)
            else:
                widgetend4.set_sensitive(True)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general cycle_preview")
            if widgetstate.upper() == "FALSE":
                widgetend4.set_state(False)
            else:
                widgetend4.set_state(True)
            if widgetstate.upper() == "FALSE":
                widgetend4.set_state(False)
            else:
                widgetend4.set_state(True)
            widgetend4.connect('state-set', self.btn_widget4switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend4, False, True, 0)
            settings.add_row(widget)
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Show shadows under popup windows")
            widgetend5 = Gtk.Switch()
            if str(widgetend1.get_state()).upper() == "FALSE":
                widgetend5.set_sensitive(False)
            else:
                widgetend5.set_sensitive(True)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general show_popup_shadow")
            if widgetstate.upper() == "FALSE":
                widgetend5.set_state(False)
            else:
                widgetend5.set_state(True)
            if widgetstate.upper() == "FALSE":
                widgetend5.set_state(False)
            else:
                widgetend5.set_state(True)
            widgetend5.connect('state-set', self.btn_widget5switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend5, False, True, 0)
            settings.add_row(widget)
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Show shadows around panels and under dock windows")
            widgetend6 = Gtk.Switch()
            if str(widgetend1.get_state()).upper() == "FALSE":
                widgetend6.set_sensitive(False)
            else:
                widgetend6.set_sensitive(True)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general show_dock_shadow")
            if widgetstate.upper() == "FALSE":
                widgetend6.set_state(False)
            else:
                widgetend6.set_state(True)
            if widgetstate.upper() == "FALSE":
                widgetend6.set_state(False)
            else:
                widgetend6.set_state(True)
            widgetend6.connect('state-set', self.btn_widget6switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend6, False, True, 0)
            settings.add_row(widget)
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Show shadows under regular windows")
            widgetend7 = Gtk.Switch()
            if str(widgetend1.get_state()).upper() == "FALSE":
                widgetend7.set_sensitive(False)
            else:
                widgetend7.set_sensitive(True)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general show_frame_shadow")
            if widgetstate.upper() == "FALSE":
                widgetend7.set_state(False)
            else:
                widgetend7.set_state(True)
            if widgetstate.upper() == "FALSE":
                widgetend7.set_state(False)
            else:
                widgetend7.set_state(True)
            widgetend7.connect('state-set', self.btn_widget7switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend7, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Opacity of window decorations")
            ad1 = Gtk.Adjustment(0, 0, 100, 1, 0, 0)
            widgetend8 = Gtk.Scale(adjustment=ad1, digits=0)
            widgetend8.set_draw_value(False)
            if str(widgetend1.get_state()).upper() == "FALSE":
                widgetend8.set_sensitive(False)
            else:
                widgetend8.set_sensitive(True)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general frame_opacity")
            widgetend8.set_value(int(widgetstate))
            widgetend8.connect('change-value', self.btn_widget8switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend8, True, True, 0)
            settings.add_row(widget)
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Opacity of inactive windows")
            ad2 = Gtk.Adjustment(0, 0, 100, 1, 0, 0)
            widgetend9 = Gtk.Scale(adjustment=ad2, digits=0)
            widgetend9.set_draw_value(False)
            if str(widgetend1.get_state()).upper() == "FALSE":
                widgetend9.set_sensitive(False)
            else:
                widgetend9.set_sensitive(True)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general inactive_opacity")
            widgetend9.set_value(int(widgetstate))
            widgetend9.connect('change-value', self.btn_widget9switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend9, True, True, 0)
            settings.add_row(widget)
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Opacity of windows during move")
            ad3 = Gtk.Adjustment(0, 0, 100, 1, 0, 0)
            widgetend10 = Gtk.Scale(adjustment=ad3, digits=0)
            widgetend10.set_draw_value(False)
            if str(widgetend1.get_state()).upper() == "FALSE":
                widgetend10.set_sensitive(False)
            else:
                widgetend10.set_sensitive(True)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general move_opacity")
            widgetend10.set_value(int(widgetstate))
            widgetend10.connect('change-value', self.btn_widget10switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend10, True, True, 0)
            settings.add_row(widget)
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Opacity of windows during resize")
            ad4 = Gtk.Adjustment(0, 0, 100, 1, 0, 0)
            widgetend11 = Gtk.Scale(adjustment=ad4, digits=0)
            widgetend11.set_draw_value(False)
            if str(widgetend1.get_state()).upper() == "FALSE":
                widgetend11.set_sensitive(False)
            else:
                widgetend11.set_sensitive(True)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general resize_opacity")
            widgetend11.set_value(int(widgetstate))
            widgetend11.connect('change-value', self.btn_widget11switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend11, True, True, 0)
            settings.add_row(widget)
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Opacity of popup windows")
            ad5 = Gtk.Adjustment(0, 0, 100, 1, 0, 0)
            widgetend12 = Gtk.Scale(adjustment=ad5, digits=0)
            widgetend12.set_draw_value(False)
            if str(widgetend1.get_state()).upper() == "FALSE":
                widgetend12.set_sensitive(False)
            else:
                widgetend12.set_sensitive(True)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general popup_opacity")
            widgetend12.set_value(int(widgetstate))
            widgetend12.connect('change-value', self.btn_widget12switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend12, True, True, 0)
            settings.add_row(widget)

            self.builder = self.sidePage.builder

    def btn_compositeswitch_click(self, switch, toggled):
        global widgetend1
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","use_compositing",str(not widgetend1.get_state()).lower()])
        if str(widgetend1.get_state()).upper() == "TRUE":
            widgetend2.set_sensitive(False)
            widgetend3.set_sensitive(False)
            widgetend4.set_sensitive(False)
            widgetend5.set_sensitive(False)
            widgetend6.set_sensitive(False)
            widgetend7.set_sensitive(False)
            widgetend8.set_sensitive(False)
            widgetend9.set_sensitive(False)
            widgetend10.set_sensitive(False)
            widgetend11.set_sensitive(False)
            widgetend12.set_sensitive(False)
        else:
            widgetend2.set_sensitive(True)
            widgetend3.set_sensitive(True)
            widgetend4.set_sensitive(True)
            widgetend5.set_sensitive(True)
            widgetend6.set_sensitive(True)
            widgetend7.set_sensitive(True)
            widgetend8.set_sensitive(True)
            widgetend9.set_sensitive(True)
            widgetend10.set_sensitive(True)
            widgetend11.set_sensitive(True)
            widgetend12.set_sensitive(True)

    def btn_widget2switch_click(self, switch, toggled):
        global widgetend2
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","unredirect_overlays",str(not widgetend2.get_state()).lower()])

    def btn_widget3switch_click(self, switch, toggled):
        global widgetend3
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","sync_to_vblank",str(not widgetend3.get_state()).lower()])

    def btn_widget4switch_click(self, switch, toggled):
        global widgetend4
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","cycle_preview",str(not widgetend4.get_state()).lower()])

    def btn_widget5switch_click(self, switch, toggled):
        global widgetend5
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","show_popup_shadow",str(not widgetend5.get_state()).lower()])

    def btn_widget6switch_click(self, switch, toggled):
        global widgetend6
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","show_dock_shadow",str(not widgetend6.get_state()).lower()])

    def btn_widget7switch_click(self, switch, toggled):
        global widgetend7
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","show_frame_shadow",str(not widgetend7.get_state()).lower()])

    def btn_widget8switch_click(self, scale, dunno, dunnoeither):
        global widgetend8
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","frame_opacity",str(int(widgetend8.get_value()))])

    def btn_widget9switch_click(self, scale, dunno, dunnoeither):
        global widgetend9
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","inactive_opacity",str(int(widgetend9.get_value()))])

    def btn_widget10switch_click(self, scale, dunno, dunnoeither):
        global widgetend10
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","move_opacity",str(int(widgetend10.get_value()))])

    def btn_widget11switch_click(self, scale, dunno, dunnoeither):
        global widgetend11
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","resize_opacity",str(int(widgetend11.get_value()))])

    def btn_widget12switch_click(self, scale, dunno, dunnoeither):
        global widgetend12
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","popup_opacity",str(int(widgetend12.get_value()))])

    def make_effect_group(self, group_label, key, effects=None):
        tmin, tmax, tstep, tdefault = (0, 2000, 50, 200)

        row = SettingsWidget()
        row.set_spacing(5)

        label = SettingsLabel()
        label.set_margin_right(5)
        label.set_markup(group_label)
        label.props.xalign = 0.0
        row.pack_start(label, False, False, 0)

        label = Gtk.Label(_("ms"))
        row.pack_end(label, False, False, 0)

        effect = GSettingsEffectChooserButton(SCHEMA, KEY_TEMPLATE % (key, "effect"), DEP_PATH, effects)
        self.size_group.add_widget(effect)
        tween = GSettingsTweenChooserButton(SCHEMA, KEY_TEMPLATE % (key, "transition"), DEP_PATH)
        self.size_group.add_widget(tween)
        time = GSettingsSpinButton("", SCHEMA, KEY_TEMPLATE % (key, "time"), dep_key=DEP_PATH, mini=tmin, maxi=tmax, step=tstep, page=tdefault)
        time.set_border_width(0)
        time.set_margin_right(0)
        time.set_margin_left(0)
        time.set_spacing(0)
        row.pack_end(time, False, False, 0)
        row.pack_end(tween, False, False, 0)
        row.pack_end(effect, False, False, 0)

        return row

    def is_custom(self):
        effects = []
        transitions = []
        times = []

        for i in TYPES:
            effects.append(self.schema.get_string(KEY_TEMPLATE % (i, "effect")))
            transitions.append(self.schema.get_string(KEY_TEMPLATE % (i, "transition")))
            times.append(self.schema.get_int(KEY_TEMPLATE % (i, "time")))

        value = (tuple(effects), tuple(transitions), tuple(times))
        return value != self.effect_sets[self.chooser.value]

    def on_value_changed(self, widget):
        value = self.effect_sets[self.schema.get_string("desktop-effects-style")]
        j = 0
        for i in TYPES:
            self.schema.set_string(KEY_TEMPLATE % (i, "effect"), value[0][j])
            self.schema.set_string(KEY_TEMPLATE % (i, "transition"), value[1][j])
            self.schema.set_int(KEY_TEMPLATE % (i, "time"), value[2][j])
            j += 1

    def update_effects(self, switch, gparam):
        active = switch.get_active()

        self.revealer.set_reveal_child(active)
        #when unchecking the checkbutton, reset the values
        if not active:
            self.on_value_changed(self.chooser)

    def on_desktop_effects_enabled_changed(self, schema, key):
        active = schema.get_boolean(key)

        if not active and schema.get_boolean("desktop-effects-on-dialogs"):
            schema.set_boolean("desktop-effects-on-dialogs", False)

        if not active and schema.get_boolean("desktop-effects-on-menus"):
            schema.set_boolean("desktop-effects-on-menus", False)

        self.update_effects(self.custom_switch, None)

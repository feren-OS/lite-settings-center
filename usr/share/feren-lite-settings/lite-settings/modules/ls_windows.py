#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio, Gtk, GObject, Gdk

from GSettingsWidgets import *


class Module:
    name = "windows"
    category = "prefs"
    comment = _("Manage window preferences")

    def __init__(self, content_box):
        keywords = _("windows, titlebar, edge, switcher, window list, attention, focus")
        sidePage = SidePage(_("Windows"), "xfwm4", keywords, content_box, module=self)
        self.sidePage = sidePage

    def on_module_selected(self):
        if not self.loaded:
            print("Loading Windows module")

            self.sidePage.stack = SettingsStack()
            self.sidePage.add_widget(self.sidePage.stack)

            # Titlebar

            page = SettingsPage()
            self.sidePage.stack.add_titled(page, "titlebar", _("Titlebar"))

            widget = TitleBarButtonsOrderSelector()
            page.add(widget)

            settings = page.add_section(_("Actions (XFWM4)"))

            global combo1
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Action on title bar double-click")
            combo1 = Gtk.ComboBoxText()
            combo1.append_text('Toggle Shade')
            combo1.append_text('Minimise')
            combo1.append_text('Toggle Maximise')
            combo1.append_text('Toggle Fill')
            combo1.append_text('Do Nothing')
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general double_click_action")
            combo1.connect('changed', self.on_title_doubleclk_changed)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(combo1, False, True, 0)
            settings.add_row(widget)
            if widgetstate == "shade":
                combo1.set_active(0)
            elif widgetstate == "hide":
                combo1.set_active(1)
            elif widgetstate == "maximize":
                combo1.set_active(2)
            elif widgetstate == "fill":
                combo1.set_active(3)
            elif widgetstate == "none":
                combo1.set_active(4)

            if os.path.exists("/usr/bin/xfwm4-settings"):
                image = Gtk.Image.new_from_icon_name("xfwm4", Gtk.IconSize.BUTTON)
                image.props.use_fallback=True
                widget = SettingsWidget()
                button = Gtk.Button(label="Open the Xfce Window Manager Settings", image=image)
                button.set_tooltip_text(_("Opens the Classic Xfce Window Manager Settings"))
                button.connect("clicked", self.on_button_clicked)
                widget.pack_start(button, True, True, 0)
                settings.add_row(widget)

            # Behavior

            page = SettingsPage()
            self.sidePage.stack.add_titled(page, "behavior", _("Behavior"))

            settings = page.add_section(_("Window Focus"))

            global combo2
            global combo3
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
            global widgetend13
            global widgetend14
            global widgetend15
            global widgetend16
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Window focus mode")
            combo2 = Gtk.ComboBoxText()
            combo2.append_text('Click To Focus')
            combo2.append_text('Hover To Focus')
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general click_to_focus")
            ad1 = Gtk.Adjustment(5, 5, 2000, 1, 0, 0)
            widgetend1 = Gtk.Scale(adjustment=ad1, digits=0)
            combo2.connect('changed', self.on_title_focus_changed)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(combo2, False, True, 0)
            settings.add_row(widget)
            if widgetstate.lower() == "true":
                combo2.set_active(0)
            else:
                combo2.set_active(1)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Delay before window receives focus")
            widgetend1.set_draw_value(False)
            if combo2.get_active() == 0:
                widgetend1.set_sensitive(False)
            else:
                widgetend1.set_sensitive(True)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general focus_delay")
            widgetend1.set_value(int(widgetstate))
            widgetend1.connect('change-value', self.btn_widget1switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend1, True, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Automatically give focus to newly created windows")
            widgetend2 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general focus_new")
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
            widgetstart.set_markup("Automatically raise focused windows")
            widgetend3 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general raise_on_focus")
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
            widgetstart.set_markup("Delay before window receives focus")
            ad2 = Gtk.Adjustment(5, 5, 2000, 1, 0, 0)
            widgetend4 = Gtk.Scale(adjustment=ad2, digits=0)
            widgetend4.set_draw_value(False)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general raise_delay")
            widgetend4.set_value(int(widgetstate))
            widgetend4.connect('change-value', self.btn_widget4switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend4, True, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Automatically raise when clicking inside application window")
            widgetend5 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general raise_on_click")
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
            widgetstart.set_markup("Prevent focus stealing")
            widgetend6 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general prevent_focus_stealing")
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
            widgetstart.set_markup("Honour standard ICCCM focus hint")
            widgetend7 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general focus_hint")
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
            widgetstart.set_markup("Window focus mode")
            combo3 = Gtk.ComboBoxText()
            combo3.append_text('Bring window on current workspace')
            combo3.append_text("Switch to window's workspace")
            combo3.append_text('Do Nothing')
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general activate_action")
            combo3.connect('changed', self.btn_widget8switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(combo3, False, True, 0)
            settings.add_row(widget)
            if widgetstate.lower() == "bring":
                combo3.set_active(0)
            elif widgetstate.lower() == "switch":
                combo3.set_active(1)
            elif widgetstate.lower() == "none":
                combo3.set_active(2)

            settings = page.add_section(_("Windows snapping"))

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("To screen borders")
            widgetend8 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general snap_to_border")
            if widgetstate.upper() == "FALSE":
                widgetend8.set_state(False)
            else:
                widgetend8.set_state(True)
            widgetend8.connect('state-set', self.btn_widget9switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend8, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("To other windows")
            widgetend9 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general snap_to_windows")
            if widgetstate.upper() == "FALSE":
                widgetend9.set_state(False)
            else:
                widgetend9.set_state(True)
            widgetend9.connect('state-set', self.btn_widget10switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend9, False, True, 0)
            settings.add_row(widget)

            settings = page.add_section(_("Hide content of windows"))

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("When moving")
            widgetend10 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general box_move")
            if widgetstate.upper() == "FALSE":
                widgetend10.set_state(False)
            else:
                widgetend10.set_state(True)
            widgetend10.connect('state-set', self.btn_widget11switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend10, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("When resizing")
            widgetend11 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general box_resize")
            if widgetstate.upper() == "FALSE":
                widgetend11.set_state(False)
            else:
                widgetend11.set_state(True)
            widgetend11.connect('state-set', self.btn_widget12switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend11, False, True, 0)
            settings.add_row(widget)

            # Other Settings

            page = SettingsPage()
            self.sidePage.stack.add_titled(page, "alttab", _("Other Settings"))

            settings = page.add_section(_("Cycling"))

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Skip windows that have 'skip pager' or 'skip taskbar' set")
            widgetend12 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general cycle_minimum")
            if widgetstate.upper() == "FALSE":
                widgetend12.set_state(False)
            else:
                widgetend12.set_state(True)
            widgetend12.connect('state-set', self.btn_widget13switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend12, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Include hidden (i.e. iconified) windows")
            widgetend13 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general cycle_hidden")
            if widgetstate.upper() == "FALSE":
                widgetend13.set_state(False)
            else:
                widgetend13.set_state(True)
            widgetend13.connect('state-set', self.btn_widget14switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend13, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Cycle through windows on all workspaces")
            widgetend14 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general cycle_workspaces")
            if widgetstate.upper() == "FALSE":
                widgetend14.set_state(False)
            else:
                widgetend14.set_state(True)
            widgetend14.connect('state-set', self.btn_widget15switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend14, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Draw frame around selected windows while cycling")
            widgetend15 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general cycle_draw_frame")
            if widgetstate.upper() == "FALSE":
                widgetend15.set_state(False)
            else:
                widgetend15.set_state(True)
            widgetend15.connect('state-set', self.btn_widget16switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend15, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Cycle through windows in a list")
            widgetend16 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general cycle_tabwin_mode")
            if widgetstate.upper() == "0":
                widgetend16.set_state(False)
            else:
                widgetend16.set_state(True)
            widgetend16.connect('state-set', self.btn_widget17switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend16, False, True, 0)
            settings.add_row(widget)

            settings = page.add_section(_("Accessibility"))
            global combo4
            global widgetend17
            global widgetend18
            global widgetend19
            global widgetend20

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Window focus mode")
            combo4 = Gtk.ComboBoxText()
            combo4.append_text('None')
            combo4.append_text('Alt')
            combo4.append_text('Control')
            combo4.append_text('Hyper')
            combo4.append_text('Meta')
            combo4.append_text('Shift')
            combo4.append_text('Super')
            combo4.append_text('Mod1')
            combo4.append_text('Mod2')
            combo4.append_text('Mod3')
            combo4.append_text('Mod4')
            combo4.append_text('Mod5')
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general easy_click")
            combo4.connect('changed', self.btn_widget18switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(combo4, False, True, 0)
            settings.add_row(widget)
            if widgetstate.lower() == "none":
                combo4.set_active(0)
            elif widgetstate.lower() == "alt":
                combo4.set_active(1)
            elif widgetstate.lower() == "control":
                combo4.set_active(2)
            elif widgetstate.lower() == "hyper":
                combo4.set_active(3)
            elif widgetstate.lower() == "meta":
                combo4.set_active(4)
            elif widgetstate.lower() == "shift":
                combo4.set_active(5)
            elif widgetstate.lower() == "super":
                combo4.set_active(6)
            elif widgetstate.lower() == "mod1":
                combo4.set_active(7)
            elif widgetstate.lower() == "mod2":
                combo4.set_active(8)
            elif widgetstate.lower() == "mod3":
                combo4.set_active(9)
            elif widgetstate.lower() == "mod4":
                combo4.set_active(10)
            elif widgetstate.lower() == "mod5":
                combo4.set_active(11)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Raise windows with any mouse button")
            widgetend17 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general raise_with_any_button")
            if widgetstate.upper() == "FALSE":
                widgetend17.set_state(False)
            else:
                widgetend17.set_state(True)
            widgetend17.connect('state-set', self.btn_widget19switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend17, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Notify of urgency by making titlebar blink")
            widgetend18 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general urgent_blink")
            if widgetstate.upper() == "FALSE":
                widgetend18.set_state(False)
            else:
                widgetend18.set_state(True)
            widgetend18.connect('state-set', self.btn_widget20switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend18, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Use mouse wheel on titlebar to roll up the window")
            widgetend19 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general mousewheel_rollup")
            if widgetstate.upper() == "FALSE":
                widgetend19.set_state(False)
            else:
                widgetend19.set_state(True)
            widgetend19.connect('state-set', self.btn_widget21switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend19, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Keep urgent windows blinking repeatedly")
            widgetend20 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general repeat_urgent_blink")
            if widgetstate.upper() == "FALSE":
                widgetend20.set_state(False)
            else:
                widgetend20.set_state(True)
            widgetend20.connect('state-set', self.btn_widget22switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend20, False, True, 0)
            if widgetend18.get_state() == True:
                widgetend20.set_sensitive(True)
            else:
                widgetend20.set_sensitive(False)
            settings.add_row(widget)

            settings = page.add_section(_("Placement"))
            global widgetend21
            global widgetend22
            global combo5

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Minimum size of windows to trigger smart placement")
            ad5 = Gtk.Adjustment(0, 0, 100, 1, 0, 0)
            widgetend21 = Gtk.Scale(adjustment=ad5, digits=0)
            widgetend21.set_draw_value(False)
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general placement_ratio")
            widgetend21.set_value(int(widgetstate))
            widgetend21.connect('change-value', self.btn_widget23switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend21, True, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("By default, place windows")
            combo5 = Gtk.ComboBoxText()
            combo5.append_text('At the centre of the screen')
            combo5.append_text("Under the mouse pointer")
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general placement_mode")
            combo5.connect('changed', self.btn_widget24switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(combo5, False, True, 0)
            settings.add_row(widget)
            if widgetstate.lower() == "center":
                combo5.set_active(0)
            elif widgetstate.lower() == "mouse":
                combo5.set_active(1)

            #WM Tweaks
            page = SettingsPage()
            self.sidePage.stack.add_titled(page, "tweaks", _("Tweaks"))

            settings = page.add_section(_("Workspaces"))
            global widgetend23
            global widgetend24
            global widgetend25
            global widgetend26
            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Use the mouse wheel on the desktop to switch workspaces")
            widgetend23 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general scroll_workspaces")
            if widgetstate.upper() == "FALSE":
                widgetend23.set_state(False)
            else:
                widgetend23.set_state(True)
            widgetend23.connect('state-set', self.btn_widget25switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend23, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Remember and recall previous workspace when switching via keyboard shortcuts")
            widgetend24 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general toggle_workspaces")
            if widgetstate.upper() == "FALSE":
                widgetend24.set_state(False)
            else:
                widgetend24.set_state(True)
            widgetend24.connect('state-set', self.btn_widget26switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend24, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Wrap workspaces depending on the actual desktop layout")
            widgetend25 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general wrap_layout")
            if widgetstate.upper() == "FALSE":
                widgetend25.set_state(False)
            else:
                widgetend25.set_state(True)
            widgetend25.connect('state-set', self.btn_widget27switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend25, False, True, 0)
            settings.add_row(widget)

            widget = SettingsWidget()
            widgetstart = Gtk.Label()
            widgetstart.set_markup("Wrap workspaces when the first or the last workspace is reached")
            widgetend26 = Gtk.Switch()
            widgetstate = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general wrap_cycle")
            if widgetstate.upper() == "FALSE":
                widgetend26.set_state(False)
            else:
                widgetend26.set_state(True)
            widgetend26.connect('state-set', self.btn_widget28switch_click)
            widget.pack_start(widgetstart, False, False, 0)
            widget.pack_end(widgetend26, False, True, 0)
            settings.add_row(widget)

    
    def on_button_clicked(self, button):
        subprocess.Popen(["xfwm4-settings"])

    def on_title_doubleclk_changed(self, dropdown):
        global combo1
        option=combo1.get_active()
        if option == 0:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","double_click_action","shade"])
        elif option == 1:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","double_click_action","hide"])
        elif option == 2:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","double_click_action","maximize"])
        elif option == 3:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","double_click_action","fill"])
        elif option == 4:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","double_click_action","none"])

    def btn_widget1switch_click(self, scale, dunno, dunnoeither):
        global widgetend1
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","focus_delay",str(int(widgetend1.get_value()))])

    def btn_widget2switch_click(self, switch, toggled):
        global widgetend2
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","focus_new",str(not widgetend2.get_state()).lower()])

    def btn_widget3switch_click(self, switch, toggled):
        global widgetend3
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","raise_on_focus",str(not widgetend3.get_state()).lower()])

    def btn_widget4switch_click(self, scale, dunno, dunnoeither):
        global widgetend4
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","raise_delay",str(int(widgetend4.get_value()))])

    def btn_widget5switch_click(self, switch, toggled):
        global widgetend5
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","raise_on_click",str(not widgetend5.get_state()).lower()])

    def btn_widget6switch_click(self, switch, toggled):
        global widgetend6
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","prevent_focus_stealing",str(not widgetend6.get_state()).lower()])
    
    def btn_widget7switch_click(self, switch, toggled):
        global widgetend7
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","focus_hint",str(not widgetend7.get_state()).lower()])

    def btn_widget8switch_click(self, dropdown):
        global combo3
        option=combo3.get_active()
        if option == 0:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","activate_action","bring"])
        elif option == 1:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","activate_action","switch"])
        elif option == 2:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","activate_action","none"])

    def btn_widget9switch_click(self, switch, toggled):
        global widgetend8
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","snap_to_border",str(not widgetend8.get_state()).lower()])
    
    def btn_widget10switch_click(self, switch, toggled):
        global widgetend9
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","snap_to_windows",str(not widgetend9.get_state()).lower()])

    def btn_widget11switch_click(self, switch, toggled):
        global widgetend10
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","box_move",str(not widgetend10.get_state()).lower()])

    def btn_widget12switch_click(self, switch, toggled):
        global widgetend11
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","box_resize",str(not widgetend11.get_state()).lower()])

    def btn_widget13switch_click(self, switch, toggled):
        global widgetend12
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","cycle_minimum",str(not widgetend12.get_state()).lower()])

    def btn_widget14switch_click(self, switch, toggled):
        global widgetend13
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","cycle_hidden",str(not widgetend13.get_state()).lower()])

    def btn_widget15switch_click(self, switch, toggled):
        global widgetend14
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","cycle_workspaces",str(not widgetend14.get_state()).lower()])

    def btn_widget16switch_click(self, switch, toggled):
        global widgetend15
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","cycle_draw_frame",str(not widgetend15.get_state()).lower()])

    def btn_widget17switch_click(self, switch, toggled):
        global widgetend16
        if str(not widgetend16.get_state()).lower() == "false":
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","cycle_tabwin_mode","0"])
        else:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","cycle_tabwin_mode","1"])

    def btn_widget18switch_click(self, dropdown):
        global combo4
        option=combo4.get_active()
        if option == 0:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","easy_click","None"])
        elif option == 1:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","easy_click","Alt"])
        elif option == 2:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","easy_click","Control"])
        elif option == 3:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","easy_click","Hyper"])
        elif option == 4:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","easy_click","Meta"])
        elif option == 5:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","easy_click","Shift"])
        elif option == 6:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","easy_click","Super"])
        elif option == 7:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","easy_click","Mod1"])
        elif option == 8:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","easy_click","Mod2"])
        elif option == 9:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","easy_click","Mod3"])
        elif option == 10:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","easy_click","Mod4"])
        elif option == 11:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","easy_click","Mod5"])

    def btn_widget19switch_click(self, switch, toggled):
        global widgetend17
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","raise_with_any_button",str(not widgetend17.get_state()).lower()])
    
    def btn_widget20switch_click(self, switch, toggled):
        global widgetend18
        global widgetend20
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","urgent_blink",str(not widgetend18.get_state()).lower()])
        if str(not widgetend18.get_state()).lower() == "true":
            widgetend20.set_sensitive(True)
        else:
            widgetend20.set_sensitive(False)

    def btn_widget21switch_click(self, switch, toggled):
        global widgetend19
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","mousewheel_rollup",str(not widgetend19.get_state()).lower()])

    def btn_widget22switch_click(self, switch, toggled):
        global widgetend20
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","repeat_urgent_blink",str(not widgetend20.get_state()).lower()])

    def btn_widget23switch_click(self, scale, dunno, dunnoeither):
        global widgetend21
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","placement_ratio",str(int(widgetend21.get_value()))])

    def btn_widget24switch_click(self, dropdown):
        global combo5
        global widgetend22
        option=combo5.get_active()
        if option == 0:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","placement_mode","center"])
        elif option == 1:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","placement_mode","mouse"])

    def btn_widget25switch_click(self, switch, toggled):
        global widgetend23
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","scroll_workspaces",str(not widgetend23.get_state()).lower()])

    def btn_widget26switch_click(self, switch, toggled):
        global widgetend24
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","toggle_workspaces",str(not widgetend24.get_state()).lower()])

    def btn_widget27switch_click(self, switch, toggled):
        global widgetend25
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","wrap_layout",str(not widgetend25.get_state()).lower()])

    def btn_widget28switch_click(self, switch, toggled):
        global widgetend26
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","wrap_cycle",str(not widgetend26.get_state()).lower()])

    def on_title_focus_changed(self, dropdown):
        global combo2
        global widgetend1
        option=combo2.get_active()
        if option == 0:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","click_to_focus","true"])
            widgetend1.set_sensitive(False)
        elif option == 1:
            subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","click_to_focus","false"])
            widgetend1.set_sensitive(True)

class TitleBarButtonsOrderSelector(SettingsBox):
    def __init__(self):
        self.schema = "org.cinnamon.desktop.wm.preferences"
        self.key = "button-layout"

        super(TitleBarButtonsOrderSelector, self).__init__(_("Buttons (XFWM4)"))

        self.settings = Gio.Settings.new(self.schema)
        self.value = subprocess.getoutput("./bin/ManageXfconf.sh get xfwm4 general button_layout")

        left_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        left_box.set_border_width(5)
        left_box.set_margin_left(20)
        left_box.set_margin_right(20)
        left_box.set_spacing(5)

        right_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        right_box.set_border_width(5)
        right_box.set_margin_left(20)
        right_box.set_margin_right(20)
        right_box.set_spacing(5)

        try:
            left_items, right_items = self.value.split("|")
        except:
            left_items = right_items = ""
        if len(left_items) > 0:
            left_items_old = left_items
            left_items = []
            for i in left_items_old:
                left_items.append(i)
        else:
            left_items = []
        if len(right_items) > 0:
            right_items_old = right_items
            right_items = []
            for i in right_items_old:
                right_items.append(i)
        else:
            right_items = []

        left_label = Gtk.Label.new(_("Left side title bar buttons"))
        left_label.set_alignment(0.0, 0.5)
        left_label.set_line_wrap(True)
        left_box.pack_start(left_label, False, False, 0)
        left_grid = Gtk.Grid()
        left_grid.set_column_spacing(4)
        left_box.pack_end(left_grid, False, False, 0)
        left_grid.set_valign(Gtk.Align.CENTER)

        right_label = Gtk.Label.new(_("Right side title bar buttons"))
        right_label.set_alignment(0.0, 0.5)
        right_label.set_line_wrap(True)
        right_box.pack_start(right_label, False, False, 0)
        right_grid = Gtk.Grid()
        right_grid.set_column_spacing(4)
        right_box.pack_end(right_grid, False, False, 0)
        right_grid.set_valign(Gtk.Align.CENTER)

        self.left_side_widgets = []
        self.right_side_widgets = []
        for i in range(6):
            self.left_side_widgets.append(Gtk.ComboBox())
            self.right_side_widgets.append(Gtk.ComboBox())

        buttons = [
            ("", ""),
            ("O", _("Menu")),
            ("C", _("Close")),
            ("H", _("Minimize")),
            ("M", _("Maximize")),
            ("T", _("Stick")),
            ("S", _("Shade"))
        ]

        for i in self.left_side_widgets + self.right_side_widgets:
            if i in self.left_side_widgets:
                ref_list = left_items
                index = self.left_side_widgets.index(i)
            else:
                ref_list = right_items
                index = self.right_side_widgets.index(i)
            model = Gtk.ListStore(str, str)
            selected_iter = None
            for button in buttons:
                iter = model.insert_before(None, None)
                model.set_value(iter, 0, button[0])
                model.set_value(iter, 1, button[1])
                if index < len(ref_list) and ref_list[index] == button[0]:
                    selected_iter = iter
            i.set_model(model)
            renderer_text = Gtk.CellRendererText()
            i.pack_start(renderer_text, True)
            i.add_attribute(renderer_text, "text", 1)
            if selected_iter is not None:
                i.set_active_iter(selected_iter)
            i.connect("changed", self.on_my_value_changed)

        for i in self.left_side_widgets:
            index = self.left_side_widgets.index(i)
            left_grid.attach(i, index, 0, 1, 1)
            i.set_valign(Gtk.Align.CENTER)
        for i in self.right_side_widgets:
            index = self.right_side_widgets.index(i)
            right_grid.attach(i, index, 0, 1, 1)
            i.set_valign(Gtk.Align.CENTER)

        self.add_row(left_box)
        self.add_row(right_box)

    def on_my_value_changed(self, widget):
        active_iter = widget.get_active_iter()
        if active_iter:
            new_value = widget.get_model()[active_iter][0]
        else:
            new_value = None
        left_items = []
        right_items = []
        for i in self.left_side_widgets + self.right_side_widgets:
            active_iter = i.get_active_iter()
            if active_iter:
                value = i.get_model()[i.get_active_iter()][0]
                if i != widget and value == new_value:
                    i.set_active_iter(None)
                elif value != "":
                    if i in self.left_side_widgets:
                        left_items.append(value)
                    else:
                        right_items.append(value)
        subprocess.Popen(["./bin/ManageXfconf.sh","set","xfwm4","general","button_layout",(''.join(str(item) for item in left_items) + '|' + ''.join(str(item) for item in right_items))])

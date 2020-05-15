#!/usr/bin/python3

from GSettingsWidgets import *

class Module:
    name = "calendar"
    comment = _("Manage date and time settings")
    category = "prefs"

    def __init__(self, content_box):
        keywords = _("time, date, calendar, format, network, sync")
        self.sidePage = SidePage(_("Date & Time"), "preferences-system-time", keywords, content_box, 560, module=self)

    def on_module_selected(self):
        if not self.loaded:
            print("Loading Calendar module")

            page = SettingsPage()
            self.sidePage.add_widget(page)

            try:
                settings = page.add_section(_("Settings"))
                widget = SettingsWidget()
                content = self.sidePage.content_box.c_manager.get_c_widget("datetime")
                widget.pack_start(content, False, False, 0)
                settings.add_row(widget)

            except Exception as detail:
                print(detail)

"""
    Copyright (C) 2024  nghfp9wa7bzq@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import wx

from app.checklistpanel import CheckListPanel
from app.buttonpanel import ButtonPanel

from db.db import Database


class MainFrame(wx.Frame):
    def __init__(self, parent, **kwargs):
        wx.Frame.__init__(self, parent, **kwargs)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self.clp = CheckListPanel(self)

        self.db = Database()
        self.clp.set_data(self.db.get_table_names())

        sizer.Add(self.clp, 1, wx.EXPAND | wx.ALL, 10)
        sizer.Add(ButtonPanel(self), 0, wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.LEFT, 10)

    def on_save_button(self):
        selected_tables = self.clp.get_selected()
        print("Selected for save:", selected_tables)
#        for table_name in selected_tables:
#            self.db.save_table_to_csv(table_name)


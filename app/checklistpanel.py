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

from app.checklistctrl import CheckListCtrl


class CheckListPanel(wx.Panel):
    def __init__(self, parent, **kwargs):
        wx.Panel.__init__(self, parent, **kwargs)

        sizer = wx.BoxSizer()
        self.SetSizer(sizer)

        self.list = CheckListCtrl(self, style=wx.LC_REPORT)
        sizer.Add(self.list, 1, wx.EXPAND)

        select_all_checkbox = wx.CheckBox(self, wx.ID_ANY, pos=(7, 2))
        select_all_checkbox.Bind(wx.EVT_CHECKBOX, self.on_select_all)

        self.list.InsertColumn(0, "")
        self.list.InsertColumn(1, "Table name")

    def set_data(self, data):

        for key, item_data in data.items():
            index = self.list.InsertItem(self.list.GetItemCount(), "")
            self.list.SetItem(index, 1, item_data[0])
            self.list.SetItemData(index, key)

        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)

    def on_select_all(self, event):
        if event.IsChecked():
            self.list.set_all()
        else:
            self.list.set_all(False)

    def get_selected(self):
        return self.list.get_selected()

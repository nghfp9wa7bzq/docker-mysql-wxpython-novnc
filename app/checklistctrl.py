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


class CheckListCtrl(wx.ListCtrl):
    def __init__(self, parent, **kwargs):
        wx.ListCtrl.__init__(self, parent, **kwargs)

        self.EnableCheckBoxes()
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.toggle_item)

    def toggle_item(self, event):
        self.CheckItem(event.Index, not self.IsItemChecked(event.Index))

    def map_filter_items(self, callback):
        if not self.IsEmpty():
            item = -1

            while True:
                item = self.GetNextItem(item)

                if item == -1:
                    break

                callback(item)

    def set_all(self, to_selected=True):
        self.map_filter_items(lambda x: self.CheckItem(x, to_selected))

    def get_selected(self):
        selected_tables = []
        self.map_filter_items(
            lambda x: selected_tables.append(self.GetItem(x, 1).GetText()) if self.IsItemChecked(x) else None)
        return selected_tables

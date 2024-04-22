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

import sys
import wx


class ButtonPanel(wx.Panel):
    def __init__(self, parent, **kwargs):
        wx.Panel.__init__(self, parent, **kwargs)

        sizer = wx.BoxSizer()
        self.SetSizer(sizer)

        quit_button = wx.Button(self, wx.ID_ANY, "Quit")
        self.GetParent().Bind(wx.EVT_BUTTON, self.on_quit_button_click, quit_button)
        self.GetParent().Bind(wx.EVT_CLOSE, self.on_close_window)

        save_button = wx.Button(self, wx.ID_ANY, "Save")
        self.GetParent().Bind(wx.EVT_BUTTON, self.on_save_button_click, save_button)

        sizer.Add(quit_button, 0, wx.LEFT | wx.RIGHT, 10)
        sizer.Add((-1, -1), 1)
        sizer.Add(save_button, 0, wx.LEFT | wx.RIGHT, 10)

    def on_quit_button_click(self, event):
        self.GetParent().Close(True)

    def on_save_button_click(self, event):
        self.GetParent().on_save_button()

    def on_close_window(self, event):
        self.GetParent().Destroy()

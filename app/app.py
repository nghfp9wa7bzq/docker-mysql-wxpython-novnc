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

from app.mainframe import MainFrame

app = wx.App()

frame_size = wx.Size(300, 400)

my_frame = MainFrame(None,
                     id=-1,
                     title="Database table export",
                     size=frame_size,
                     style=wx.DEFAULT_FRAME_STYLE)
my_frame.SetMinSize(frame_size)
my_frame.SetIcon(wx.Icon("app/logo.ico"))
my_frame.Show()

app.MainLoop()

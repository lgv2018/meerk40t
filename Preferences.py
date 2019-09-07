# -*- coding: ISO-8859-1 -*-
#
# generated by wxGlade 0.9.3 on Thu Jun 27 21:45:40 2019
#

import wx
# begin wxGlade: dependencies
# end wxGlade


class Preferences(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Preferences.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((406, 261))
        self.combobox_board = wx.ComboBox(self, wx.ID_ANY, choices=["M2", "B2", "M/M1", "A/B/B1"], style=wx.CB_DROPDOWN)
        self.radio_units = wx.RadioBox(self, wx.ID_ANY, "Units", choices=["mm", "cm", "inch", "mils"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.spin_bedwidth = wx.SpinCtrlDouble(self, wx.ID_ANY, "330.0", min=1.0, max=1000.0)
        self.spin_bedheight = wx.SpinCtrlDouble(self, wx.ID_ANY, "230.0", min=1.0, max=1000.0)
        self.checkbox_autolock = wx.CheckBox(self, wx.ID_ANY, "Automatically Lock Rail")
        self.checkbox_autohome = wx.CheckBox(self, wx.ID_ANY, "Home After Job complete")
        self.checkbox_autobeep = wx.CheckBox(self, wx.ID_ANY, "Beep After Job Complete")
        self.checkbox_rotary = wx.CheckBox(self, wx.ID_ANY, "Rotary")
        self.spin_scalex = wx.SpinCtrlDouble(self, wx.ID_ANY, "1.0", min=0.0, max=5.0)
        self.spin_scaley = wx.SpinCtrlDouble(self, wx.ID_ANY, "1.0", min=0.0, max=5.0)
        self.checkbox_mock_usb = wx.CheckBox(self, wx.ID_ANY, "Mock USB Connection Mode")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_combobox_boardtype, self.combobox_board)
        self.Bind(wx.EVT_RADIOBOX, self.on_radio_units, self.radio_units)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.spin_on_bedwidth, self.spin_bedwidth)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.spin_on_bedheight, self.spin_bedheight)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_autolock, self.checkbox_autolock)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_autohome, self.checkbox_autohome)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_autobeep, self.checkbox_autobeep)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.spin_on_scalex, self.spin_scalex)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_scalex, self.spin_scalex)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.spin_on_scaley, self.spin_scaley)
        self.Bind(wx.EVT_TEXT_ENTER, self.spin_on_scalex, self.spin_scaley)
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_mock_usb, self.checkbox_mock_usb)
        # end wxGlade
        self.project = None

    def set_project(self, project):
        self.project = project

    def __set_properties(self):
        # begin wxGlade: Preferences.__set_properties
        self.SetTitle("Preferences")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("icons/icons8-administrative-tools-50.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.combobox_board.SetSelection(0)
        self.radio_units.SetSelection(0)
        self.spin_bedwidth.SetMinSize((80, 23))
        self.spin_bedheight.SetMinSize((80, 23))
        self.checkbox_autolock.SetValue(1)
        self.checkbox_autobeep.SetValue(1)
        self.checkbox_rotary.Enable(False)
        self.spin_scalex.SetMinSize((80, 23))
        self.spin_scalex.Enable(False)
        self.spin_scalex.SetIncrement(0.01)
        self.spin_scaley.SetMinSize((80, 23))
        self.spin_scaley.Enable(False)
        self.spin_scaley.SetIncrement(0.01)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Preferences.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Board Type")
        sizer_2.Add(label_1, 0, 0, 0)
        sizer_2.Add(self.combobox_board, 0, 0, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add(self.radio_units, 0, 0, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Bedwidth")
        sizer_7.Add(label_2, 0, 0, 0)
        sizer_7.Add(self.spin_bedwidth, 0, 0, 0)
        sizer_5.Add(sizer_7, 1, wx.EXPAND, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Bedheight")
        sizer_4.Add(label_3, 0, 0, 0)
        sizer_4.Add(self.spin_bedheight, 0, 0, 0)
        sizer_5.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_1.Add(self.checkbox_autolock, 0, 0, 0)
        sizer_1.Add(self.checkbox_autohome, 0, 0, 0)
        sizer_1.Add(self.checkbox_autobeep, 0, 0, 0)
        static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        sizer_1.Add(static_line_1, 0, wx.EXPAND, 0)
        sizer_1.Add(self.checkbox_rotary, 0, 0, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, "Scale X")
        sizer_8.Add(label_4, 0, 0, 0)
        sizer_8.Add(self.spin_scalex, 0, 0, 0)
        sizer_6.Add(sizer_8, 1, wx.EXPAND, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, "Scale Y")
        sizer_9.Add(label_5, 0, 0, 0)
        sizer_9.Add(self.spin_scaley, 0, 0, 0)
        sizer_6.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_6, 1, wx.EXPAND, 0)
        static_line_2 = wx.StaticLine(self, wx.ID_ANY)
        sizer_1.Add(static_line_2, 0, wx.EXPAND, 0)
        sizer_1.Add(self.checkbox_mock_usb, 0, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_combobox_boardtype(self, event):  # wxGlade: Preferences.<event_handler>
        self.project.board = self.combobox_board.GetValue()

    def on_radio_units(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_radio_units' not implemented!")
        event.Skip()

    def spin_on_bedwidth(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_bedwidth' not implemented!")
        event.Skip()

    def spin_on_bedheight(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_bedheight' not implemented!")
        event.Skip()

    def on_check_autolock(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_autolock' not implemented!")
        event.Skip()

    def on_check_autohome(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_autohome' not implemented!")
        event.Skip()

    def on_check_autobeep(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_check_autobeep' not implemented!")
        event.Skip()

    def spin_on_scalex(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_scalex' not implemented!")
        event.Skip()

    def spin_on_scaley(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'spin_on_scaley' not implemented!")
        event.Skip()

    def on_checkbox_mock_usb(self, event):  # wxGlade: Preferences.<event_handler>
        print("Event handler 'on_checkbox_mock_usb' not implemented!")
        event.Skip()


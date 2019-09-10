# -*- coding: ISO-8859-1 -*-
#
# generated by wxGlade 0.9.3 on Fri Jun 28 16:25:14 2019
#

import wx


class Controller(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Controller.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((717, 250))
        self.controller_statusbar = self.CreateStatusBar(1)
        self.packet_list = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.TE_CHARWRAP | wx.TE_MULTILINE)
        self.text_byte_0 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_byte_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_desc = wx.TextCtrl(self, wx.ID_ANY, "\n")
        self.text_byte_2 = wx.TextCtrl(self, wx.ID_ANY, "\n")
        self.text_byte_3 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_byte_4 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_byte_5 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.last_packet_text = wx.TextCtrl(self, wx.ID_ANY, "")
        self.packet_text_text = wx.TextCtrl(self, wx.ID_ANY, "")
        self.packet_count_text = wx.TextCtrl(self, wx.ID_ANY, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        self.Bind(wx.EVT_CLOSE, self.on_close, self)
        self.project = None

    def set_project(self, project):
        self.project = project
        self.project.controller.status_listener = self.update_status
        self.project.controller.packet_listener = self.update_packet

    def on_close(self, event):
        self.project.controller.status_listener = None
        self.project.controller.packet_listener = None
        self.project = None
        event.Skip()  # delegate destroy to super

    def __set_properties(self):
        # begin wxGlade: Controller.__set_properties
        self.SetTitle("Controller")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("icons/icons8-usb-connector-50.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.controller_statusbar.SetStatusWidths([-1])

        # statusbar fields
        controller_statusbar_fields = ["Status"]
        for i in range(len(controller_statusbar_fields)):
            self.controller_statusbar.SetStatusText(controller_statusbar_fields[i], i)
        self.packet_list.SetMinSize((250, -1))
        self.text_byte_0.SetMinSize((77, 23))
        self.text_byte_1.SetMinSize((77, 23))
        self.text_desc.SetMinSize((75, 23))
        self.text_byte_2.SetMinSize((77, 23))
        self.text_byte_3.SetMinSize((77, 23))
        self.text_byte_4.SetMinSize((77, 23))
        self.text_byte_5.SetMinSize((77, 23))
        self.packet_count_text.SetMinSize((77, 23))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Controller.__do_layout
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        byte_data_sizer = wx.BoxSizer(wx.HORIZONTAL)
        byte5sizer = wx.BoxSizer(wx.VERTICAL)
        byte4sizer = wx.BoxSizer(wx.VERTICAL)
        byte3sizer = wx.BoxSizer(wx.VERTICAL)
        byte2sizer = wx.BoxSizer(wx.VERTICAL)
        byte1sizer = wx.BoxSizer(wx.VERTICAL)
        byte0sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_8.Add(self.packet_list, 1, wx.EXPAND, 0)
        byte0sizer.Add(self.text_byte_0, 0, 0, 0)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Byte 0")
        byte0sizer.Add(label_1, 0, 0, 0)
        byte_data_sizer.Add(byte0sizer, 1, wx.EXPAND, 0)
        byte1sizer.Add(self.text_byte_1, 0, 0, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Byte 1")
        byte1sizer.Add(label_2, 0, 0, 0)
        byte1sizer.Add(self.text_desc, 0, 0, 0)
        byte_data_sizer.Add(byte1sizer, 1, wx.EXPAND, 0)
        byte2sizer.Add(self.text_byte_2, 0, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Byte 2")
        byte2sizer.Add(label_3, 0, 0, 0)
        byte_data_sizer.Add(byte2sizer, 1, wx.EXPAND, 0)
        byte3sizer.Add(self.text_byte_3, 0, 0, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, "Byte 3")
        byte3sizer.Add(label_4, 0, 0, 0)
        byte_data_sizer.Add(byte3sizer, 1, wx.EXPAND, 0)
        byte4sizer.Add(self.text_byte_4, 0, 0, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, "Byte 4")
        byte4sizer.Add(label_5, 0, 0, 0)
        byte_data_sizer.Add(byte4sizer, 1, wx.EXPAND, 0)
        byte5sizer.Add(self.text_byte_5, 0, 0, 0)
        label_6 = wx.StaticText(self, wx.ID_ANY, "Byte 5")
        byte5sizer.Add(label_6, 0, 0, 0)
        byte_data_sizer.Add(byte5sizer, 1, wx.EXPAND, 0)
        sizer_9.Add(byte_data_sizer, 0, 0, 0)
        static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        sizer_9.Add(static_line_1, 0, wx.EXPAND, 0)
        label_9 = wx.StaticText(self, wx.ID_ANY, "Last Packet  ")
        sizer_13.Add(label_9, 1, 0, 0)
        sizer_13.Add(self.last_packet_text, 11, 0, 0)
        sizer_9.Add(sizer_13, 5, 0, 0)
        label_10 = wx.StaticText(self, wx.ID_ANY, "Packet Text  ")
        sizer_14.Add(label_10, 1, 0, 0)
        sizer_14.Add(self.packet_text_text, 11, 0, 0)
        sizer_9.Add(sizer_14, 5, 0, 0)
        label_11 = wx.StaticText(self, wx.ID_ANY, "Packet Count  \n")
        sizer_16.Add(label_11, 0, 0, 0)
        sizer_16.Add(self.packet_count_text, 0, 0, 0)
        sizer_9.Add(sizer_16, 5, 0, 0)
        sizer_8.Add(sizer_9, 4, wx.EXPAND, 0)
        self.SetSizer(sizer_8)
        self.Layout()
        # end wxGlade

    def update_status(self, data):
        try:
            if isinstance(data, int):
                self.text_desc.SetValue(str(data))
            elif len(data) == 6:
                self.text_byte_0.SetValue(str(data[0]))
                self.text_byte_1.SetValue(str(data[1]))
                self.text_byte_2.SetValue(str(data[2]))
                self.text_byte_3.SetValue(str(data[3]))
                self.text_byte_4.SetValue(str(data[4]))
                self.text_byte_5.SetValue(str(data[5]))
            else:
                self.text_desc.SetValue(str(data))
            self.Update()
        except RuntimeError:
            pass

    def update_packet(self, data, string_data):
        try:
            self.last_packet_text.SetValue(str(data))
            self.packet_text_text.SetValue(str(string_data))
            self.packet_count_text.SetValue(str(self.project.controller.packet_count))
            self.packet_list.AppendText('\n' + str(string_data))

            self.Update()
        except RuntimeError:
            pass

# end of class Controller

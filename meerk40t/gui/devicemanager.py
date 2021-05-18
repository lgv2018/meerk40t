#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Sat Feb  1 06:42:01 2020
#

import wx

from .icons import icons8_manager_50, icons8_plus_50, icons8_trash_50
from .mwindow import MWindow

_ = wx.GetTranslation


class DeviceManager(MWindow):
    def __init__(self, *args, **kwds):
        super().__init__(653, 332, *args, **kwds)
        self.devices_list = wx.ListCtrl(
            self, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES
        )
        self.new_device_button = wx.BitmapButton(
            self, wx.ID_ANY, icons8_plus_50.GetBitmap()
        )
        self.remove_device_button = wx.BitmapButton(
            self, wx.ID_ANY, icons8_trash_50.GetBitmap()
        )

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LIST_BEGIN_DRAG, self.on_list_drag, self.devices_list)
        self.Bind(
            wx.EVT_LIST_ITEM_ACTIVATED, self.on_list_item_activated, self.devices_list
        )
        self.Bind(
            wx.EVT_LIST_ITEM_RIGHT_CLICK, self.on_list_right_click, self.devices_list
        )
        self.Bind(
            wx.EVT_LIST_ITEM_SELECTED, self.on_list_item_selected, self.devices_list
        )
        self.Bind(
            wx.EVT_LIST_ITEM_DESELECTED, self.on_list_item_selected, self.devices_list
        )
        self.Bind(wx.EVT_BUTTON, self.on_button_new, self.new_device_button)
        self.Bind(wx.EVT_BUTTON, self.on_button_remove, self.remove_device_button)
        # end wxGlade

    def __set_properties(self):
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(icons8_manager_50.GetBitmap())
        self.SetIcon(_icon)
        self.SetTitle("Device Manager")
        self.devices_list.SetFont(
            wx.Font(
                13,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                0,
                "Segoe UI",
            )
        )
        self.devices_list.AppendColumn("Index", format=wx.LIST_FORMAT_LEFT, width=56)
        self.devices_list.AppendColumn("Spooler", format=wx.LIST_FORMAT_LEFT, width=74)
        self.devices_list.AppendColumn(
            "Driver/Input", format=wx.LIST_FORMAT_LEFT, width=170
        )
        self.devices_list.AppendColumn("Output", format=wx.LIST_FORMAT_LEFT, width=170)
        self.devices_list.AppendColumn(
            "Registered", format=wx.LIST_FORMAT_LEFT, width=93
        )
        self.new_device_button.SetToolTip("Add a new device")
        self.new_device_button.SetSize(self.new_device_button.GetBestSize())
        self.remove_device_button.SetToolTip("Remove selected device")
        self.remove_device_button.SetSize(self.remove_device_button.GetBestSize())
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: DeviceManager.__do_layout
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.devices_list, 0, wx.EXPAND, 0)
        button_sizer.Add(self.new_device_button, 0, 0, 0)
        button_sizer.Add(self.remove_device_button, 0, 0, 0)
        main_sizer.Add(button_sizer, 0, wx.EXPAND, 0)
        self.new_device_button.Enable(False)
        self.remove_device_button.Enable(False)
        self.SetSizer(main_sizer)
        self.Layout()
        # end wxGlade

    def window_open(self):
        self.refresh_device_list()

    def window_close(self):
        item = self.devices_list.GetFirstSelected()
        if item != -1:
            uid = self.devices_list.GetItem(item).Text
            self.context.device_primary = uid

    def refresh_device_list(self):
        self.devices_list.DeleteAllItems()
        for i, dev in enumerate(self.context.match("device")):
            device = self.context.registered[dev]
            spooler, input_driver, output = device
            device_context = self.context.get_context("devices")
            dev_string = "device_%d" % i
            if hasattr(device_context, dev_string):
                line = getattr(device_context, dev_string)
                registered = len(line) > 0
            else:
                registered = False
            m = self.devices_list.InsertItem(i, str(i))
            if self.context.active == str(m):
                self.devices_list.SetItemBackgroundColour(m, wx.LIGHT_GREY)

            if m != -1:
                spooler_name = spooler.name if spooler is not None else "None"
                self.devices_list.SetItem(m, 1, str(spooler_name))
                self.devices_list.SetItem(m, 2, str(input_driver))
                self.devices_list.SetItem(m, 3, str(output))
                self.devices_list.SetItem(m, 4, str(registered))

    def on_list_drag(self, event):  # wxGlade: DeviceManager.<event_handler>
        pass

    def on_list_right_click(self, event):  # wxGlade: DeviceManager.<event_handler>
        uid = event.GetLabel()
        print(uid)
        self.refresh_device_list()

    def on_list_item_selected(self, event=None):
        item = self.devices_list.GetFirstSelected()
        self.new_device_button.Enable(item != -1)
        self.remove_device_button.Enable(item != -1)

    def on_list_item_activated(
        self, event=None
    ):  # wxGlade: DeviceManager.<event_handler>
        item = self.devices_list.GetFirstSelected()
        if item == -1:
            return
        uid = self.devices_list.GetItem(item).Text
        self.context("device activate %s\n" % uid)
        self.context("timer 1 0.2 window close DeviceManager\n")

    def on_button_new(self, event):  # wxGlade: DeviceManager.<event_handler>
        item = self.devices_list.GetFirstSelected()
        if item == -1:
            return
        spooler_input = self.devices_list.GetItem(item).Text
        # END SPOOLER

        names = [name for name in self.context._kernel.match("driver", suffix=True)]
        dlg = wx.SingleChoiceDialog(
            None, _("What type of driver is being added?"), _("Device Type"), names
        )
        dlg.SetSelection(0)
        if dlg.ShowModal() == wx.ID_OK:
            device_type = names[dlg.GetSelection()]
        else:
            dlg.Destroy()
            return
        dlg.Destroy()
        # END Driver

        names = [name for name in self.context._kernel.match("output", suffix=True)]
        dlg = wx.SingleChoiceDialog(
            None, _("Where does the device output data?"), _("Output Type"), names
        )
        dlg.SetSelection(0)
        if dlg.ShowModal() == wx.ID_OK:
            output_type = names[dlg.GetSelection()]
        else:
            dlg.Destroy()
            return
        dlg.Destroy()
        # END OUTPUT

        if output_type == "file":
            dlg = wx.TextEntryDialog(
                None,
                _("What filename does this device output to?"),
                _("Output"),
            )
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetValue()
            else:
                dlg.Destroy()
                return
            self.context(
                "spool%s -r driver -n %s outfile %s\n"
                % (spooler_input, device_type, filename)
            )

            dlg.Destroy()
            self.refresh_device_list()
            return

        if output_type == "tcp":
            dlg = wx.TextEntryDialog(
                None,
                _("What network address does this device output to?"),
                _("Output"),
            )
            if dlg.ShowModal() == wx.ID_OK:
                address = dlg.GetValue()
            else:
                dlg.Destroy()
                return
            dlg.Destroy()

            port = None
            if ":" in address:
                port = address.split(':')[-1]
                try:
                    port = int(port)
                    address = address.split(':')[0]
                except ValueError:
                    port = None

            if port is None:
                dlg = wx.TextEntryDialog(
                    None,
                    _("What network port does this device output to?"),
                    _("Output"),
                )
                if dlg.ShowModal() == wx.ID_OK:
                    port = dlg.GetValue()
                else:
                    dlg.Destroy()
                    return
                dlg.Destroy()
            self.context(
                "spool%s -r driver -n %s tcp %s %s\n"
                % (spooler_input, device_type, address, str(port))
            )

            self.refresh_device_list()
            return

        self.context(
            "spool%s -r driver -n %s output -n %s\n"
            % (spooler_input, device_type, output_type)
        )
        self.refresh_device_list()
        self.context.get_context("devices").flush()

    def on_button_remove(self, event):  # wxGlade: DeviceManager.<event_handler>
        item = self.devices_list.GetFirstSelected()
        if item == -1:
            return
        uid = self.devices_list.GetItem(item).Text
        self.context("device delete %s\n" % uid)
        self.refresh_device_list()

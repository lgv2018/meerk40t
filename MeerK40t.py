# -*- coding: ISO-8859-1 -*-
#
# generated by wxGlade 0.9.3 on Thu Jun 27 21:45:40 2019
#
import sys
import traceback

import wx
import wx.ribbon as RB
from PIL import Image

import svg_parser
from LaserProject import LaserProject, ImageElement, PathElement, EgvElement, LaserThread
from LaserSceneView import LaserSceneView


# begin wxGlade: dependencies
# end wxGlade


class IdInc:
    def __init__(self):
        self.id_highest_value = wx.ID_HIGHEST

    def new(self):
        self.id_highest_value += 1
        return self.id_highest_value


idinc = IdInc()
ID_MAIN_TOOLBAR = idinc.new()
ID_ADD_FILE = idinc.new()
ID_OPEN = idinc.new()
ID_SAVE = idinc.new()
ID_SCRIPTS = idinc.new()
ID_NAV = idinc.new()
ID_USB = idinc.new()
ID_CONTROLLER = idinc.new()
ID_CUT_CONFIGURATION = idinc.new()
ID_PREFERENCES = idinc.new()
ID_SELECT = idinc.new()

ID_MENU_NEW = idinc.new()
ID_MENU_OPEN_PROJECT = idinc.new()
ID_MENU_RECENT_PROJECT = idinc.new()

ID_MENU_IMPORT = idinc.new()
ID_MENU_SAVE = idinc.new()
ID_MENU_SAVE_AS = idinc.new()
ID_MENU_EXIT = idinc.new()
ID_MENU_ZOOM_OUT = idinc.new()
ID_MENU_ZOOM_IN = idinc.new()
ID_MENU_ZOOM_SIZE = idinc.new()
ID_MENU_HIDE_GUIDES = idinc.new()
ID_MENU_HIDE_GRID = idinc.new()

ID_MENU_ROTATE_CW = idinc.new()
ID_MENU_ROTATE_CCW = idinc.new()

ID_MENU_HFLIP = idinc.new()
ID_MENU_VFLIP = idinc.new()

ID_MENU_PREFERENCES = idinc.new()
ID_MENU_NAVIGATION = idinc.new()
ID_MENU_CONTROLLER = idinc.new()
ID_MENU_TREE = idinc.new()

ID_MENU_WEBPAGE = idinc.new()
ID_CUT_TREE = idinc.new()
ID_CUT_BURN_BUTTON = idinc.new()

project = LaserProject()


class MeerK40t(wx.Frame):

    def __init__(self, *args, **kwds):
        # begin wxGlade: MeerK40t.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1200, 600))
        self.DragAcceptFiles(True)
        self.project = project
        self.scene = LaserSceneView(self, wx.ID_ANY)
        self.scene.set_project(self.project)
        self.tree = CutConfiguration(self, ID_CUT_CONFIGURATION)

        panel = wx.Panel(self)

        self._ribbon = RB.RibbonBar(panel, style=RB.RIBBON_BAR_DEFAULT_STYLE
                                                 | RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)

        self._bitmap_creation_dc = wx.MemoryDC()
        self._colour_data = wx.ColourData()

        home = RB.RibbonPage(self._ribbon, wx.ID_ANY, "Examples",
                             wx.Bitmap("icons/icons8-redo-50.png", wx.BITMAP_TYPE_ANY))
        toolbar_panel = RB.RibbonPanel(home, wx.ID_ANY, "Toolbar",
                                       style=RB.RIBBON_PANEL_NO_AUTO_MINIMISE | RB.RIBBON_PANEL_EXT_BUTTON)

        toolbar = RB.RibbonToolBar(toolbar_panel, ID_MAIN_TOOLBAR)
        self.toolbar = toolbar
        toolbar.AddTool(ID_OPEN, wx.Bitmap("icons/icons8-opened-folder-50.png", wx.BITMAP_TYPE_ANY))  # "Open",
        toolbar.AddTool(ID_SAVE, wx.Bitmap("icons/icons8-save-50.png", wx.BITMAP_TYPE_ANY))  # "Save",

        windows_panel = RB.RibbonPanel(home, wx.ID_ANY, "Windows",
                                       wx.Bitmap("icons/icons8-py-50.png", wx.BITMAP_TYPE_ANY))
        windows = RB.RibbonButtonBar(windows_panel)
        windows.AddButton(ID_NAV, "Navigation", wx.Bitmap("icons/icons8-move-32.png", wx.BITMAP_TYPE_ANY), "")
        windows.AddButton(ID_USB, "Usb", wx.Bitmap("icons/icons8-usb-connector-50.png", wx.BITMAP_TYPE_ANY), "")
        windows.AddButton(ID_CONTROLLER, "Controller", wx.Bitmap("icons/icons8-connected-50.png", wx.BITMAP_TYPE_ANY),
                          "")
        windows.AddButton(ID_PREFERENCES, "Preferences",
                          wx.Bitmap("icons/icons8-administrative-tools-50.png", wx.BITMAP_TYPE_ANY), "")

        label_font = wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT)

        self._bitmap_creation_dc.SetFont(label_font)
        self._ribbon.Realize()

        s = wx.BoxSizer(wx.VERTICAL)
        s.Add(self._ribbon, 0, wx.EXPAND)
        ss = wx.BoxSizer(wx.HORIZONTAL)
        ss.Add(self.tree, 1, wx.EXPAND)
        ss.Add(self.scene, 4, wx.EXPAND)
        s.Add(ss, 1, wx.EXPAND)

        panel.SetSizer(s)
        self.panel = panel

        self.CenterOnScreen()

        # Menu Bar
        self.main_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(ID_MENU_NEW, "New", "")
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(ID_MENU_OPEN_PROJECT, "Open Project", "")
        wxglade_tmp_menu.Append(ID_MENU_IMPORT, "Import File", "")
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(ID_MENU_SAVE, "Save", "")
        wxglade_tmp_menu.Append(ID_MENU_SAVE_AS, "Save As", "")
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(ID_MENU_EXIT, "Exit", "")
        self.main_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()

        wxglade_tmp_menu.Append(ID_MENU_ZOOM_OUT, "Zoom Out", "")
        wxglade_tmp_menu.Append(ID_MENU_ZOOM_IN, "Zoom In", "")
        wxglade_tmp_menu.Append(ID_MENU_ZOOM_SIZE, "Zoom To Size", "")
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(ID_MENU_HIDE_GRID, "Hide Grid", "", wx.ITEM_CHECK)
        wxglade_tmp_menu.Append(ID_MENU_HIDE_GUIDES, "Hide Guides", "", wx.ITEM_CHECK)
        self.main_menubar.Append(wxglade_tmp_menu, "View")
        wxglade_tmp_menu = wx.Menu()

        wxglade_tmp_menu_sub = wx.Menu()
        wxglade_tmp_menu_sub.Append(ID_MENU_ROTATE_CW, u"Rotate \u03c4/4", "")
        wxglade_tmp_menu_sub.Append(ID_MENU_ROTATE_CCW, u"Rotate -\u03c4/4", "")
        wxglade_tmp_menu_sub.Append(ID_MENU_HFLIP, "H-Flip", "")
        wxglade_tmp_menu_sub.Append(ID_MENU_VFLIP, "V-Flip", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "Transform", wxglade_tmp_menu_sub, "")

        self.main_menubar.Append(wxglade_tmp_menu, "Design")

        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(ID_MENU_PREFERENCES, "Preferences", "")
        wxglade_tmp_menu.Append(ID_MENU_NAVIGATION, "Navigation", "")
        wxglade_tmp_menu.Append(ID_MENU_CONTROLLER, "Controller", "")

        self.main_menubar.Append(wxglade_tmp_menu, "Windows")

        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(ID_MENU_WEBPAGE, "Webpage", "")
        self.main_menubar.Append(wxglade_tmp_menu, "Help")

        self.SetMenuBar(self.main_menubar)
        # Menu Bar end

        self.Bind(wx.EVT_MENU, self.on_click_new, id=ID_MENU_NEW)
        self.Bind(wx.EVT_MENU, self.on_click_open, id=ID_MENU_OPEN_PROJECT)
        self.Bind(wx.EVT_MENU, self.on_click_import, id=ID_MENU_IMPORT)
        self.Bind(wx.EVT_MENU, self.on_click_save, id=ID_MENU_SAVE)
        self.Bind(wx.EVT_MENU, self.on_click_save_as, id=ID_MENU_SAVE_AS)
        self.Bind(wx.EVT_MENU, self.on_click_exit, id=ID_MENU_EXIT)
        self.Bind(wx.EVT_MENU, self.on_click_zoom_out, id=ID_MENU_ZOOM_OUT)
        self.Bind(wx.EVT_MENU, self.on_click_zoom_in, id=ID_MENU_ZOOM_IN)
        self.Bind(wx.EVT_MENU, self.on_click_zoom_size, id=ID_MENU_ZOOM_SIZE)
        self.Bind(wx.EVT_MENU, self.toggle_show_grid, id=ID_MENU_HIDE_GRID)
        self.Bind(wx.EVT_MENU, self.toggle_hide_guides, id=ID_MENU_HIDE_GUIDES)
        self.Bind(wx.EVT_MENU, self.transform_rotate_right, id=ID_MENU_ROTATE_CW)
        self.Bind(wx.EVT_MENU, self.transform_rotate_left, id=ID_MENU_ROTATE_CCW)
        self.Bind(wx.EVT_MENU, self.transform_mirror_hflip, id=ID_MENU_HFLIP)
        self.Bind(wx.EVT_MENU, self.transform_mirror_vflip, id=ID_MENU_VFLIP)

        self.Bind(wx.EVT_MENU, self.open_preferences, id=ID_MENU_PREFERENCES)
        self.Bind(wx.EVT_MENU, self.open_navigation, id=ID_MENU_NAVIGATION)
        self.Bind(wx.EVT_MENU, self.open_controller, id=ID_MENU_CONTROLLER)

        self.Bind(wx.EVT_MENU, self.launch_webpage, id=ID_MENU_WEBPAGE)

        toolbar.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.on_click_open, id=ID_OPEN)
        toolbar.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.on_click_save, id=ID_SAVE)

        windows.Bind(RB.EVT_RIBBONBUTTONBAR_CLICKED, self.open_usb, id=ID_USB)
        windows.Bind(RB.EVT_RIBBONBUTTONBAR_CLICKED, self.open_navigation, id=ID_NAV)
        windows.Bind(RB.EVT_RIBBONBUTTONBAR_CLICKED, self.open_controller, id=ID_CONTROLLER)
        windows.Bind(RB.EVT_RIBBONBUTTONBAR_CLICKED, self.open_preferences, id=ID_PREFERENCES)

        self.main_statusbar = self.CreateStatusBar(1)

        self.__set_properties()
        self.__do_layout()

        # end wxGlade

        self.Bind(wx.EVT_DROP_FILES, self.on_drop_file)

        self.Bind(wx.EVT_SIZE, self.on_size_set)

        self.previous_position = None
        self.project.elements_change_listener = self.tree_update

    def on_size_set(self, event):
        self.panel.Size = self.ClientSize
        self.panel.Update()

    def __set_properties(self):
        # begin wxGlade: MeerK40t.__set_properties
        self.SetTitle("MeerK40t")
        self.main_statusbar.SetStatusWidths([-1])

        # statusbar fields
        main_statusbar_fields = ["Status"]
        for i in range(len(main_statusbar_fields)):
            self.main_statusbar.SetStatusText(main_statusbar_fields[i], i)
        # self.main_toolbar.Realize()
        self.scene.SetMinSize((1000, 880))
        self.scene.SetBackgroundColour(wx.Colour(112, 219, 147))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MeerK40t.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel)
        self.SetSizer(sizer)
        self.Layout()
        # end wxGlade

    def on_drop_file(self, event):
        for pathname in event.GetFiles():
            if pathname.lower().endswith(".svg"):
                self.load_svg(pathname)
            elif pathname.lower().endswith(".egv"):
                self.load_egv(pathname)
            else:
                self.load_image(pathname)
        self.tree.refresh_tree_elements()

    def load_svg(self, pathname):
        svg = svg_parser.parse_svg_file(pathname)
        context = self.project
        for element in svg:
            if 'd' in element:
                pathd = element['d']
                context.append(PathElement(pathd))
            else:
                group = []
                context.append(group)
                context = group
        self.scene.update_buffer()

    def tree_update(self):
        self.tree.refresh_tree_elements()

    def load_egv(self, pathname):
        self.project.append(EgvElement(pathname))
        self.scene.update_buffer()

    def load_image(self, pathname):
        image = Image.open(pathname)
        self.project.append(ImageElement(image))
        width, height = image.size
        self.project.append(PathElement("M0,0 {0},0 {0},{1} 0,{1}z".format(width, height)))
        self.scene.update_buffer()

    def on_click_new(self, event):  # wxGlade: MeerK40t.<event_handler>
        self.project.elements = []
        self.scene.update_buffer()
        self.Refresh()

    def on_click_open(self, event):  # wxGlade: MeerK40t.<event_handler>
        # This code should load just specific project files rather than all importable formats.
        files = "All valid types|*.svg;*.egv;*.png;*.jpg;*.jpeg|" \
                "Scalable Vector Graphics svg (*.svg)|*.svg|" \
                "Engrave egv (*.egv)|*.egv|" \
                "Portable Network Graphics png (*.png)|*.png"
        with wx.FileDialog(self, "Open", wildcard=files,
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind
            pathname = fileDialog.GetPath()
            if pathname.lower().endswith(".svg"):
                self.load_svg(pathname)
            elif pathname.lower().endswith(".egv"):
                self.load_egv(pathname)
            else:
                self.load_image(pathname)

    def on_click_import(self, event):  # wxGlade: MeerK40t.<event_handler>
        files = "All valid types|*.svg;*.egv;*.png;*.jpg;*.jpeg|" \
                "Scalable Vector Graphics svg (*.svg)|*.svg|" \
                "Engrave egv (*.egv)|*.egv|" \
                "Portable Network Graphics png (*.png)|*.png"
        with wx.FileDialog(self, "Open", wildcard=files,
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind
            pathname = fileDialog.GetPath()
            if pathname.lower().endswith(".svg"):
                self.load_svg(pathname)
            elif pathname.lower().endswith(".egv"):
                self.load_egv(pathname)
            else:
                self.load_image(pathname)

    def on_click_save(self, event):  # wxGlade: MeerK40t.<event_handler>
        print("Event handler 'on_click_save' not implemented!")
        event.Skip()

    def on_click_save_as(self, event):  # wxGlade: MeerK40t.<event_handler>
        print("Event handler 'on_click_save_as' not implemented!")
        event.Skip()

    def on_click_exit(self, event):  # wxGlade: MeerK40t.<event_handler>
        self.Close()

    def on_click_zoom_out(self, event):  # wxGlade: MeerK40t.<event_handler>
        m = self.scene.ClientSize / 2
        self.scene.scene_post_scale(1.0 / 1.5, 1.0 / 1.5, m[0], m[1])

    def on_click_zoom_in(self, event):  # wxGlade: MeerK40t.<event_handler>
        m = self.scene.ClientSize / 2
        self.scene.scene_post_scale(1.5, 1.5, m[0], m[1])

    def on_click_zoom_size(self, event):  # wxGlade: MeerK40t.<event_handler>
        self.scene.focus_on_project()

    def toggle_show_grid(self, event):  # wxGlade: MeerK40t.<event_handler>
        self.scene.draw_grid = not self.scene.draw_grid

    def toggle_hide_guides(self, event):  # wxGlade: MeerK40t.<event_handler>
        self.scene.draw_guides = not self.scene.draw_guides

    def transform_rotate_right(self, event):  # wxGlade: MeerK40t.<event_handler>
        from math import pi
        tau = pi * 2
        self.project.menu_rotate(0.25 * tau)

    def transform_rotate_left(self, event):  # wxGlade: MeerK40t.<event_handler>
        from math import pi
        tau = pi * 2
        self.project.menu_rotate(0.25 * tau)

    def transform_mirror_hflip(self, event):  # wxGlade: MeerK40t.<event_handler>
        self.project.menu_scale(-1, 1)

    def transform_mirror_vflip(self, event):  # wxGlade: MeerK40t.<event_handler>
        self.project.menu_scale(1, -1)

    def on_click_group(self, event):  # wxGlade: MeerK40t.<event_handler>
        print("Event handler 'on_click_group' not implemented!")
        event.Skip()

    def on_click_ungroup(self, event):  # wxGlade: MeerK40t.<event_handler>
        print("Event handler 'on_click_ungroup' not implemented!")
        event.Skip()

    def open_preferences(self, event):  # wxGlade: MeerK40t.<event_handler>
        from Preferences import Preferences
        window = Preferences(None, wx.ID_ANY, "")
        window.set_project(project)
        window.Show()

    def open_usb(self, event):  # wxGlade: MeerK40t.<event_handler>
        from UsbConnect import UsbConnect
        window = UsbConnect(None, wx.ID_ANY, "")
        window.set_project(project)
        window.Show()

    def open_navigation(self, event):  # wxGlade: MeerK40t.<event_handler>
        from Navigation import Navigation
        window = Navigation(None, wx.ID_ANY, "")
        window.set_project(project)
        window.Show()

    def open_controller(self, event):  # wxGlade: MeerK40t.<event_handler>
        from Controller import Controller
        window = Controller(None, wx.ID_ANY, "")
        window.set_project(project)
        window.Show()

    def launch_webpage(self, event):  # wxGlade: MeerK40t.<event_handler>
        import webbrowser
        webbrowser.open("https://github.com/meerk40t/meerk40t", new=0, autoraise=True)


# end of class MeerK40t


class CutConfiguration(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: CutConfiguration.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.SetSize((300, -1))
        self.element_tree = wx.TreeCtrl(self, ID_CUT_TREE, style=wx.FULL_REPAINT_ON_RESIZE)
        self.burn_button = wx.BitmapButton(self, ID_CUT_BURN_BUTTON, wx.Bitmap("./icons/icons8-gas-industry-50.png",
                                                                               wx.BITMAP_TYPE_ANY))
        self.item_lookup = {}
        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_item_changed, self.element_tree)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.on_item_activated, self.element_tree)
        self.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.on_item_right_click, self.element_tree)
        self.Bind(wx.EVT_BUTTON, self.on_clicked_burn, id=ID_CUT_BURN_BUTTON)
        self.refresh_tree_elements()

        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: CutConfiguration.__set_properties
        self.SetSize((300, -1))
        self.burn_button.SetSize(self.burn_button.GetBestSize())
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: CutConfiguration.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.element_tree, 1, wx.EXPAND, 0)
        sizer_1.Add(self.burn_button, 0, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_clicked_burn(self, event):
        if project.thread is None:
            project.thread = LaserThread(project)
            project.thread.start()

            from JobInfo import JobInfo
            window = JobInfo(None, wx.ID_ANY, "")
            window.set_project(project)
            window.Show()

    def on_item_right_click(self, event):
        menu = wx.Menu()
        convert = menu.Append(wx.ID_ANY, "Delete", "", wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.on_tree_popup_delete, convert)
        self.PopupMenu(menu)
        menu.Destroy()

    def on_tree_popup_delete(self, event):
        print(event)
        for e in project.selected:
            project.remove_element(e)
        project.set_selected([])

    def on_item_activated(self, event):  # wxGlade: CutConfiguration.<event_handler>
        item = event.GetItem()
        if item in self.item_lookup:
            element = self.item_lookup[item]
            from ElementProperty import ElementProperty
            window = ElementProperty(None, wx.ID_ANY, "")
            window.set_element(element)
            window.Show()

    def on_item_changed(self, event):
        item = event.GetItem()
        if item in self.item_lookup:
            element = self.item_lookup[item]
            project.set_selected(element)

    def add_element(self, tree, node, element):
        if isinstance(element, list):
            subnode = tree.AppendItem(node, str("Group"))
            self.item_lookup[subnode] = element
            for subitem in element:
                self.add_element(tree, subnode, subitem)
        else:
            item = tree.AppendItem(node, str(element))
            self.item_lookup[item] = element

    def refresh_tree_elements(self):
        tree = self.element_tree
        tree.DeleteAllItems()
        self.item_lookup = {}
        root = self.element_tree.AddRoot("Job Parts")

        for element in project.elements:
            self.add_element(tree, root, element)
        tree.CollapseAll()
        tree.ExpandAll()


class MeerK40tGui(wx.App):
    def OnInit(self):
        self.MeerK40t = MeerK40t(None, wx.ID_ANY, "")
        self.SetTopWindow(self.MeerK40t)
        self.MeerK40t.Show()
        return True


# end of class MeerK40tGui
def handleGUIException(exc_type, exc_value, exc_traceback):
    err_msg = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    dlg = wx.MessageDialog(None, err_msg, 'Error encountered', wx.OK | wx.ICON_ERROR)
    dlg.ShowModal()
    dlg.Destroy()
    print(err_msg)


sys.excepthook = handleGUIException

if __name__ == "__main__":
    MeerK40tApp = MeerK40tGui(0)
    MeerK40tApp.MainLoop()

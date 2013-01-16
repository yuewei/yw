#-----------------------------------------------------------------------------
# Name:        test.py
# Purpose:     
#
# Author:      <your name>
#
# Created:     2013/01/01
# RCS-ID:      $Id: test.py $
# Copyright:   (c) 2006
# Licence:     <your licence>
#-----------------------------------------------------------------------------
#Boa:Frame:Frame1

import wx
import wx.richtext

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON3, wxID_FRAME1PANEL1, 
 wxID_FRAME1RICHTEXTCTRL1, wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT10, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, 
 wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3, 
 wxID_FRAME1TEXTCTRL4, wxID_FRAME1TEXTCTRL5, wxID_FRAME1TEXTCTRL6, 
 wxID_FRAME1TEXTCTRL7, wxID_FRAME1TEXTCTRL8, 
] = [wx.NewId() for _init_ctrls in range(24)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(451, 159), size=wx.Size(583, 491),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Frame1')
        self.SetClientSize(wx.Size(567, 453))
        self.SetMaxSize(wx.Size(583, 491))
        self.SetMinSize(wx.Size(583, 491))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(567, 453),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Georgia'))

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'ID\u67e5\u8be2',
              name='button1', parent=self.panel1, pos=wx.Point(376, 208),
              size=wx.Size(75, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3,
              label=u'ISBN\u67e5\u8be2', name='button3', parent=self.panel1,
              pos=wx.Point(376, 248), size=wx.Size(75, 24), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(192, 207), size=wx.Size(152, 25),
              style=0, value=u'')

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL1,
              parent=self.panel1, pos=wx.Point(16, 316), size=wx.Size(544, 132),
              style=wx.richtext.RE_MULTILINE, value=u' ')
        self.richTextCtrl1.SetLabel(u'richText')

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u' \u56fe\u4e66\u7b80\u4ecb', name='staticText1',
              parent=self.panel1, pos=wx.Point(16, 280), size=wx.Size(52, 14),
              style=0)
        self.staticText1.SetForegroundColour(wx.Colour(128, 64, 64))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'ID\u53f7', name='staticText2', parent=self.panel1,
              pos=wx.Point(136, 208), size=wx.Size(32, 19), style=0)
        self.staticText2.SetFont(wx.Font(12, wx.SWISS, wx.ITALIC, wx.BOLD,
              False, u'Calibri'))
        self.staticText2.SetForegroundColour(wx.Colour(64, 0, 128))

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'ISBN', name='staticText3', parent=self.panel1,
              pos=wx.Point(128, 248), size=wx.Size(37, 18), style=0)
        self.staticText3.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Georgia'))
        self.staticText3.SetForegroundColour(wx.Colour(64, 0, 128))

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(192, 248), size=wx.Size(152, 23),
              style=0, value=u'')

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_FRAME1STATICBITMAP1, name='staticBitmap1',
              parent=self.panel1, pos=wx.Point(32, 40), size=wx.Size(112, 152),
              style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'\u4f5c\u8005\uff1a', name='staticText4',
              parent=self.panel1, pos=wx.Point(264, 16), size=wx.Size(51, 18),
              style=0)
        self.staticText4.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Georgia'))

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'\u4e66\u540d\uff1a', name='staticText5',
              parent=self.panel1, pos=wx.Point(264, 48), size=wx.Size(51, 18),
              style=0)
        self.staticText5.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Georgia'))

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'\u56fe\u4e66\u5c01\u9762\uff1a', name='staticText6',
              parent=self.panel1, pos=wx.Point(24, 16), size=wx.Size(65, 15),
              style=0)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'\u51fa\u7248\u793e\uff1a', name='staticText7',
              parent=self.panel1, pos=wx.Point(264, 80), size=wx.Size(68, 18),
              style=0)
        self.staticText7.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Georgia'))

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'\u4ef7\u683c\uff1a', name='staticText8',
              parent=self.panel1, pos=wx.Point(264, 112), size=wx.Size(51, 18),
              style=0)
        self.staticText8.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Georgia'))

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'\u51fa\u7248\u65e5\u671f\uff1a', name='staticText9',
              parent=self.panel1, pos=wx.Point(264, 144), size=wx.Size(85, 18),
              style=0)
        self.staticText9.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Georgia'))

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'\u9875\u6570\uff1a', name='staticText10',
              parent=self.panel1, pos=wx.Point(264, 176), size=wx.Size(51, 18),
              style=0)
        self.staticText10.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Georgia'))

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self.panel1, pos=wx.Point(336, 16), size=wx.Size(216, 23),
              style=0, value=u'')

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self.panel1, pos=wx.Point(336, 48), size=wx.Size(216, 23),
              style=0, value=u'')

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL5, name='textCtrl5',
              parent=self.panel1, pos=wx.Point(336, 80), size=wx.Size(216, 23),
              style=0, value=u'')

        self.textCtrl6 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL6, name='textCtrl6',
              parent=self.panel1, pos=wx.Point(336, 112), size=wx.Size(216, 23),
              style=0, value=u'')

        self.textCtrl7 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL7, name='textCtrl7',
              parent=self.panel1, pos=wx.Point(336, 176), size=wx.Size(216, 23),
              style=0, value=u'')

        self.textCtrl8 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL8, name='textCtrl8',
              parent=self.panel1, pos=wx.Point(336, 144), size=wx.Size(216, 23),
              style=0, value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton3Button(self, event):
        isbn = self.textCtrl2.GetValue()
        import urllib2,json
        url="https://api.douban.com/v2/book/isbn/"+isbn
        response=urllib2.urlopen(url)
        page=response.read()
        array=json.loads(page)
        author=array['author'][0]
        self.textCtrl1.SetValue(array["id"])
        id=array["id"]
        if(author!=""):
            self.textCtrl3.SetValue(author)
        else:
            self.textCtrl3.SetValue("")
        self.textCtrl4.SetValue(array["title"])
        publisher=array["publisher"]
        if(publisher!=""):
            self.textCtrl5.SetValue(publisher)
        else:
            self.textCtrl5.SetValue("")
        self.textCtrl6.SetValue(array["price"])
        pubdate=array["pubdate"]
        if(pubdate!=""):
            self.textCtrl8.SetValue(array["pubdate"])
        else:
            self.textCtrl8.SetValue("")
        pages=array["pages"]
        if(pages!=""):
            self.textCtrl7.SetValue(pages)
        else:
            self.textCtrl7.SetValue("")
        summary=array["summary"]
        if(summary!=""):
            self.richTextCtrl1.SetValue(array["summary"])
        else:
            self.richTextCtrl1.SetValue("")
        try:
            self.textCtrl2.SetValue(array["isbn10"])
        except:
            self.textCtrl2.SetValue(array["isbn13"])
            image=array["image"]
        if(image!=""):
            url = image  
            path = "D:/douban/"+id+".jpg"  
            data = urllib2.urlopen(url).read()  
            f = file(path,"wb")  
            f.write(data)  
            f.close()
            jpg = wx.Image(path, wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
            self.staticBitmap1.SetBitmap(jpg)
        event.Skip()

    def OnButton1Button(self, event):
        id=self.textCtrl1.GetValue()
        import urllib2,json
        url="https://api.douban.com/v2/book/"+id
        response=urllib2.urlopen(url)
        page=response.read()
        array=json.loads(page)
        author=array['author'][0]
        if(author!=""):
            self.textCtrl3.SetValue(author)
        else:
            self.textCtrl3.SetValue("")
        self.textCtrl4.SetValue(array["title"])
        publisher=array["publisher"]
        if(publisher!=""):
            self.textCtrl5.SetValue(publisher)
        else:
            self.textCtrl5.SetValue("")
        self.textCtrl6.SetValue(array["price"])
        pubdate=array["pubdate"]
        if(pubdate!=""):
            self.textCtrl8.SetValue(array["pubdate"])
        else:
            self.textCtrl8.SetValue("")
        pages=array["pages"]
        if(pages!=""):
            self.textCtrl7.SetValue(pages)
        else:
            self.textCtrl7.SetValue("")
        summary=array["summary"]
        if(summary!=""):
            self.richTextCtrl1.SetValue(array["summary"])
        else:
            self.richTextCtrl1.SetValue("")
        try:
            self.textCtrl2.SetValue(array["isbn10"])
        except:
            self.textCtrl2.SetValue(array["isbn13"])
        image=array["image"]
        if(image!=""):
            url = image  
            path = "D:/douban/"+id+".jpg"  
            data = urllib2.urlopen(url).read()  
            f = file(path,"wb")  
            f.write(data)  
            f.close()
            jpg = wx.Image(path, wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
            self.staticBitmap1.SetBitmap(jpg)
        event.Skip()

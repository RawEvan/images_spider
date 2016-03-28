# -*- coding: utf-8 -*-
from django import forms

class siteForm(forms.Form):
    site = forms.CharField(label = '网址 ', initial = 'http://www.tuchong.com')

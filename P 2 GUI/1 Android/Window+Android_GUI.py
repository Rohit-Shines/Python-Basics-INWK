# Pip install buildozer to convert code into android apk

from kivymd.app import MDApp
from kivy.lang import Builder   #builder used to build the kivy application

class Test(MDApp):

    def build(self):
        self.title = 'Programming mowa'
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'
    MDToolbar:
        title: 'Dalhousei University'
        md_bg_color: app.theme_cls.primary_color
        specific_text_color: 1, 1, 9, 9

    MDBottomNavigation:
                
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Rohit'
            icon: 'rohit.png'

            Image:
                id: imageView
                source: 'rohit.png'
        
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Pavan V'
            icon: 'pava.png'

            Image:
                id: imageView
                source: 'pava.png'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Nagasai P'
            icon: 'nag.png'

            Image:
                id: imageView
                source: 'nag.png'
                
        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Kasi '
            icon: 'bottle-tonic-skull'

            Image:
                id: imageView
                source: 'tam2.gif'
'''
        )

Test().run()
# Display an image

from kivy.app import App
from kivy.uix.image import Image


class MainApp(App):
    def build(self):
        img = Image(
            source='/root/_ARCHIVED_HONEYsave/_workfinish/KISHORE-mtechPD_28May2019_ALLData/DATA_KISHORE_MTECH-2018'
                   '-19_submitted/_Figures/_pwelchPlots/mabfAB/mabfA/Ach9/ mabf A_vol6_Ch9 (30 Hz).jpg',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5})
        return img


if __name__ == '__main__':
    app = MainApp()
    app.run()

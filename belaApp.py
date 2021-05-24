
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout

class belaLayout(BoxLayout):
    #create a buttn pressing function
    suma = 0
    counter = 0
    suma = 0
    counter_decko = 0
    counter_baba = 0
    counter_kralj = 0
    counter_AS = 0
    counter_deset = 0
    counter_devet = 0
    counter_deckoAdut = 0
    counter_zadnji = 0
    lista=[]
    def incrementDecko(self):
        self.ids.napomena_text.text=''
        self.ids['id_decko'].background_color = (0, 5,0, 1)

        self.ids['id_baba'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kralj'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kec'].background_color = (191, 191, 191, 0.82)
        self.ids['id_devet'].background_color = (500, 500, 500, 0.82)
        self.ids['id_deset'].background_color = (191, 191, 191, 0.82)
        self.ids['id_zadnji'].background_color = (191, 191, 191, 0.82)
        self.ids['id_deckoAdut'].background_color = (500, 500, 500, 0.82)

        self.counter_decko +=1 
        self.suma += 2
        self.ids.counter_text.text= str(self.suma)
        self.lista.append(2)
        self.ids.ukupno_text.text= ''
        if self.counter_decko>3:
            self.ids.napomena_text.text= "Unio si više od 3 dečka a da nisi onog u adutu!"
            self.suma=0
            self.lista= []
            self.ids.ukupno_text.text= ''
            self.ids.counter_text.text= str(self.suma)
            self.counter_decko = 0

    def incrementBaba(self):
        self.ids.napomena_text.text=''
        self.ids['id_baba'].background_color = (0, 5,0, 1)

        self.ids['id_decko'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kralj'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kec'].background_color = (191, 191, 191, 0.82)
        self.ids['id_devet'].background_color = (500, 500, 500, 0.82)
        self.ids['id_deset'].background_color = (191, 191, 191, 0.82)
        self.ids['id_zadnji'].background_color = (191, 191, 191, 0.82)
        self.ids['id_deckoAdut'].background_color = (500, 500, 500, 0.82)

        self.counter_baba +=1 
        self.suma += 3
        self.ids.counter_text.text= str(self.suma)
        self.lista.append(3)
        self.ids.ukupno_text.text= ''
        if self.counter_baba>4:
            self.ids.napomena_text.text= "Unio si više od 4 dame!"
            self.suma=0
            self.lista= []
            self.ids.ukupno_text.text= ''
            self.ids.counter_text.text= str(self.suma)
            self.counter_baba = 0

    def incrementKralj(self):
        self.ids.napomena_text.text=''
        self.ids['id_kralj'].background_color = (0, 5,0, 1)

        self.ids['id_baba'].background_color = (191, 191, 191, 0.82)
        self.ids['id_decko'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kec'].background_color = (191, 191, 191, 0.82)
        self.ids['id_devet'].background_color = (500, 500, 500, 0.82)
        self.ids['id_deset'].background_color = (191, 191, 191, 0.82)
        self.ids['id_zadnji'].background_color = (191, 191, 191, 0.82)
        self.ids['id_deckoAdut'].background_color = (500, 500, 500, 0.82)

        self.counter_kralj +=1 
        self.suma += 4
        self.ids.counter_text.text= str(self.suma)
        self.lista.append(4)
        self.ids.ukupno_text.text= ''
        if self.counter_kralj>4:
            self.ids.napomena_text.text= "Unio si više od 4 kralja!"
            self.suma=0
            self.lista= []
            self.ids.ukupno_text.text= ''
            self.ids.counter_text.text= str(self.suma)
            self.counter_kralj = 0

    def incrementAS(self):
        self.ids.napomena_text.text=''
        self.ids['id_kec'].background_color = (0, 5,0, 1)
        
        self.ids['id_kralj'].background_color = (191, 191, 191, 0.82)
        self.ids['id_baba'].background_color = (191, 191, 191, 0.82)
        self.ids['id_decko'].background_color = (191, 191, 191, 0.82)
        self.ids['id_devet'].background_color = (500, 500, 500, 0.82)
        self.ids['id_deset'].background_color = (191, 191, 191, 0.82)
        self.ids['id_zadnji'].background_color = (191, 191, 191, 0.82)
        self.ids['id_deckoAdut'].background_color = (500, 500, 500, 0.82)
        
        self.counter_AS +=1 
        self.suma += 11
        self.ids.counter_text.text= str(self.suma)
        self.lista.append(11)
        self.ids.ukupno_text.text= ''
        if self.counter_AS>4:
            self.ids.napomena_text.text= "Unio si više od 4 asa!"
            self.suma=0
            self.lista= []
            self.ids.ukupno_text.text= ''
            self.ids.counter_text.text= str(self.suma)
            self.counter_AS = 0
    
    def incrementDeset(self):
        self.ids.napomena_text.text=''
        self.ids['id_deset'].background_color = (0, 5,0, 1)

        self.ids['id_kec'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kralj'].background_color = (191, 191, 191, 0.82)
        self.ids['id_baba'].background_color = (191, 191, 191, 0.82)
        self.ids['id_decko'].background_color = (191, 191, 191, 0.82)
        self.ids['id_devet'].background_color = (500, 500, 500, 0.82)
        self.ids['id_zadnji'].background_color = (191, 191, 191, 0.82)
        self.ids['id_deckoAdut'].background_color = (500, 500, 500, 0.82)

        self.counter_deset +=1 
        self.suma += 10
        self.ids.counter_text.text= str(self.suma)
        self.lista.append(10)
        self.ids.ukupno_text.text= ''
        if self.counter_deset>4:
            self.ids.napomena_text.text= "Unio si više od 4 desetke!"
            self.suma=0
            self.lista= []
            self.ids.ukupno_text.text= ''
            self.ids.counter_text.text= str(self.suma)
            self.counter_deset = 0

    def incrementDevet(self):
        self.ids.napomena_text.text=''
        self.ids['id_devet'].background_color = (0, 5,0, 1)

        self.ids['id_deset'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kec'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kralj'].background_color = (191, 191, 191, 0.82)
        self.ids['id_baba'].background_color = (191, 191, 191, 0.82)
        self.ids['id_decko'].background_color = (191, 191, 191, 0.82)
        self.ids['id_zadnji'].background_color = (191, 191, 191, 0.82)
        self.ids['id_deckoAdut'].background_color = (500, 500, 500, 0.82)

        self.counter_devet +=1 
        self.suma += 14
        self.ids.counter_text.text= str(self.suma)
        self.lista.append(14)
        self.ids.ukupno_text.text= ''
        if self.counter_devet>1:
            self.ids.napomena_text.text= "Unio si više od jedne devetke!"
            self.suma=0
            self.lista= []
            self.ids.ukupno_text.text= ''
            self.ids.counter_text.text= str(self.suma)
            self.counter_devet = 0

    def incrementDeckoAdut(self):
        self.ids.napomena_text.text=''
        self.ids['id_deckoAdut'].background_color = (0, 5,0, 1)

        self.ids['id_devet'].background_color = (500, 500, 500, 0.82)
        self.ids['id_deset'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kec'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kralj'].background_color = (191, 191, 191, 0.82)
        self.ids['id_baba'].background_color = (191, 191, 191, 0.82)
        self.ids['id_decko'].background_color = (191, 191, 191, 0.82)
        self.ids['id_zadnji'].background_color = (191, 191, 191, 0.82)

        self.counter_deckoAdut +=1 
        self.suma += 20
        self.ids.counter_text.text= str(self.suma)
        self.lista.append(20)
        self.ids.ukupno_text.text= ''
        if self.counter_deckoAdut>1:
            self.ids.napomena_text.text= "Unio si više od jednog dečka u adutu!"
            self.suma=0
            self.lista= []
            self.ids.ukupno_text.text= ''
            self.ids.counter_text.text= str(self.suma)
            self.counter_deckoAdut = 0

    def incrementZadnji(self):
        self.ids.napomena_text.text=''
        self.ids['id_zadnji'].background_color = (0, 5,0, 1)

        self.ids['id_deckoAdut'].background_color = (500, 500, 500, 0.82)
        self.ids['id_devet'].background_color = (500, 500, 500, 0.82)
        self.ids['id_deset'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kec'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kralj'].background_color = (191, 191, 191, 0.82)
        self.ids['id_baba'].background_color = (191, 191, 191, 0.82)
        self.ids['id_decko'].background_color = (191, 191, 191, 0.82)
        
        self.counter_zadnji +=1
        self.suma += 10
        self.ids.counter_text.text= str(self.suma)
        self.lista.append(100)
        self.ids.ukupno_text.text= ''
        if self.counter_zadnji>1:
            self.ids.napomena_text.text= "Unio si više od jednog zadnjeg štiha!"
            self.suma=0
            self.lista= []
            self.ids.ukupno_text.text= ''
            self.ids.counter_text.text= str(self.suma)
            self.counter_zadnji = 0
   

    def reset(self):
        # self.counter = 0
        # self.root.ids.counter_text.text = str(self.counter)
        self.ids['id_deckoAdut'].background_color = (500, 500, 500, 0.82)
        self.ids['id_devet'].background_color = (500, 500, 500, 0.82)
        self.ids['id_deset'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kec'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kralj'].background_color = (191, 191, 191, 0.82)
        self.ids['id_baba'].background_color = (191, 191, 191, 0.82)
        self.ids['id_decko'].background_color = (191, 191, 191, 0.82)
        self.ids['id_zadnji'].background_color = (191, 191, 191, 0.82)
        
        self.suma = 0
        self.ids.counter_text.text = str(self.suma)
        self.ids.ukupno_text.text= ''
        self.ids.napomena_text.text= ''
        self.lista=[]
        self.counter_decko = 0
        self.counter_deckoAdut = 0
        self.counter_deset = 0
        self.counter_devet= 0
        self.counter_zadnji = 0
        self.counter_AS = 0
        self.counter_baba = 0
        self.counter_kralj = 0

    def incrementAll(self):
        self.ids['id_deckoAdut'].background_color = (500, 500, 500, 0.82)
        self.ids['id_devet'].background_color = (500, 500, 500, 0.82)
        self.ids['id_deset'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kec'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kralj'].background_color = (191, 191, 191, 0.82)
        self.ids['id_baba'].background_color = (191, 191, 191, 0.82)
        self.ids['id_decko'].background_color = (191, 191, 191, 0.82)
        self.ids['id_zadnji'].background_color = (191, 191, 191, 0.82)

        self.ids.ukupno_text.text = str(self.suma)
        self.ids.counter_text.text= '0'
        self.ids.napomena_text.text= ''
        self.lista=[]
        self.suma = 0
        self.counter_decko = 0
        self.counter_baba = 0
        self.counter_kralj = 0
        self.counter_AS = 0
        self.counter_deset = 0
        self.counter_devet = 0
        self.counter_deckoAdut = 0
        self.counter_zadnji = 0

    
    def decrement(self):
        self.ids['id_deckoAdut'].background_color = (500, 500, 500, 0.82)
        self.ids['id_devet'].background_color = (500, 500, 500, 0.82)
        self.ids['id_deset'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kec'].background_color = (191, 191, 191, 0.82)
        self.ids['id_kralj'].background_color = (191, 191, 191, 0.82)
        self.ids['id_baba'].background_color = (191, 191, 191, 0.82)
        self.ids['id_decko'].background_color = (191, 191, 191, 0.82)
        self.ids['id_zadnji'].background_color = (191, 191, 191, 0.82)
        if len(self.lista)>0:
            if self.lista[-1]==2:
                self.lista.remove(self.lista[-1])
                self.suma -=2
                self.ids.counter_text.text= str(self.suma)
                self.counter_decko -=1
            elif self.lista[-1]==3:
                self.lista.remove(self.lista[-1])
                self.suma -=3
                self.ids.counter_text.text= str(self.suma)
                self.counter_baba -=1
            elif self.lista[-1]==4:
                self.lista.remove(self.lista[-1])
                self.suma -=4
                self.ids.counter_text.text= str(self.suma)
                self.counter_kralj-=1
            elif self.lista[-1]==10:
                self.lista.remove(self.lista[-1])
                self.suma -=10
                self.ids.counter_text.text= str(self.suma)
                self.counter_deset -=1
            elif self.lista[-1]==11:
                self.lista.remove(self.lista[-1])
                self.suma -=11
                self.ids.counter_text.text= str(self.suma)
                self.counter_AS -=1
            elif self.lista[-1]==14:
                self.lista.remove(self.lista[-1])
                self.suma -=14
                self.ids.counter_text.text= str(self.suma)
                self.counter_devet -=1
            elif self.lista[-1]==20:
                self.lista.remove(self.lista[-1])
                self.suma -=20
                self.ids.counter_text.text= str(self.suma)
                self.counter_deckoAdut -=1
            else:
                self.lista.remove(self.lista[-1])
                self.suma -=10
                self.ids.counter_text.text= str(self.suma)
                self.counter_zadnji -=1
        else:
            self.ids.counter_text.text= '0'
            self.ids.ukupno_text.text= ''
            self.suma = 0
            self.lista=[]
            self.ids.napomena_text.text= ''
            self.counter_decko = 0
            self.counter_baba = 0
            self.counter_kralj = 0
            self.counter_AS = 0
            self.counter_deset = 0
            self.counter_devet = 0
            self.counter_deckoAdut = 0
            self.counter_zadnji = 0
        



 


class belaApp(App):
    def build(self):
        return belaLayout()
if __name__=='__main__':
    ba = belaApp()
    ba.run()
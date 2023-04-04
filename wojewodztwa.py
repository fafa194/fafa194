rmf = {"kujawsko-pomorskie","dolnośląskie", "lubuskie", "łódzkie","mazowieckie","podlaskie","pomorskie","śląskie","świętokrzyskie","warmińsko-mazurskie","wielkopolskie","zachodniopomorskie"}
zet = {"kujawsko-pomorskie","dolnośląskie", "lubelskie", "lubuskie", "łódzkie","podkarpackie","śląskie","świętokrzyskie","warmińsko-mazurskie","wielkopolskie","zachodniopomorskie"}
eska = {"lubelskie", "lubuskie","mazowieckie","opolskie","podkarpackie","podlaskie","świętokrzyskie","warmińsko-mazurskie"}
vox = {"lubelskie", "lubuskie", "łódzkie","małopolskie","mazowieckie","opolskie","pomorskie","śląskie","świętokrzyskie",}
disco = {"kujawsko-pomorskie","dolnośląskie", "lubelskie", "lubuskie", "łódzkie","małopolskie","mazowieckie","opolskie","podkarpackie"}
wnet = {"kujawsko-pomorskie","dolnośląskie","mazowieckie","opolskie","podkarpackie","podlaskie","świętokrzyskie"}
pollo = {"kujawsko-pomorskie","dolnośląskie", "lubelskie", "lubuskie", "łódzkie","małopolskie","mazowieckie","opolskie","warmińsko-mazurskie","wielkopolskie","zachodniopomorskie"}
regionalne = {"opolskie","podkarpackie","podlaskie","pomorskie","śląskie","świętokrzyskie","warmińsko-mazurskie","wielkopolskie","zachodniopomorskie"}
zlote_przeboje = {"podkarpackie","podlaskie","pomorskie","śląskie","świętokrzyskie"}

radio_array_list = [rmf,zet,eska,vox,disco,wnet,pollo,regionalne]
radio_array_list_strings = ['RMF', 'ZET', 'ESKA', 'VOX', 'DISCO', 'WNET', 'POLLO', 'REGIONALNE']

i = 0
j = 0

# Sprawdzamy jakie jest pokrycie dla kazdego radia
for i, each_radio in enumerate(radio_array_list):
    each_radio_len = len(each_radio) # Zasięg zmierzony w liczbie
    print(radio_array_list_strings[i], each_radio_len)
    # Kazdy zasięg porównuję z każdym
    for j in range(len(radio_array_list_strings)):
        radio_minus_radio = set(each_radio) - set(radio_array_list[j]) # Które zasięgi nie pokrywają się
        if len(radio_minus_radio) == 0:
            print("OK")
        else:
            print(radio_minus_radio, radio_array_list_strings[i], " I " , radio_array_list_strings[j])
rmf = {"kujawsko-pomorskie","dolnośląskie", "lubuskie", "łódzkie","mazowieckie","podlaskie","pomorskie","śląskie","świętokrzyskie","warmińsko-mazurskie","wielkopolskie"}
zet = {"kujawsko-pomorskie","dolnośląskie", "lubelskie", "lubuskie", "łódzkie","podkarpackie","śląskie","zachodniopomorskie"}
eska = {"lubelskie", "lubuskie","mazowieckie","opolskie","podkarpackie","podlaskie","świętokrzyskie","warmińsko-mazurskie"}
vox = {"lubelskie", "lubuskie", "łódzkie","małopolskie","mazowieckie","opolskie","pomorskie","świętokrzyskie",}
disco = {"kujawsko-pomorskie","dolnośląskie", "lubelskie", "lubuskie", "łódzkie","małopolskie"}
wnet = {"kujawsko-pomorskie","dolnośląskie","mazowieckie","opolskie","podkarpackie","podlaskie","świętokrzyskie"}
pollo = {"kujawsko-pomorskie","dolnośląskie", "lubelskie", "lubuskie", "łódzkie","małopolskie","mazowieckie","opolskie","warmińsko-mazurskie","wielkopolskie"}
regionalne = {"opolskie","podkarpackie","podlaskie","pomorskie","śląskie","świętokrzyskie","warmińsko-mazurskie","wielkopolskie"}
zlote_przeboje = {"podkarpackie","podlaskie","pomorskie","śląskie","świętokrzyskie"}

radio_array_list = [rmf,zet,eska,vox,disco,wnet,pollo,regionalne]
radio_array_list_strings = ['RMF', 'ZET', 'ESKA', 'VOX', 'DISCO', 'WNET', 'POLLO', 'REGIONALNE']

i = 0
j = 0

# Sprawdzamy jakie jest pokrycie dla kazdego radia
for i, each_radio in enumerate(radio_array_list):
    each_radio_len = len(each_radio) # Zasięg zmierzony w liczbie
    print(radio_array_list_strings[i], "zasięg:", each_radio_len)
    # Kazdy zasięg porównuję z każdym
    for j in range(len(radio_array_list)):
        radio_minus_radio = each_radio - radio_array_list[j] # Które zasięgi nie pokrywają się
        radio_intersection = each_radio & radio_array_list[j] # Które zasięgi się pokrywają
        if len(radio_intersection) > 0:
            total_range = len(radio_intersection | each_radio | radio_array_list[j])
            print(radio_array_list_strings[i], "i", radio_array_list_strings[j], "o łącznym zasięgu radiowym:", total_range)
    print()
import random

brojac = 0


class Korisnik:
    
    def __init__(self, ime, potreban_opseg, novac):
        self.ime = ime
        self.potreban_opseg = potreban_opseg
        self.novac = novac
        global brojac
        brojac =+ 3


def raspodela_listi(lista_novca, lista_korisnika, lista_opsega, lista_imena):
    global brojac
    for i in range(len(lista_korisnika)):
        lista_novca.append(lista_korisnika[i].novac)
        lista_opsega.append(lista_korisnika[i].potreban_opseg)
        lista_imena.append(lista_korisnika[i].ime)
        
        brojac += 3
    return lista_novca, lista_opsega, lista_imena



def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
 
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            global brojac
            
            if i == 0 or w == 0: 
                K[i][w] = 0

                brojac += 1

            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] 
                            + K[i-1][w-wt[i-1]], 
                            K[i-1][w]) 
                
                brojac += 1

            else: 
                K[i][w] = K[i-1][w] 
                
                brojac+= 1
                 
    return K[n][W], K 


def izdvajanje_imena(tabela, max_opseg, potrebni_opsezi, broj_korisnika, imena):
    global brojac

    imena_korisnika = []
    indeksi_odabranih = []

    for i in range(broj_korisnika,0,-1):

        if tabela[i][max_opseg] > tabela[i-1][max_opseg]:
            imena_korisnika.append(imena[i-1])
            indeksi_odabranih.append(i-1)
            max_opseg -= potrebni_opsezi[i-1]
            
            brojac += 3

        else: continue

    indeksi_odabranih.reverse()
    imena_korisnika.reverse()
    brojac += 4

    return indeksi_odabranih, imena_korisnika


def kladjenje(novac, cilj):

    global brojac

    pocetni_ulog = novac
    vrv = 0.5
    
    brojac += 2

    verovatnoce = [[0 for col in range(cilj + 1)] for row in range(4)]
    brojac += ((cilj+1) * 4)

    for i in range(3, -1, -1):
        if i == 3:
            if cilj > 2**4 * pocetni_ulog: return 0
            
            else:
                for j in range(cilj + 1):
                    if cilj > 2*j :
                        verovatnoce[i][j] = 0
                        brojac += 1

                    elif cilj == j :
                        verovatnoce[i][j] = 1
                        brojac += 1

                    else:
                        verovatnoce[i][j] = vrv
                        brojac += 1
    
        else:
            for j in range(cilj + 1):
                temp = [0]
                brojac += 1

                for k in range(cilj + 1):
                    if k + j >= cilj: break
                    if k > j: break
                    else:
                        temp.append(0.5 * verovatnoce[i+1][j+k] + 0.5 * verovatnoce[i+1][j-k])
                        brojac += 1


                verovatnoce[i][j] = max(temp)
                brojac += 1

    #vracamo tabelu verovatnoca i maksimalnu verovatnocu da ce doci do dobitka ako se ulozi 'pocetni_ulog'
    return verovatnoce[0][pocetni_ulog]


if __name__ == '__main__': 

    imena = []
    opsezi  = []
    cene = []
    korisnici = []
    brojac += 4

    for i in range(5):

        ime ='Korisnik{}'.format(i+1)
        opseg = round(random.uniform(0,200))
        cena = round(random.uniform(0,1000))
        korisnik = Korisnik(ime, opseg, cena)
        korisnici.append(korisnik) 
        brojac += 5

    #k1 = Korisnik('Branko', 60, 130)
    #k2 = Korisnik('Adam', 70, 140)
    #k3 = Korisnik('Sora', 65, 150)
    #k4 = Korisnik('Stijepo', 80, 160)

    
    dostupan_opseg = 200
    print()
    cene, opsezi, imena = raspodela_listi(cene, korisnici, opsezi, imena)
    for i in range(len(imena)):
        print('{} trazi opseg od {} MHz za cenu {} $'.format(imena[i], opsezi[i], cene[i]))

    zarada, lista_ranac = knapSack(dostupan_opseg, opsezi, cene, len(korisnici))
    print('\nKontrolor ce zaraditi: {} $\n'.format(zarada))

    indeksi_odabranih, odabrani = izdvajanje_imena(lista_ranac, dostupan_opseg, opsezi, len(korisnici), imena)
    print('Korisnici koji su dobili opseg su: {}\n'.format(odabrani))

    neodabrani = []
    brojac += 1

    for i in range(len(imena)):
        if i not in indeksi_odabranih:
            neodabrani.append(imena[i])
            brojac += 1
    
    print('Korisnici koji nisu dobili opseg: {}\n'.format(neodabrani))

    broj_kladjenja = 3
    brojac += 1

    for i in range(broj_kladjenja):
        
        neodabrani_korisnici = []
        brojac += 1

        for i in korisnici:
            if i.ime in neodabrani:
                neodabrani_korisnici.append(i)
                brojac += 1
        
        odabrani_korisnici = []
        dodeljeni_opsezi = []
        prihvacene_cene = []
        brojac += 3

        for i in korisnici:
            if i.ime in odabrani:
                odabrani_korisnici.append(i)
                dodeljeni_opsezi.append(i.potreban_opseg)    
                prihvacene_cene.append(i.novac)  
                brojac += 3

        #print(odabrani_korisnici, dodeljeni_opsezi, prihvacene_cene)

        


        #kladjenje
        koeficijent = random.uniform(1.2, 1.8) 
        pomocna_lista1 = [] #lista onih koji imaju mogucnost kladjenja
        lista_ciljeva = []
        brojac += 3

        for i in neodabrani_korisnici:
            

            pomocni_opsezi2 = []
            cene2 = []
            
            brojac += 2

            for j in range(len(dodeljeni_opsezi)):
                if dodeljeni_opsezi[j] > i.potreban_opseg:
                    pomocni_opsezi2.append(opsezi[j])
                    cene2.append(prihvacene_cene[j])
                    brojac += 2


            #if len(cene2) != 0:
            #    cilj = min(cene2)
            #    brojac += 1

            #else:
                cilj = round(koeficijent * i.novac)
                brojac += 1
            
            if kladjenje(i.novac, cilj) > 0.3:
                pomocna_lista1.append(i)
                lista_ciljeva.append(cilj)
                brojac += 2
    
        pomocna_lista2 = []  #lista korisnika koji su odlucili da se klade
        brojac += 1

        for i in pomocna_lista1:
            if random.random() > 0.5:
                pomocna_lista2.append(i)
                brojac += 1

        if len(pomocna_lista2) == 0:
            print('Korisnici su odlucili da se ne klade!')
            break

        indikator_kladjenja = 0
        brojac += 1

        for i in pomocna_lista2:
            
            indikator_kladjenja = 1
            brojac += 1

            print('Korisnik {} se kladi.\n'.format(i.ime))
            for j in range(4):

                

                print('Na raspolaganju je {}, a cilj je {}'.format(i.novac, lista_ciljeva[pomocna_lista2.index(i)]))
                #ulog_stari = int(input('Unesite ulog: '))
                if i.novac >= lista_ciljeva[pomocna_lista2.index(i)]:
                    print('')

                ulog = round(random.uniform(0, i.novac))
                i.novac -= ulog
                brojac += 2

                
                if random.random() > 0.5:
                    i.novac += 2 * ulog
                    brojac += 1

                if i.novac >= lista_ciljeva[pomocna_lista2.index(i)]:
                    print('\nDostignut iznos je {}$'.format(i.novac))
                    print('Dostigli ste cilj.\n')
                    break

                if i.novac <= 0:
                    print('\nIzgubili ste sav novac\n')
                    break
                if i.novac > 0 and i.novac < lista_ciljeva[pomocna_lista2.index(i)]:
                    print('Novi iznos je {}$\n'.format(i.novac))
        
        print()
        if indikator_kladjenja == 1:
            cene = []
            opsezi = []
            imena = []
            brojac += 3

            cene, opsezi, imena = raspodela_listi(cene, korisnici, opsezi, imena)
            for i in range(len(imena)):
                print('{} trazi opseg od {} MHz za cenu {} $'.format(imena[i], opsezi[i], cene[i]))
            zarada, lista_ranac= knapSack(dostupan_opseg, opsezi, cene, len(korisnici))
            print('\nKontrolor ce zaraditi: {} $\n'.format(zarada))
            indeksi_odabranih, odabrani = izdvajanje_imena(lista_ranac, dostupan_opseg, opsezi, len(korisnici), imena)
            print('Korisnici koji su dobili opseg su: {}\n'.format(odabrani))
            neodabrani = []
            brojac += 1

            for i in range(len(imena)):
                if i not in indeksi_odabranih:
                    neodabrani.append(imena[i])
                    brojac += 1
            
            print('Korisnici koji nisu dobili opseg: {}\n'.format(neodabrani))
            indikator_kladjenja = 0
    print(brojac)


import random

class Moshtari:
    
    print('....Etelate Moshtari....')
    name = input('Nam khod ra vared konid: ')
    cart = input('Shomare cart khod ra vared konid: ')
    mojodi = random.randint(100000,1000000)
    print()


class Foroshghah(Moshtari):
    List_Mahsolat = {'chips' :[{'1.mazmaz':[27000,100]}, {'2.chitoz':[30000,50]}],
                     'pofak' :[{'1.mazmaz':[29700,0]}, {'2.chitoz':[430000,120]}, {'3.chakelz':[20000,70]}],
                     'shir'  :[{'1.kalleh':[28000,30]}, {'2.pegah':[30000,50]}],
                     'mast'  :[{'1.mihan':[115000,40]}, {'2.chopan':[100000,30]}],
                     }
    
    @classmethod
    def __init__(cls):
        M = Moshtari()
        print('....List Mahsolat....')
        code_mahsolat = 1
        for esm_jens,List_brand in Foroshghah.List_Mahsolat.items():
            print(f'{code_mahsolat}.{esm_jens}:')
            code_mahsolat +=1
            for brand in List_brand:
                for esm_brand,data in brand.items():
                    print(f'{esm_brand} >> ghimat:{data[0]} toman , tedad:{data[1]} ')
            print('------------------')
            
        print()

    @classmethod
    def tozihat(cls):
        try:
            esm_jens = int(input('code mahsol ra vared konid: '))
        except:
            print('\n>>> faghat adad vared konid! <<<\n')
            esm_jens = int(input('code mahsol ra vared konid: '))
        print()
        if esm_jens == 1:
            print('>>chips ha 2 brend ast: mazmaz va chitoz')
        elif esm_jens == 2:
            print('>>pofak ha 3 brend ast: mazmaz va chitoz va chakelz')
        elif esm_jens == 3:
            print('>>shir ha 2 brend ast: kalleh va pegah')
        elif esm_jens == 4:
            print('>>mast ha 2 brend ast: mihan va chopan')

    @classmethod
    def dastebandi(cls):
        try:
            D = int(input('''Dastebandi Mahsolat Foroshghah:
1.tanagholat
2.labaniyat
(adad vared konid): '''))
        except:
            print('\n>>> faghat adad vared konid! <<<\n')
            D = int(input('''Dastebandi Mahsolat Foroshghah:
1.tanagholat
2.labaniyat
(adad vared konid): '''))
        print()
        if D == 1:
            print('~tanagholat~')
            print('chips , pofak')
            
        elif D == 2:
            print('~labaniyat~')
            print('shir , mast')
    

    Sabad_kharid =dict()
    def kharid(self):
        print('....kharid....')
        mahsol = input('esm mahsol ra vared konid: ')
        if mahsol in Foroshghah.List_Mahsolat:
            code_brand = int(input('code brand ra vared konid: '))
            if code_brand <= len(Foroshghah.List_Mahsolat[mahsol]):
                tedad = int(input('tedad ra vared konid: '))
                key= list(Foroshghah.List_Mahsolat[mahsol][code_brand-1].keys())[0]
                ghimat_mahsol = Foroshghah.List_Mahsolat[mahsol][code_brand-1][key][0]
                if tedad <= Foroshghah.List_Mahsolat[mahsol][code_brand-1][key][1]:
                    print('kharid shod!')
                else:
                    print('tedad mojaz nist!')
            else:
                print('code brand mojaz nist!')
        else:
            print('esm mahsol mojaz nist!')

        kharid = { mahsol :[{key:[ghimat_mahsol,tedad]}]}
        if mahsol in Foroshghah.Sabad_kharid:
            Foroshghah.Sabad_kharid[mahsol].append({key:[ghimat_mahsol,tedad]})
        else:
            Foroshghah.Sabad_kharid.update(kharid)
            

    @classmethod
    def sabad_kharid(cls):
        def tayeed_nahayee():
            tayeed= input('Aya Kharid khod ra tayeed mikonid?(y/n)')
            if tayeed == 'y':
                print('....Sabad Kharid....')
                kharid_kol = 0
                code_mahsolat = 1
                for esm_jens,List_brand in Foroshghah.Sabad_kharid.items():
                    print(f'{code_mahsolat}.{esm_jens}:')
                    code_mahsolat +=1
                    for brand in List_brand:
                        for esm_brand,data in brand.items():
                            majmo_kharid = data[0]*data[1]
                            print(f'{esm_brand} >> ghimat:{data[0]} toman , tedad:{data[1]} \n>majmo kharid: {majmo_kharid} toman')
                        kharid_kol += majmo_kharid
                    print('------------------')
                print(f'kharid kol: {kharid_kol} toman')
                print()

                # dargha_pardakht()

            else:
                Q = input('')
                rabetkarbari()

        def virayesh_kharid():
            virayesh= input('Aya ghast virayesh kharid darid?(y/n): ')
            if virayesh == 'y':
                q_virayesh = int(input('''1.delet kol Sabad kharid
2.delet yek mahsol
3.edit kharid'''))
                if q_virayesh == 1:
                    Foroshghah.Sabad_kharid.clear()
                elif q_virayesh == 2:
                    esm_jens = input('esm mahsol ra vared konid: ')
                    if esm_jens in Foroshghah.Sabad_kharid:
                        del Foroshghah.Sabad_kharid(esm_jens)
                        print('mahsol hazf shod!')
                    else:
                        print('esm mahsol mojaz nist!')
                elif q_virayesh == 3:
                    esm_jens = input('esm mahsol ra vared konid: ')
                    if esm_jens in Foroshghah.Sabad_kharid:
                        del Foroshghah.Sabad_kharid(esm_jens)
                        mahsol = input('esm mahsol jadid ra vared konid: ')
                        if mahsol in Foroshghah.List_Mahsolat:
                            code_brand = int(input('code brand ra vared konid: '))
                            if code_brand <= len(Foroshghah.List_Mahsolat[mahsol]):
                                tedad = int(input('tedad ra vared konid: '))
                                key= list(Foroshghah.List_Mahsolat[mahsol][code_brand-1].keys())[0]
                                ghimat_mahsol = Foroshghah.List_Mahsolat[mahsol][code_brand-1][key][0]
                                if tedad <= Foroshghah.List_Mahsolat[mahsol][code_brand-1][key][1]:
                                    print('kharid shod!')
                                else:
                                    print('tedad mojaz nist!')
                            else:
                                print('code brand mojaz nist!')
                        else:
                            print('esm mahsol mojaz nist!')
                        kharid = { mahsol :[{key:[ghimat_mahsol,tedad]}]}
                        if mahsol in Foroshghah.Sabad_kharid:
                            Foroshghah.Sabad_kharid[mahsol].append({key:[ghimat_mahsol,tedad]})
                        else:
                            Foroshghah.Sabad_kharid.update(kharid)
                                        
                    else:
                        print('esm mahsol mojaz nist!')
            else:
                tayeed_nahayee()
        virayesh_kharid()

    @classmethod
    def factor_kharid():
        print('....Factor Kharid....')
        kharid_kol = 0
        code_mahsolat = 1
        for esm_jens,List_brand in Foroshghah.Sabad_kharid.items():
            print(f'{code_mahsolat}.{esm_jens}:')
            code_mahsolat +=1
            for brand in List_brand:
                for esm_brand,data in brand.items():
                    majmo_kharid = data[0]*data[1]
                    print(f'{esm_brand} >> ghimat:{data[0]} toman , tedad:{data[1]} \n>majmo kharid: {majmo_kharid} toman')
                kharid_kol += majmo_kharid
            print('------------------')
        print(f'kharid kol: {kharid_kol} toman')
        print()
       

            
    @staticmethod
    def kharid_kol():
        for esm_jens,List_brand in Foroshghah.Sabad_kharid.items():
            for brand in List_brand:
                for esm_brand,data in brand.items():
                    majmo_kharid = data[0]*data[1]
                kharid_kol += majmo_kharid
        return kharid_kol
    


               



F =Foroshghah()


def rabetkarbari():
    
    try:
        H = int(input('''....panel karbari....
1.Tozihat
2.Dastebandi Mahsolat
3.Kharid(va afzodan Kharid)
4.Sabad Kharid(va tayeed Kharid)
5.Factor Kharid(nayesh kharid ha)
(adad amaliyat ra vared konid): '''))
    except:
        print('\n>>> faghat adad vared konid! <<<\n')
        H = int(input('''....panel karbari....
1.Tozihat mahsol 
2.Dastebandi Mahsolat
3.Kharid(va edame Kharid)
4.Sabad Kharid(ba virayesh va tayeed Kharid)
5.5.Factor Kharid(nayesh kharid ha)
(adad amaliyat ra vared konid): '''))
    
    if H == 1:
        F.tozihat()
    elif H == 2:
        F.dastebandi()
    elif H == 3:
        F.kharid()
    elif H == 4:
        F.sabad_kharid()
    elif H == 5:
        F.factor_kharid()

    print()
    rabetkarbari()


rabetkarbari()
    








"""
Module baraye simolateshon ye system foroshgah sade.
Shamel class haye Moshtari va Foroshghah ast.
"""

import random
from shop import *


class Moshtari:
    """Class baraye negahdari etelaat moshtari."""

    print("....Etelate Moshtari....")
    name = input("Nam khod ra vared konid: ")
    cart = input("Shomare cart khod ra vared konid: ")
    mojodi = random.randint(100000, 1000000)
    print()


class Foroshghah(Moshtari):
    """Class foroshgah ke shamel list mahsolat, amaliyat kharid va sabad kharid ast."""

    list_mahsolat = {
        "chips": [{"1.mazmaz": [27000, 100]}, {"2.chitoz": [30000, 50]}],
        "pofak": [{"1.mazmaz": [29700, 0]}, {"2.chitoz": [430000, 120]}, {"3.chakelz": [20000, 70]}],
        "shir": [{"1.kalleh": [28000, 30]}, {"2.pegah": [30000, 50]}],
        "mast": [{"1.mihan": [115000, 40]}, {"2.chopan": [100000, 30]}],
    }

    sabad_kharid = {}

    @classmethod
    def __init__(cls):
        """Method sazande class Foroshghah."""
        Moshtari()

        print("....List Mahsolat....")
        code_mahsolat = 1
        for esm_jens, list_brand in Foroshghah.list_mahsolat.items():
            print(f"{code_mahsolat}.{esm_jens}:")
            code_mahsolat += 1
            for brand in list_brand:
                for esm_brand, data in brand.items():
                    print(f"{esm_brand} >> ghimat:{data[0]} toman , tedad:{data[1]} ")
            print("------------------")

        print()

    @classmethod
    def tozihat(cls):
        """Namayesh tozihat bishtar dar mored brandhaye mahsolat."""
        try:
            esm_jens = int(input("code mahsol ra vared konid: "))
        except ValueError:
            print("\n>>> faghat adad vared konid! <<<\n")
            esm_jens = int(input("code mahsol ra vared konid: "))
        print()
        if esm_jens == 1:
            print(">>chips ha 2 brend ast: mazmaz va chitoz")
        elif esm_jens == 2:
            print(">>pofak ha 3 brend ast: mazmaz va chitoz va chakelz")
        elif esm_jens == 3:
            print(">>shir ha 2 brend ast: kalleh va pegah")
        elif esm_jens == 4:
            print(">>mast ha 2 brend ast: mihan va chopan")

    @classmethod
    def dastebandi(cls):
        """Dastebandi mahsolat foroshgah ra namayesh midahad."""
        try:
            dastebandi_choice = int(
                input(
                    """Dastebandi Mahsolat Foroshghah:
1.tanagholat
2.labaniyat
(adad vared konid): """
                )
            )
        except ValueError:
            print("\n>>> faghat adad vared konid! <<<\n")
            dastebandi_choice = int(
                input(
                    """Dastebandi Mahsolat Foroshghah:
1.tanagholat
2.labaniyat
(adad vared konid): """
                )
            )
        print()
        if dastebandi_choice == 1:
            print("~tanagholat~")
            print("chips , pofak")

        elif dastebandi_choice == 2:
            print("~labaniyat~")
            print("shir , mast")

    def kharid(self):
        """Amaliyat kharid ye mahsol va afzoodan an be sabad kharid ra anjam midahad."""
        print("....kharid....")
        mahsol = input("esm mahsol ra vared konid: ")
        key = None
        ghimat_mahsol = 0
        tedad = 0

        if mahsol in Foroshghah.list_mahsolat:
            try:
                code_brand = int(input("code brand ra vared konid: "))
                if 1 <= code_brand <= len(Foroshghah.list_mahsolat[mahsol]):
                    tedad = int(input("tedad ra vared konid: "))
                    key = list(Foroshghah.list_mahsolat[mahsol][code_brand - 1].keys())[
                        0
                    ]
                    ghimat_mahsol = Foroshghah.list_mahsolat[mahsol][code_brand - 1][
                        key
                    ][0]

                    if (
                        tedad
                        <= Foroshghah.list_mahsolat[mahsol][code_brand - 1][key][1]
                    ):
                        print("kharid shod!")
                    else:
                        print("tedad mojaz nist!")
                        return
                else:
                    print("code brand mojaz nist!")
                    return
            except ValueError:
                print(">>> faghat adad vared konid! <<<")
                return
        else:
            print("esm mahsol mojaz nist!")
            return

        kharid_item = {mahsol: [{key: [ghimat_mahsol, tedad]}]}
        if mahsol in Foroshghah.sabad_kharid:
            Foroshghah.sabad_kharid[mahsol].append({key: [ghimat_mahsol, tedad]})
        else:
            Foroshghah.sabad_kharid.update(kharid_item)
        

    @classmethod
    def Sabad_kharid(cls):
        """Namayesh sabad kharid, emkane virayesh ya tayeed nahayee kharid ra faraham mikonad."""

        def tayeed_nahayee():
            """Tayeed nahayee kharid va namayesh factor nahayee."""
            Foroshghah.factor_kharid()
            tayeed = input("Aya Kharid khod ra tayeed mikonid?(y/n)")
            if tayeed == "y":
                print("....Sabad Kharid....")
                kharid_kol = 0
                code_mahsolat = 1
                for esm_jens, list_brand in Foroshghah.sabad_kharid.items():
                    print(f"{code_mahsolat}.{esm_jens}:")
                    code_mahsolat += 1
                    for brand in list_brand:
                        for esm_brand, data in brand.items():
                            majmo_kharid = data[0] * data[1]
                            print(
                                f"{esm_brand} >> ghimat:{data[0]} toman , tedad:{data[1]} \n"
                                f">majmo kharid: {majmo_kharid} toman"
                            )
                        kharid_kol += majmo_kharid
                    print("------------------")
                print(f"kharid kol: {kharid_kol} toman")
                print()

                Pardakht()

            

        def virayesh_kharid():
            """Emkane hazf ya virayesh ye item dar sabad kharid ra faraham mikonad."""
            Foroshghah.factor_kharid()
            virayesh = input("Aya ghast virayesh kharid darid?(y/n): ")
            if virayesh == "y":
                try:
                    q_virayesh = int(
                        input(
                            """1.delet kol Sabad kharid
2.delet yek mahsol
3.edit kharid
(adad vared konid): """
                        )
                    )
                except ValueError:
                    print(">>> faghat adad vared konid! <<<")
                    return

                if q_virayesh == 1:
                    Foroshghah.sabad_kharid.clear()
                elif q_virayesh == 2:
                    esm_jens = input("esm mahsol ra vared konid: ")
                    if esm_jens in Foroshghah.sabad_kharid:
                        Foroshghah.sabad_kharid.pop(esm_jens)
                        print("mahsol hazf shod!")
                    else:
                        print("esm mahsol mojaz nist!")
                elif q_virayesh == 3:
                    esm_jens_old = input("esm mahsoli ke mikhahid virayesh konid: ")
                    if esm_jens_old in Foroshghah.sabad_kharid:
                        Foroshghah.sabad_kharid.pop(esm_jens_old)

                        mahsol_new = input("esm mahsol jadid ra vared konid: ")
                        if mahsol_new in Foroshghah.list_mahsolat:
                            try:
                                code_brand = int(input("code brand ra vared konid: "))
                                if (
                                    1
                                    <= code_brand
                                    <= len(Foroshghah.list_mahsolat[mahsol_new])
                                ):
                                    tedad_new = int(input("tedad ra vared konid: "))
                                    key_new = list(
                                        Foroshghah.list_mahsolat[mahsol_new][
                                            code_brand - 1
                                        ].keys()
                                    )[0]
                                    ghimat_mahsol_new = Foroshghah.list_mahsolat[
                                        mahsol_new
                                    ][code_brand - 1][key_new][0]
                                    if (
                                        tedad_new
                                        <= Foroshghah.list_mahsolat[mahsol_new][
                                            code_brand - 1
                                        ][key_new][1]
                                    ):
                                        print("virayesh shod!")
                                        kharid_item_new = {
                                            mahsol_new: [
                                                {
                                                    key_new: [
                                                        ghimat_mahsol_new,
                                                        tedad_new,
                                                    ]
                                                }
                                            ]
                                        }
                                        if mahsol_new in Foroshghah.sabad_kharid:
                                            Foroshghah.sabad_kharid[mahsol_new].append(
                                                {
                                                    key_new: [
                                                        ghimat_mahsol_new,
                                                        tedad_new,
                                                    ]
                                                }
                                            )
                                        else:
                                            Foroshghah.sabad_kharid.update(
                                                kharid_item_new
                                            )

                                    else:
                                        print("tedad mojaz nist!")
                                else:
                                    print("code brand mojaz nist!")
                            except ValueError:
                                print(">>> faghat adad vared konid! <<<")

                        else:
                            print("esm mahsol jadid mojaz nist!")
                    else:
                        print("esm mahsol baraye virayesh mojaz nist!")
            else:
                tayeed_nahayee()

        virayesh_kharid()

    @classmethod
    def factor_kharid(cls):
        """Factor nahayee kharid ra namayesh midahad."""
        print("\n....Factor Kharid....")
        kharid_kol = 0
        code_mahsolat = 1
        for esm_jens, list_brand in Foroshghah.sabad_kharid.items():
            print(f"{code_mahsolat}.{esm_jens}:")
            code_mahsolat += 1
            for brand in list_brand:
                for esm_brand, data in brand.items():
                    majmo_kharid = data[0] * data[1]
                    print(
                        f"{esm_brand} >> ghimat:{data[0]} toman , tedad:{data[1]} \n"
                        f">majmo kharid: {majmo_kharid} toman"
                    )
                kharid_kol += majmo_kharid
            print("------------------")
        print(f"kharid kol: {kharid_kol} toman")
        print()

    @staticmethod
    def kharid_kol():
        """Majmo kol hazine kharid ra mohasebe va baz migardanad."""
        kharid_kol = 0
        for esm_jens, list_brand in Foroshghah.sabad_kharid.items():
            for brand in list_brand:
                for esm_brand, data in brand.items():
                    majmo_kharid = data[0] * data[1]
                kharid_kol += majmo_kharid
        return kharid_kol


F = Foroshghah()

def Pardakht():
    print('entegal be darghah')
    #
    #
    #
    print('Moshtari badi:')
    F1 = Foroshghah()
    

def rabetkarbari():
    """Tabe rabet karbari asli baraye modiriat amaliyat foroshgah."""

    try:
        user_choice = int(
            input(
                """....panel karbari....
1.Tozihat
2.Dastebandi Mahsolat
3.Kharid(va afzodan Kharid)
4.Sabad Kharid(ba virayesh va tayeed Kharid)
5.Factor Kharid(nayesh kharid ha)
6.Pardakht(darhgah)
(adad amaliyat ra vared konid): """
            )
        )
    except ValueError:
        print("\n>>> faghat adad vared konid! <<<\n")
        user_choice = int(
            input(
                """....panel karbari....
1.Tozihat mahsol 
2.Dastebandi Mahsolat
3.Kharid(va edame Kharid)
4.Sabad Kharid(ba virayesh va tayeed Kharid)
5.Factor Kharid(nayesh kharid ha)
6.Pardakht(darhgah)
(adad amaliyat ra vared konid): """
            )
        )

    if user_choice == 1:
        F.tozihat()
        print()
        rabetkarbari()
    elif user_choice == 2:
        F.dastebandi()
        print()
        rabetkarbari()
    elif user_choice == 3:
        F.kharid()
        print()
        rabetkarbari()
    elif user_choice == 4:
        F.Sabad_kharid()
        print()
        rabetkarbari()
    elif user_choice == 5:
        F.factor_kharid()
        print()
        rabetkarbari()
    elif user_choice == 6:
        Pardakht()
    
rabetkarbari()

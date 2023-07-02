# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import locale
import re
import math
from frappe.utils import cstr
import frappe


class number2word(object):
    def __init__(self, number):
        self.number = float(abs(number))

    def validate(self):
        returnmsg = ""
        my_number = self.number
        english_format_number = self.convert_number(my_number)
        array_number1 = cstr(english_format_number).split(".")
        array_number = array_number1[0].split(",")

        for i in range(len(array_number)):
            place = len(array_number) - i
            returnmsg = returnmsg + self.convert(array_number[i], place)
            if (
                (0 <= i)
                and (i < len(array_number) - 1)
                and int(array_number[i + 1]) > 0
            ):
                returnmsg = returnmsg + " و "
        factor1 = re.sub(r"[^0-9]", "", array_number1[0])
        factor2 = re.sub(r"[^0-9]", "", array_number1[1])
        if int(factor1) == 0 and int(factor2) == 0:
            return "صفر"
        if int(factor1) != 0:
            returnmsg = returnmsg + " ريـال "
        if int(factor2) == 0:
            return returnmsg + "فقط لا غير"

        if int(factor2) != 0:
            if int(factor1) != 0:
                returnmsg = returnmsg + " و " + self.convert(array_number1[1], 1)
            else:
                returnmsg = self.convert(array_number1[1], 1)
            returnmsg = returnmsg + " هللة فقط لا غير "
            return returnmsg

    def convert_number(self, number):
        # locale.setlocale(locale.LC_ALL,'')
        num = "{:.2f}".format(self.number)
        xx = num.split(".")
        xx[0] = self.addcomma(xx[0])
        x = self.number
        x = float(x)
        x1 = xx[0] + "." + xx[1]
        if x < 0 or x > 999999999999:
            frappe.msgprint("العدد خارج النطاق")
            return ""
        else:
            return x1

    def addcomma(self, number):
        indexes = [
            3,
            7,
            11,
            15,
            19,
            23,
            27,
            31,
            35,
            39,
            43,
            47,
            51,
            55,
            59,
            63,
            67,
            71,
            75,
            79,
            83,
            87,
            91,
            95,
            99,
            103,
            107,
            111,
            115,
            119,
        ]
        rnumber = number[::-1]
        length = len(rnumber)
        number_of_comma = math.ceil(float(float(length) / float(3))) - 1
        for x in range(int(number_of_comma)):
            rnumber = rnumber[: indexes[x]] + "," + rnumber[indexes[x] :]
        returnNumber = rnumber[::-1]
        return returnNumber

    def convert(self, number, place):
        returnmsg = ""

        sex = "male"

        words = {
            "male": {
                "0": "",
                "1": "واحد",
                "2": "اثنان",
                "3": "ثلاثة",
                "4": "أربعة",
                "5": "خمسة",
                "6": "ستة",
                "7": "سبعة",
                "8": "ثمانية",
                "9": "تسعة",
                "10": "عشرة",
                "11": "أحد عشر",
                "12": "اثنا عشر",
                "13": "ثلاثة عشر",
                "14": "أربعة عشر",
                "15": "خمسة عشر",
                "16": "ستة عشر",
                "17": "سبعة عشر",
                "18": "ثمانية عشر",
                "19": "تسعة عشر",
                "20": "عشرون",
                "30": "ثلاثون",
                "40": "أربعون",
                "50": "خمسون",
                "60": "ستون",
                "70": "سبعون",
                "80": "ثمانون",
                "90": "تسعون",
                "100": "مئة",
                "200": "مئتان",
                "300": "ثلاثمائة",
                "400": "أربعمائة",
                "500": "خمسمائة",
                "600": "ستمائة",
                "700": "سبعمائة",
                "800": "ثمانمائة",
                "900": "تسعمائة",
            },
            "female": {
                "0": "",
                "1": "واحدة",
                "2": "اثنتان",
                "3": "ثلاث",
                "4": "أربع",
                "5": "خمس",
                "6": "ست",
                "7": "سبع",
                "8": "ثمان",
                "9": "تسع",
                "10": "عشر",
                "11": "إحدى عشرة",
                "12": "ثنتا عشرة",
                "13": "ثلاث عشرة",
                "14": "أربع عشرة",
                "15": "خمس عشرة",
                "16": "ست عشرة",
                "17": "سبع عشرة",
                "18": "ثمان عشرة",
                "19": "تسع عشرة",
                "20": "عشرون",
                "30": "ثلاثون",
                "40": "أربعون",
                "50": "خمسون",
                "60": "ستون",
                "70": "سبعون",
                "80": "ثمانون",
                "90": "تسعون",
                "100": "مئة",
                "200": "مئتان",
                "300": "ثلاثمائة",
                "400": "أربعمائة",
                "500": "خمسمائة",
                "600": "ستمائة",
                "700": "سبعمائة",
                "800": "ثمانمائة",
                "900": "تسعمائة",
            },
        }
        # 	//take in charge the different way of writing the thousands and millions ...
        # mil = list[
        #     '2' : list['1' : 'ألف', '2' : 'ألفان', '3' : 'آلاف'],
        #     '3' : list['1' : 'مليون', '2' : 'مليونان', '3' : 'ملايين'],
        #     '4' : list['1' : 'مليار', '2' : 'ملياران', '3' : 'مليارات'] ]
        mf = {"1": "male", "2": "male", "3": "male", "4": "male"}
        number_length = len(cstr(number))

        if int(number) == 0:
            return ""
        elif number[0] == 0:
            if number[1] == 0:
                number = int(number[:-1])
                return number
            else:
                number = int(number[:-2])
                return number

        returnmsg = ""
        number = cstr(number)
        if number_length == 1:
            # number=number+'one'
            if place == 1:
                returnmsg = returnmsg + words[mf[cstr(place)]][number]
            if place == 2:
                if int(number) == 1:
                    returnmsg = " ألف"
                elif int(number) == 2:
                    returnmsg = " ألفان"
                else:
                    returnmsg = returnmsg + words[mf[cstr(place)]][number] + " آلاف"
            if place == 3:
                if int(number) == 1:
                    returnmsg = returnmsg + " مليون"
                elif int(number) == 2:
                    returnmsg = returnmsg + " مليونان"
                else:
                    returnmsg = returnmsg + words[mf[cstr(place)]][number] + " ملايين"
            if place == 4:
                if int(number) == 1:
                    returnmsg = returnmsg + " مليار"
                elif int(number) == 2:
                    returnmsg = returnmsg + " ملياران"
                else:
                    returnmsg = returnmsg + words[mf[cstr(place)]][number] + " مليارات"

        elif number_length == 2:
            # number=number+'two'

            # if (words[mf[cstr(place)]][number]):
            if words[mf[cstr(place)]].__contains__(number):
                returnmsg = returnmsg + words[mf[cstr(place)]][number]
            else:
                twoy = int(number[0]) * 10
                ony = number[1]
                returnmsg = (
                    returnmsg
                    + words[mf[cstr(place)]][ony]
                    + " و "
                    + words[mf[cstr(place)]][cstr(twoy)]
                )

            if place == 2:
                returnmsg = returnmsg + " ألف"
            if place == 3:
                returnmsg = returnmsg + " مليون"
            if place == 4:
                returnmsg = returnmsg + " مليار"

        elif number_length == 3:
            # number=number+'three'
            # if (words[mf[cstr(place)]][number]):
            if words[mf[cstr(place)]].__contains__(cstr(number)):
                returnmsg = returnmsg + words[mf[cstr(place)]][cstr(number)]

                if int(number) == 200:
                    returnmsg = " مئتا"

                if place == 2:
                    returnmsg = returnmsg + " ألف"
                if place == 3:
                    returnmsg = returnmsg + " مليون"
                if place == 4:
                    returnmsg = returnmsg + " مليار"

                return returnmsg

            else:
                threey = int(number[0]) * 100
                threey = cstr(threey)
                if words[mf[cstr(place)]][threey]:
                    returnmsg = returnmsg + words[mf[cstr(place)]][threey]

                twoyony = (int(number[1]) * 10) + int(number[2])
                if int(twoyony) == 2:
                    if place == 1:
                        twoyony = words[mf[cstr(place)]]["2"]
                    if place == 2:
                        twoyony = " ألفان"
                    if place == 3:
                        twoyony = " مليونان"
                    if place == 4:
                        twoyony = " ملياران"

                    if int(threey) != 0:
                        twoyony = " و " + cstr(twoyony)

                    returnmsg = returnmsg + " " + twoyony

                elif int(twoyony) == 1:
                    twoyony = cstr(twoyony)
                    if place == 1:
                        twoyony = words[mf[cstr(place)]]["1"]
                    if place == 2:
                        twoyony = "ألف"
                    if place == 3:
                        twoyony = "مليون"
                    if place == 4:
                        twoyony = "مليار"

                    if int(threey) != 0:
                        twoyony = " و " + cstr(twoyony)

                    returnmsg = returnmsg + " " + twoyony
                else:
                    # if ((words[mf[cstr(place)]][twoyony])):
                    twoyony = cstr(twoyony)
                    if words[mf[cstr(place)]].__contains__(twoyony):
                        # if words.has_key(twoyony):
                        twoyony = words[mf[cstr(place)]][twoyony]
                    else:
                        twoy = int(number[1]) * 10
                        twoy = cstr(twoy)
                        ony = number[2]
                        twoyony = (
                            words[mf[cstr(place)]][ony]
                            + " و "
                            + words[mf[cstr(place)]][twoy]
                        )
                    if (twoyony != "") and (int(threey) != 0):
                        returnmsg = returnmsg + " و " + twoyony
                    else:
                        returnmsg = returnmsg + " " + twoyony

                    if place == 2:
                        returnmsg = returnmsg + " ألف"
                    if place == 3:
                        returnmsg = returnmsg + " مليون"
                    if place == 4:
                        returnmsg = returnmsg + " مليار"

        return returnmsg

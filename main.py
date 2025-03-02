def int_to_roman(num):
    roman = ""

    while True:
        if int(str(num)[0]) == 4 or int(str(num)[0]) == 9:
            if num-500 >= 0:
                roman += "CM"
                num -= 900
            
            elif num-100 >= 0:
                roman += "CD"
                num -= 400

            elif num-50 >= 0:
                roman += "XC"
                num -= 90

            elif num-10 >= 0:
                roman += "XL"
                num -= 40

            elif num-5 >= 0:
                roman += "IX"
                num -= 9

            elif num-1 >= 0:
                roman += "IV"
                num -= 4
        
        else:
            if num-1000 >= 0:
                roman += "M"
                num -= 1000

            elif num-500 >= 0:
                roman += "D"
                num -= 500               

            elif num-100 >= 0:
                roman += "C"
                num -= 100

            elif num-50 >= 0:
                roman += "L"
                num -= 50

            elif num-10 >= 0:
                roman += "X"
                num -= 10

            elif num-5 >= 0:
                roman += "V"
                num -= 5

            elif num-1 >= 0:
                roman += "I"
                num -= 1

            else:
                break
        
    return roman
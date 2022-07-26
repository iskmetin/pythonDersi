num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
             11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
             15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
             19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
             50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
             90: 'Ninety', 100: "Hundred", 200: "Twohundred", 300: "Threehundred", 400: "Fourhundred",
             500: "Fivehundred", 600: "Sixhundred", 700: "Sevenhundred", 800: "Eighthundred",
             900: "Ninehundred", 0: 'Zero'}


def n2w(n):
    try:
        print(num2words[n])
    except KeyError:
        try:
            print(num2words[n - n % 10] + num2words[n % 10].lower())
        except KeyError:
            try:
                print(num2words[n - n % 100] + num2words[n - n % 10 - n + n % 100] + num2words[n % 10].lower())
            except:
                print("false number")


sayi = int(input("sayi gir"))
n2w(sayi)

class BankAccount:
    def __init__(self, kontonummer, saldo):
        self.kontonummer = kontonummer
        self.saldo = saldo

    def insättningar(self, belopp):
        self.saldo += belopp
        print(f"ditt kontonummer är: {self.kontonummer}")
        print(f"ditt saldo är nuvarande: {self.saldo}")

        while True:
            svar = input("Vill du göra en till insättning? (ja/nej): ")
            if svar.lower() == "ja":
                extra_belopp = float(input("Ange beloppet att sätta in: "))
                self.saldo += extra_belopp
                print(f"Ditt saldo efter den extra insättningen är: {self.saldo}")
            elif svar.lower() == "nej":
                break
            else:
                print("Ogiltigt svar. Vänligen ange 'ja' eller 'nej'.")


bankaccount = BankAccount(122252, 123)
bankaccount.insättningar(100)

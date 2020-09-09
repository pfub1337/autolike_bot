import os
from time import sleep


class ConsoleUI:
    def __init__(self):
        os.system("color f")
        self.log_pass_data = list()
        # self.message = "Comment posted by AutolikeBot\n========CODED BY PFUB========"
        self.accs_read()
        self.main_menu()

    def accs_read(self):
        with open("logpass.txt") as f:
            for line in f:
                l = line
                self.log_pass_data.append(l.split())
        if len(self.log_pass_data) == 0:
            self.log_pass_data.append(["", "", int()])
            for i in range(5):
                self.log_pass_data.append(["", ""])
        elif (len(self.log_pass_data) > 0) and (len(self.log_pass_data) < 5):
            for i in range(6 - len(self.log_pass_data)):
                self.log_pass_data.append(["", ""])

    def accs_saving(self):
        with open("logpass.txt", "w") as f:
            f.writelines(" ".join(self.log_pass_data[0]))
            for i in range(1, 6):
                if self.log_pass_data[i][0] != "":
                    f.writelines("\n" + " ".join(self.log_pass_data[i]))

    def main_menu(self):
        os.system("cls")
        print("Welcome to Autolike bot")
        print("[1] Main account settings")
        print("[2] Bots accounts settings")
        print("[3] Start")
        print("[4] Settings and help")
        print("[5] Quit")
        main_menu_item = int(input("Select menu item: "))
        if main_menu_item < 1 or main_menu_item > 5:
            while True:
                main_menu_item = int(input("Select menu item: "))
                if main_menu_item >= 1 and main_menu_item <= 5:
                    break
                else:
                    continue
        elif main_menu_item == 1:
            self.main_acc_settings()
        elif main_menu_item == 2:
            self.bots_acc_settings()
        elif main_menu_item == 3:
            return self.log_pass_data
        elif main_menu_item == 4:
            self.ui_help()
        elif main_menu_item == 5:
            exit(0)

    def main_acc_settings(self):
        os.system("cls")
        print(f"Your main account data\nLogin: {self.log_pass_data[0][0]}\nPassword: {self.log_pass_data[0][1]}\nAccount id: {self.log_pass_data[0][2]}"
              if self.log_pass_data[0][0] != "" else "Your main account isn't added. Press 1 to add account")
        print("[1] Change account data")
        print("[2] Main menu")
        mas_item = int(input("Select menu item: "))
        if mas_item != 1 and mas_item != 2:
            while True:
                mas_item = int(input("Select menu item: "))
                if mas_item == 1 or mas_item == 2:
                    break
                else:
                    continue
        elif mas_item == 1:
            self.main_account_change()
        elif mas_item == 2:
            self.main_menu()

    def bots_acc_settings(self):
        os.system("cls")
        for i in range(1, 6):
            print(f"[{i}] Show bot {i} data" if self.log_pass_data[i][0] != "" else f"[{i}] Press {i} to add bot")
        print("[6] Main menu")
        bas_item = int(input("Select menu item: "))
        if bas_item < 1 or bas_item > 6:
            while True:
                bas_item = int(input("Select menu item: "))
                if bas_item >= 1 and bas_item <= 5:
                    break
                else:
                    continue
        elif bas_item >= 1 and bas_item <= 5:
            self.show_bot_info(bas_item)
        elif bas_item == 6:
            self.main_menu()


    def ui_help(self):
        colors = {1: "c",
                  2: "e",
                  3: "a",
                  4: "b",
                  5: "9",
                  6: "d",
                  7: "f0",
                  8: "0f"}

        os.system("cls")
        print("Sorry, but i'm don't write help text. :(")
        print("UI Colors (fun settings without saving)")
        print(f"""[1] Red
[2] Yellow
[3] Green (tru haker look)
[4] Cian
[5] Blue
[6] Purple
[7] Light theme (bye bye eyes)
[8] Dark theme (for normal peoples)
[9] Main menu""")
        uih_item = int(input("Select menu item: "))
        if uih_item < 1 or uih_item > 9:
            while True:
                uih_item = int(input("Select menu item: "))
                if uih_item >= 0 and uih_item <= 9:
                    break
                else:
                    continue
        elif uih_item >= 1 and uih_item <= 8:
            os.system(f"color {colors[uih_item]}")
        elif uih_item == 9:
            self.main_menu()
        self.main_menu()

    def main_account_change(self):
        os.system("cls")
        self.log_pass_data[0][0] = input("Input main account login: ")
        self.log_pass_data[0][1] = input("Input main account password: ")
        self.log_pass_data[0][2] = input("Input main account id: ")
        while True:
            save = input("Do you want to save account data in .txt file? [Y/n] ")
            if save == "Y":
                self.accs_saving()
                break
            elif save == "n":
                break
            else:
                continue
        self.main_acc_settings()

    def bot_acc_change(self, n):
        os.system("cls")
        self.log_pass_data[n][0] = input("Input main account login: ")
        self.log_pass_data[n][1] = input("Input main account password: ")
        while True:
            save = input("Do you want to save account data in .txt file? [Y/n] ")
            if save == "Y":
                self.accs_saving()
                break
            elif save == "n":
                break
            else:
                continue
        self.bots_acc_settings()

    def show_bot_info(self, n):
        os.system("cls")
        print(f"Bot {n} data\nLogin: {self.log_pass_data[n][0]}\nPassword: {self.log_pass_data[n][1]}")
        print("[1] Change bot data")
        print("[2] Main menu")
        sbi_item = int(input("Select menu item: "))
        if sbi_item != 1 and sbi_item != 2:
            while True:
                sbi_item = int(input("Select menu item: "))
                if sbi_item == 1 or sbi_item == 2:
                    break
                else:
                    continue
        elif sbi_item == 1:
            self.bot_acc_change(n)
        elif sbi_item == 2:
            self.main_menu()
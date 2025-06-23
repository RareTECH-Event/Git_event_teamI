def main():
    while True:
        print("選択してください：")
        print("1: Masa")
        print("2: えーちゃん")
        print("3: ろく")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("みんなで頑張りましょう！")
        elif choice == "2":
            print("頑張ります！！")
        elif choice == "3":
            print("お疲れ様です")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()


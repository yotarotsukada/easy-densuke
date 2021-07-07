## for test: nabeatsu game
try:
    num = int(input("1000以下の数字を半角で入力してください"))
    if num % 3 == 0:
        print("ナベアツ！")
    elif "3" in str(num):
        print("ナベアツ！")
    else:
        print("(-_-)")
except ValueError:
    print("数値で入力してください")

# パスワードの設定
correct_password = "your_password_here"

# ユーザーからの入力を受け取る
input_password = input("パスワードを入力してください: ")

if input_password == correct_password:
    print("認証成功！次のファイルを実行します。")
    # 例えば "next_script.py" を実行
    import subprocess
    subprocess.run(["python", "next_script.py"])
else:
    print("間違い")

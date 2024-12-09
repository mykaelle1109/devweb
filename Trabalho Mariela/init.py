from flask import Flask, render_template, request, redirect, url_for, flash

app_Mykaelle = Flask(__name__)
app_Mykaelle.secret_key = "secretkey"  

USUARIO_VALIDO = {
    "email": "mykaelle@exemplo.com",
    "senha": "123456"
}

@app_Mykaelle.route("/")
def login():
    return render_template("login.html")

@app_Mykaelle.route("/login", methods=["POST"])
def autenticar():
    email = request.form.get("email")
    senha = request.form.get("password")

    if email == USUARIO_VALIDO["email"] and senha == USUARIO_VALIDO["senha"]:
        flash("Login realizado com sucesso!", "success")
        return redirect(url_for("sobre"))
    else:
        flash("Credenciais inválidas. Tente novamente.", "danger")
        return redirect(url_for("login"))

@app_Mykaelle.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app_Mykaelle.route("/contato")
def contato():
    return render_template("contato.html")

@app_Mykaelle.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            flash("As senhas não coincidem. Tente novamente!", "error")
            return redirect(url_for("cadastro"))

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for("login"))

    return render_template("cadastro.html")

if __name__ == "__main__":
    app_Mykaelle.run(debug=True)

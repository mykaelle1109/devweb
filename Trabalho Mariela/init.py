from flask import Flask, render_template, request, redirect, url_for, flash
app_Mykaelle = Flask (__name__)

app_Mykaelle.secret_key = "secretkey"  # Necessário para mensagens flash

@app_Mykaelle.route("/")
def login():
    return render_template("login.html")

@app_Mykaelle.route("/contato")
def contato():
    return render_template("contato.html")

@app_Mykaelle.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app_Mykaelle.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        name = request.form["name"]
        cpf = request.form["cpf"]
        email = request.form["email"]
        phone = request.form["phone"]
        address = request.form["address"]
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

from flask import Flask, request

app = Flask(__name__)

ADMIN_USER = "admin"
ADMIN_PASSWORD = "admin123"
FLAG = "FLAG{senha_fraca_e_porta_aberta}"

FORMULARIO = """
<h1>Area Restrita</h1>
<form method="post">
  <input name="usuario" placeholder="usuario">
  <input name="senha" type="password" placeholder="senha">
  <button type="submit">Entrar</button>
</form>
"""


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if usuario == ADMIN_USER and senha == ADMIN_PASSWORD:
            return f"<h1>Bem-vindo, admin!</h1><p>{FLAG}</p>"
        return FORMULARIO + "<p>Usuario ou senha incorretos.</p>"
    return FORMULARIO


if __name__ == "__main__":
    app.run()
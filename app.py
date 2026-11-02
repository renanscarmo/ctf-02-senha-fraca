import os

from flask import Flask, request
from werkzeug.security import check_password_hash

app = Flask(__name__)

ADMIN_USER = "admin"
SENHA_HASH = os.environ.get("ADMIN_SENHA_HASH", "")
FLAG = "FLAG{senha_forte_e_porta_fechada}"

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
        usuario = request.form.get("usuario", "")
        senha = request.form.get("senha", "")
        if usuario == ADMIN_USER and check_password_hash(SENHA_HASH, senha):
            return f"<h1>Bem-vindo, admin!</h1><p>{FLAG}</p>"
        return FORMULARIO + "<p>Usuario ou senha incorretos.</p>"
    return FORMULARIO


if __name__ == "__main__":
    app.run()
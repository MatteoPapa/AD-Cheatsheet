# 🛠️ Generatore di Cheatsheet per CTF

Genera un cheatsheet HTML elegante e interattivo con i comandi più utili per il tuo team durante i CTF o operazioni di red teaming.

---

## 📦 File Inclusi

- `commands.yaml` – Elenco delle sezioni e dei comandi, con descrizione e supporto a variabili tramite Jinja2.
- `config.yaml` – Variabili (es. indirizzi IP) da sostituire nei comandi.
- `cheatsheet.j2` – Template HTML Jinja2 per la generazione del cheatsheet.
- `render.py` – Script Python per creare `cheatsheet.html` a partire dai template e dai file YAML.
- `style.css` – Tema scuro personalizzato per il cheatsheet.
- `cheatsheet.html` – Output finale generato (non modificare manualmente).

---

## 🧰 Requisiti

Installa le dipendenze Python con:

```bash
pip install -r requirements.txt
```

Oppure manualmente:

```bash
pip install PyYAML Jinja2
```

---

## 🚀 Utilizzo

1. Modifica IP e variabili in `config.yaml`.
2. Aggiungi o modifica i comandi in `commands.yaml` (organizzati per sezione).
3. Esegui lo script:

```bash
cd cheatsheet
python render.py
```

4. Apri `cheatsheet.html` nel browser.
5. Clicca su qualsiasi comando per copiarlo automaticamente negli appunti!

---

## 💡 Funzionalità

- 🧠 Sintassi semplice in YAML per scrivere i comandi
- 🪄 Variabili dinamiche riempite automaticamente dal file di configurazione
- 🖱️ Interfaccia con click-to-copy per rapidità durante i CTF
- 🎨 Design scuro elegante (Bootstrap + CSS personalizzato)

---

## 🛡️ Licenza

MIT — sentiti libero di usare, modificare e condividere con il tuo team CTF.

Buon pwn e che vinca il miglior team! 🎯🚩💻

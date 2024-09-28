
# API pro české svátky

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

Tento API server umožňuje získávání dat o českých svátcích na základě nejrůznějších údajů (jméno, datum, den v roce...)

Pro vyzkoušení můžete použít [demo](https://svatky.dcerny.cz/apidocs). Pro aktivní používání spusťte vlastní server, nebo jen použijte databázi z tohoto projektu.
## Možnosti hledání svátků

- Všechny svátky v roce
- Podle zadaného jména
- Podle zadaného data
- Den v roce (číselně 1-366)
- Týden v roce (1-53)
- Měsíc v roce (1-12)


## Demo a dokumentace

- [Dokumentace](https://svatky.dcerny.cz/apidocs)

- [Live server](https://svatky.dcerny.cz/all)

## Příklady použití

Vyzkoušej některý z příkladů:

- [Všechny svátky v roce](https://svatky.dcerny.cz/all)
- [Hledání podle jména "david"](https://svatky.dcerny.cz/name/david)
- [Hledání podle data 26. 7.](https://svatky.dcerny.cz/date/26.7.)
- [Hledání měsíce září](https://svatky.dcerny.cz/month/9)

Všechny možnosti použití najdete v dokumentaci.

## Instalace

Pokud nemáte, nainstalujte python3, pip a venv

Naklonujte repozitář

```bash
git clone git@github.com:david-bl/api-svatky.git
cd api-svatky
```

Vytvořte a aktivujte virtuální prostředí

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Nainstalujte balíčky z requirements.txt

```bash
pip install -r .\requirements.txt
```

Inicializace databáze

```bash
flask init-db
```

Nyní můžete spustit testy a samotnou aplikaci

```bash
coverage run -m pytest
flask run --debug
```

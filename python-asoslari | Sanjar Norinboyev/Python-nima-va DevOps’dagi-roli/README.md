# 1-mavzu: Python nima va DevOps'dagi roli

# Virtual muhit

Virtual muhit yaratish va faollashtirish:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

`requests` kutubxonasi o'rnatildi va `requirements.txt` fayli `pip freeze` orqali yaratildi:

```bash
python -m pip install requests
python -m pip freeze > requirements.txt
```

# Python versiyasi va joylashuvi

Tekshiruv buyruqlari:

```text
python3 --version
Python 3.13.0

which python3
/home/sanjar/.pyenv/shims/python3
```

## argparse bilan salomlashish

```bash
python "1. Amaliy vazifa.py" --name Sanjar
```

Skript `--name` parametrini qabul qilib, salomlashuv xabarini chiqaradi.

## Fayllar sonini sanash

Python varianti:

```bash
python "1. Amaliy vazifa.py" --name Sanjar --directory .
```

Bash varianti:

```bash
bash fayllar_soni.sh .
```

### Xulosa

Bash varianti qisqa va terminaldagi oddiy fayl operatsiyalari uchun qulay. Python varianti esa `pathlib` va `argparse` yordamida platformalararo ishlaydi, parametrlarni kengaytirish va natijani keyingi dasturda qayta ishlash oson. Shu sababli DevOps avtomatlashtirishida oddiy buyruqlar uchun Bash, murakkabroq mantiq va kengayadigan vositalar uchun Python tanlanadi.
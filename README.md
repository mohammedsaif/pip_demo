# Python pip Demo

A small demo showing how to use `pip` to inspect and manage Python packages, using a script ([fetch-user.py](fetch-user.py)) that depends on the `requests` library.

## The demo script

```python
import requests

url = "https://jsonplaceholder.typicode.com/users/4"
response = requests.get(url, timeout=10)

print("Status:", response.status_code)
user = response.json()
print("Name:", user["name"])
print("Email:", user["email"])
print("City:", user["address"]["city"])
```

Install the dependency and run it:

```bash
pip install requests
python fetch-user.py
```

---

## 1. `pip --version`

Shows the installed pip version, where it is installed, and which Python it belongs to.

```bash
pip --version
```

Output:

```
pip 25.0.1 from C:\Users\Dell\AppData\Local\Programs\Python\Python312\Lib\site-packages\pip (python 3.12)
```

| Part | Meaning |
|------|---------|
| `pip 25.0.1` | pip version |
| `from ...\site-packages\pip` | install location of pip |
| `(python 3.12)` | Python version pip is tied to |

Tip: `python -m pip --version` guarantees you are using the pip that matches the `python` you run.

---

## 2. `pip show <package>`

Shows detailed metadata about one installed package.

### Example: `pip show requests`

This is the library used by `fetch-user.py`.

```bash
pip show requests
```

Output:

```
Name: requests
Version: 2.34.2
Summary: Python HTTP for Humans.
Home-page:
Author:
Author-email: Kenneth Reitz <me@kennethreitz.org>
License: Apache-2.0
Location: C:\Users\Dell\AppData\Local\Programs\Python\Python312\Lib\site-packages
Requires: certifi, charset_normalizer, idna, urllib3
Required-by: google-genai
```

### Example: `pip show pip`

```bash
pip show pip
```

Output:

```
Name: pip
Version: 25.0.1
Summary: The PyPA recommended tool for installing Python packages.
Home-page: https://pip.pypa.io/
Author:
Author-email: The pip developers <distutils-sig@python.org>
License: MIT
Location: C:\Users\Dell\AppData\Local\Programs\Python\Python312\Lib\site-packages
Requires:
Required-by:
```

### Field reference

| Field | Meaning |
|-------|---------|
| `Name` | Package name |
| `Version` | Installed version |
| `Summary` | One-line description |
| `Home-page` | Project website (may be empty) |
| `Author` / `Author-email` | Package author |
| `License` | License the package uses |
| `Location` | Folder where the package is installed |
| `Requires` | Packages this package depends on |
| `Required-by` | Installed packages that depend on this one |

Add `-f` / `--files` to also list every file the package installed: `pip show -f requests`.

---

## 3. `pip list`

Lists all installed packages with their versions in a readable table.

```bash
pip list
```

Output (this machine, 130 packages):

```
Package                   Version
------------------------- -----------
annotated-doc             0.0.4
annotated-types           0.7.0
anyio                     4.14.1
asttokens                 3.0.2
attrs                     26.1.0
beautifulsoup4            4.15.0
certifi                   2026.6.17
cffi                      2.0.0
charset-normalizer        3.4.7
click                     8.4.2
colorama                  0.4.6
coloredlogs               15.0.1
comm                      0.2.3
comtypes                  1.4.16
cryptography              49.0.0
debugpy                   1.8.21
decorator                 5.3.1
defusedxml                0.7.1
distro                    1.9.0
dnspython                 2.8.0
dotenv                    0.9.9
email-validator           2.3.0
et_xmlfile                2.0.0
euron-coding-agent        1.4.0
executing                 2.2.1
faiss-cpu                 1.15.0
fastapi                   0.139.2
fastjsonschema            2.22.1
flatbuffers               25.12.19
google-auth               2.55.1
google-genai              2.10.0
greenlet                  3.5.5
grpcio                    1.83.1
h11                       0.16.0
h2                        4.4.1
hpack                     4.2.0
httpcore                  1.0.9
httptools                 0.8.0
httpx                     0.28.1
humanfriendly             10.0
hyperframe                6.1.0
idna                      3.18
iniconfig                 2.3.0
ipykernel                 7.3.0
ipython                   9.15.0
ipython_pygments_lexers   1.1.1
jedi                      0.20.0
jiter                     0.16.0
jsonschema                4.26.0
jsonschema-specifications 2025.9.1
jupyter_client            8.9.1
jupyter_core              5.9.1
lxml                      6.1.1
markdown-it-py            4.2.0
matplotlib-inline         0.2.2
mdurl                     0.1.2
mpmath                    1.3.0
narwhals                  2.25.0
nbclient                  0.11.0
nbformat                  5.10.4
neo4j                     6.3.1
nest-asyncio2             1.7.2
numpy                     2.5.0
onnxruntime               1.27.0
openai                    2.46.0
openpyxl                  3.1.5
packaging                 26.2
pandas                    3.0.5
parso                     0.8.7
pathvalidate              3.3.1
pdfminer.six              20260107
pdfplumber                0.11.10
pikepdf                   10.12.0
pillow                    12.2.0
pip                       25.0.1
piper-tts                 1.4.2
platformdirs              4.10.0
plotly                    7.0.0
pluggy                    1.6.0
portalocker               3.2.0
prompt_toolkit            3.0.52
protobuf                  7.35.1
psutil                    7.2.2
psycopg2-binary           2.9.12
pure_eval                 0.2.3
pyasn1                    0.6.3
pyasn1_modules            0.4.2
pycparser                 3.0
pydantic                  2.13.4
pydantic_core             2.46.4
Pygments                  2.20.0
pymongo                   4.18.1
pymupdf                   1.28.0
pypdf                     6.16.2
pypdfium2                 5.12.1
pypiwin32                 223
pyreadline3               3.5.6
pytest                    9.1.1
python-dateutil           2.9.0.post0
python-dotenv             1.2.2
pyttsx3                   2.99
pytz                      2026.4
pywin32                   312
PyYAML                    6.0.3
pyzmq                     27.1.0
qdrant-client             1.19.0
referencing               0.37.0
requests                  2.34.2
rich                      15.0.0
rpds-py                   2026.6.3
six                       1.17.0
sniffio                   1.3.1
soupsieve                 2.8.4
SQLAlchemy                2.0.52
stack-data                0.6.3
starlette                 1.3.1
sympy                     1.14.0
tenacity                  9.1.4
tornado                   6.5.7
tqdm                      4.69.0
traitlets                 5.15.1
typing_extensions         4.15.0
typing-inspection         0.4.2
tzdata                    2026.3
urllib3                   2.7.0
uvicorn                   0.51.0
watchfiles                1.2.0
wcwidth                   0.8.2
websockets                16.0
```

Useful variants:

| Command | Purpose |
|---------|---------|
| `pip list --outdated` | Only packages with newer versions available |
| `pip list --format=freeze` | Same as `pip freeze` style output |
| `pip list --format=json` | Machine-readable output |

---

## 4. `pip freeze`

Prints installed packages in `package==version` format, the format expected by a `requirements.txt` file.

```bash
pip freeze
```

Output (this machine):

```
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.14.1
asttokens==3.0.2
attrs==26.1.0
beautifulsoup4==4.15.0
certifi==2026.6.17
cffi==2.0.0
charset-normalizer==3.4.7
click==8.4.2
colorama==0.4.6
coloredlogs==15.0.1
comm==0.2.3
comtypes==1.4.16
cryptography==49.0.0
debugpy==1.8.21
decorator==5.3.1
defusedxml==0.7.1
distro==1.9.0
dnspython==2.8.0
dotenv==0.9.9
email-validator==2.3.0
et_xmlfile==2.0.0
euron-coding-agent==1.4.0
executing==2.2.1
faiss-cpu==1.15.0
fastapi==0.139.2
fastjsonschema==2.22.1
flatbuffers==25.12.19
google-auth==2.55.1
google-genai==2.10.0
greenlet==3.5.5
grpcio==1.83.1
h11==0.16.0
h2==4.4.1
hpack==4.2.0
httpcore==1.0.9
httptools==0.8.0
httpx==0.28.1
humanfriendly==10.0
hyperframe==6.1.0
idna==3.18
iniconfig==2.3.0
ipykernel==7.3.0
ipython==9.15.0
ipython_pygments_lexers==1.1.1
jedi==0.20.0
jiter==0.16.0
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
jupyter_client==8.9.1
jupyter_core==5.9.1
lxml==6.1.1
markdown-it-py==4.2.0
matplotlib-inline==0.2.2
mdurl==0.1.2
mpmath==1.3.0
narwhals==2.25.0
nbclient==0.11.0
nbformat==5.10.4
neo4j==6.3.1
nest-asyncio2==1.7.2
numpy==2.5.0
onnxruntime==1.27.0
openai==2.46.0
openpyxl==3.1.5
packaging==26.2
pandas==3.0.5
parso==0.8.7
pathvalidate==3.3.1
pdfminer.six==20260107
pdfplumber==0.11.10
pikepdf==10.12.0
pillow==12.2.0
piper-tts==1.4.2
platformdirs==4.10.0
plotly==7.0.0
pluggy==1.6.0
portalocker==3.2.0
prompt_toolkit==3.0.52
protobuf==7.35.1
psutil==7.2.2
psycopg2-binary==2.9.12
pure_eval==0.2.3
pyasn1==0.6.3
pyasn1_modules==0.4.2
pycparser==3.0
pydantic==2.13.4
pydantic_core==2.46.4
Pygments==2.20.0
pymongo==4.18.1
pymupdf==1.28.0
pypdf==6.16.2
pypdfium2==5.12.1
pypiwin32==223
pyreadline3==3.5.6
pytest==9.1.1
python-dateutil==2.9.0.post0
python-dotenv==1.2.2
pyttsx3==2.99
pytz==2026.4
pywin32==312
PyYAML==6.0.3
pyzmq==27.1.0
qdrant-client==1.19.0
referencing==0.37.0
requests==2.34.2
rich==15.0.0
rpds-py==2026.6.3
six==1.17.0
sniffio==1.3.1
soupsieve==2.8.4
SQLAlchemy==2.0.52
stack-data==0.6.3
starlette==1.3.1
sympy==1.14.0
tenacity==9.1.4
tornado==6.5.7
tqdm==4.69.0
traitlets==5.15.1
typing-inspection==0.4.2
typing_extensions==4.15.0
tzdata==2026.3
urllib3==2.7.0
uvicorn==0.51.0
watchfiles==1.2.0
wcwidth==0.8.2
websockets==16.0
```

Save it to a file and reinstall elsewhere:

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

---

## `pip list` vs `pip freeze`

| | `pip list` | `pip freeze` |
|---|-----------|--------------|
| Format | Human-readable table | `name==version` lines |
| Header | Yes | No |
| Includes `pip` itself | Yes | No (pip, setuptools, wheel, distribute are skipped by default) |
| Best for | Quick look at what is installed | Creating `requirements.txt` |

## Quick command summary

| Command | What it does |
|---------|--------------|
| `pip --version` | Show pip version and location |
| `pip show <package>` | Show details of one package |
| `pip list` | List all installed packages (table) |
| `pip freeze` | List packages as `name==version` for `requirements.txt` |

> Note: the package lists above are from the global Python 3.12 install on this machine, not an isolated environment. For a project-specific `requirements.txt`, create a virtual environment first (`python -m venv .venv`) so `pip freeze` only contains what the project needs.

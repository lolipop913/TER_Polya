# Urnes de Pólya généralisées — Étude expérimentale de la domination permanente

Projet de TER de Master de Mathématiques (Aix-Marseille Université) consacré à l’étude probabiliste et computationnelle des urnes de Pólya généralisées.

Le projet combine :
- simulations stochastiques,
- méthodes de Monte Carlo,
- mécanismes de renforcement,
- étude empirique de comportements asymptotiques.

---

## Contexte mathématique

Les urnes de Pólya sont des modèles classiques de processus stochastiques à renforcement.

À chaque étape :
1. une boule est tirée aléatoirement ;
2. elle est replacée dans l’urne ;
3. des boules supplémentaires sont ajoutées selon la couleur obtenue.

Le système possède ainsi un effet de mémoire :
les couleurs fréquemment tirées deviennent progressivement plus probables.

Le projet s’intéresse ici à des régimes de renforcement asymétriques.

---

## Question étudiée

On étudie l’événement :

\[
A = \{B_n > W_n,\ \forall n \geq 0\}
\]

où :
- \(B_n\) désigne le nombre de boules noires après \(n\) étapes ;
- \(W_n\) désigne le nombre de boules blanches après \(n\) étapes.

Cet événement correspond à une **domination permanente** des boules noires.

L’objectif est d’étudier :
- l’influence des conditions initiales ;
- l’effet des paramètres de renforcement ;
- la stabilité des trajectoires dominantes ;
- les probabilités empiriques de domination.

---

## Structure du projet

```text
TER_Polya/
│
├── articles/
├── notebooks/
│   ├── 01_basic_simulations.ipynb
│   ├── 02_permanent_domination.ipynb
│   └── 03_parameter_sensitivity.ipynb
│
├── src/
│   └── urn.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Notebooks

### 01 — Simulations fondamentales

- dynamique des urnes ;
- renforcement symétrique et asymétrique ;
- évolution des proportions ;
- premières trajectoires stochastiques.

### 02 — Domination permanente

- étude de l’événement \(A\) ;
- simulations de Monte Carlo ;
- estimation empirique de probabilités ;
- rôle des fluctuations initiales.

### 03 — Sensibilité des paramètres

- influence des conditions initiales ;
- asymétrie du renforcement ;
- stabilité probabiliste des trajectoires ;
- comparaison expérimentale des régimes.

Installation
git clone https://github.com/lolipop913/TER_Polya.git
cd TER_Polya

python -m venv .venv
Activation de l’environnement
Windows
.venv\Scripts\activate
Linux / macOS
source .venv/bin/activate
Installation des dépendances
pip install -r requirements.txt
Auteur

Henri Vasserot
Master de Mathématiques — Aix-Marseille Université
TER — Processus stochastiques et urnes de Pólya
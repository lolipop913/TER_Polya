# Urnes de Pólya généralisées — Étude expérimentale de la domination permanente

Projet de TER de Master de Mathématiques (Aix-Marseille Université) consacré à l’étude probabiliste et computationnelle des urnes de Pólya généralisées.

Le projet combine :
- simulations stochastiques ;
- méthodes de Monte Carlo ;
- processus de renforcement ;
- processus de branchement ;
- étude asymptotique de trajectoires dominantes ;
- validation empirique de résultats probabilistes.

---

## Objectif du projet

Le projet s’appuie principalement sur l’article récent de Svante Janson :

> *A Note on Pólya Urns: The Winner May Lead All the Time* (2025)

ainsi que sur les travaux fondateurs :
- G. Pólya (1930) ;
- Athreya & Ney — *Branching Processes* (1972).

L’objectif du TER est d’étudier théoriquement et expérimentalement le phénomène suivant :

$$
\mathbb{P}(B_n > W_n,\ \forall n \geq 0) > 0
$$

dans des urnes de Pólya asymétriques.

Autrement dit :

> une couleur initialement dominante peut conserver son avance à tout instant avec probabilité strictement positive.

---

## Contexte mathématique

Les urnes de Pólya sont des modèles classiques de processus stochastiques à renforcement.

À chaque étape :
1. une boule est tirée aléatoirement ;
2. elle est replacée dans l’urne ;
3. des boules supplémentaires sont ajoutées selon la couleur obtenue.

Le système possède ainsi un effet de mémoire : les couleurs fréquemment tirées deviennent progressivement plus probables.

Le projet s’intéresse ici à des régimes de renforcement asymétriques.

Dans le cas :

$$
m_b > m_w
$$

les boules noires deviennent asymptotiquement dominantes.

Cependant, le TER étudie une question plus forte :

> le leader initial peut-il rester dominant pour tout temps ?

---

## Question étudiée

On étudie l’événement :

$$
A = \{B_n > W_n,\ \forall n \geq 0\}
$$

où :
- B_n désigne le nombre de boules noires après `n` étapes ;
- W_n désigne le nombre de boules blanches après `n` étapes.

Cet événement correspond à une **domination permanente** des boules noires.

L’objectif est d’étudier :
- l’influence des conditions initiales ;
- l’effet des paramètres de renforcement ;
- la stabilité des trajectoires dominantes ;
- les probabilités empiriques de domination ;
- les temps de domination asymptotique.

---

## Structure du projet

```text
TER_Polya/
│
├── articles/
│   ├── paper/
│   └── references/
│
├── notebooks/
│   ├── 01_basic_simulations.ipynb
│   ├── 02_permanent_domination.ipynb
│   ├── 03_parameter_sensitivity.ipynb
│   ├── 04_extension_time_to_domination.ipynb
│   └── 05_statistical_validation.ipynb
│
├── presentation/
│   └── slides/
│
├── src/
│   └── urn.py
│
├── figures/
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
- premières trajectoires stochastiques ;
- domination asymptotique empirique.

### 02 — Domination permanente

- étude de l’événement `A` ;
- simulations de Monte Carlo ;
- estimation empirique de probabilités ;
- rôle des fluctuations initiales ;
- validation empirique du théorème de Janson.

### 03 — Sensibilité des paramètres

- influence des conditions initiales ;
- asymétrie du renforcement ;
- stabilité probabiliste des trajectoires ;
- comparaison expérimentale des régimes ;
- étude des transitions de domination.

### 04 — Temps de domination asymptotique

- étude des temps de stabilisation ;
- comportement transitoire ;
- domination asymptotique ;
- distribution des temps de convergence ;
- analyse des trajectoires persistantes.

### 05 — Validation statistique

- robustesse des simulations ;
- estimation statistique ;
- intervalles de confiance ;
- cohérence théorie / expérience ;
- validation empirique des comportements asymptotiques.

---

## Implémentation Python

Le cœur du projet est implémenté dans :

```text
src/urn.py
```

La classe principale est :

```text
PolyaUrn
```

Elle permet :
- la simulation des urnes ;
- le suivi des trajectoires ;
- la détection de domination permanente ;
- l’analyse des temps de stabilisation.

---

## Références principales

- Svante Janson, *A Note on Pólya Urns: The Winner May Lead All the Time*, arXiv, 2025.
- G. Pólya, *Sur quelques points de la théorie des probabilités*, Annales de l’Institut Henri Poincaré, 1930.
- K. B. Athreya & P. E. Ney, *Branching Processes*, Springer, 1972.

---

## Perspectives

Le projet se poursuit désormais par :

### Rédaction de l’article scientifique

- formalisation mathématique ;
- présentation théorique ;
- intégration des résultats expérimentaux ;
- discussion probabiliste.

### Construction de la soutenance

- création des diapositives ;
- synthèse visuelle des résultats ;
- articulation théorie / simulations ;
- présentation des résultats principaux.

---

## Installation

### Clonage du dépôt

```bash
git clone https://github.com/lolipop913/TER_Polya.git
cd TER_Polya
```

### Création de l’environnement virtuel

```bash
python -m venv .venv
```

### Activation de l’environnement

Windows :

```bash
.venv\Scripts\activate
```

Linux / macOS :

```bash
source .venv/bin/activate
```

### Installation des dépendances

```bash
pip install -r requirements.txt
```

---

## Auteur

Henri Vasserot  
Master de Mathématiques — Aix-Marseille Université  

TER — Processus stochastiques et urnes de Pólya
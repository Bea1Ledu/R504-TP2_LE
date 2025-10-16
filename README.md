# TP R504-TP2 :

**IMPORTANT** : Pour exécuter les modules, restez TOUJOURS dans la racine du projet ('R504-TP2_LE') et utilisez 'python -m src.nom_du_fichier'. Ne jamais lancer depuis le dossier 'src/' !

Voici des commandes à exécuter pour chaque fichiers sur le terminal powershell:

## Exécution des Modules (exemples)

### Question 1 : FizzBuzz

#### Q1.A - Création d’une première solution
python -c "from src.fizzbuzz import affiche; affiche()"

#### Q1.B - Première évolution du code
python -c "from src.fizzbuzz_v2 import affiche; print(affiche(15))"

#### Q1.C - Deuxième évolution du code
python -c "from src.fizzbuzz_v3 import affiche; print(affiche(5, 10))"
python -c "from src.fizzbuzz_v3 import affiche; print(affiche(10, 16))"


### Question 2 : Cryptage

#### Q2.A - Création de la première solution
python -c "from src.crypto import crypt; print(crypt('abc'))"

#### Q2.B - Première évolution du code
python -c "from src.crypto_v2 import crypt; print(crypt('abc', 3))"

#### Q2.C - Deuxième évolution du code : Décryptage
python -c "from src.crypto_v3 import decrypt; print(decrypt('def3'))"


## Explication du TP ## 

Les fichiers du dossier src/ contiennent les versions finales fonctionnelles de chaque exercice, tandis que les fichiers du dossier tests/ regroupent les tests unitaires utilisés pendant le TDD et certains peuvent échouer selon l’étape de développement.

## Introduction

Ce projet a été réalisé dans le cadre du module R504 
L'objectif principal est la mise en pratique de la méthodologie de Développement Dirigé par les Tests (TDD) pour la résolution de deux problèmes distincts en Python.

Le versionnement du code est fait sur git avec plusieurs commit.

## Prérequis

* Python 3.x
* Git

## Installation

1.  Clonez le dépôt sur votre machine locale :

    git clone <URL_DU_DEPOT>
    cd <NOM_DU_DOSSIER>


2.  Il est recommandé de créer et d'activer un environnement virtuel :

    python -m venv .venv
    # Sur Windows (PowerShell)
    .\.venv\Scripts\Activate.ps1
    # Sur macOS/Linux
    source .venv/bin/activate

3.  Installez les dépendances nécessaires :
    pip install -r requirements.txt
    

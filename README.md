# Implémentation de la trie

- Créer la logique de base en définissant la fontion ```add()``` pour ajouter un mot
- Ajouter une valeur booléenne pour marquer la dernière lettre de la clé (chaîne représentant les mots intégrés à la trie)
- Chaque  nœud ou feuille doit contenir la lettre courante et la valeur citée: 
  - True si c'est un mot
  - False si c'est un prédicat
- Créer la fonction ```contains()``` pour vérifier la présence d'une clé dans la trie
- Dev l'affichage complet

## Mots à ajouter :

```words = ["à", "arbre", "artiste", "chape", "chapeau", "créatif", "œuf", "zèbre"]```

## Résultat
```
|
|--a
|  |__r
|     |--b
|     |  |__r
|     |     |__e *[arbre]
|     |
|     |__t *[art]
|        |__i
|           |__s
|              |__t
|                 |__e *[artiste]
|
|--à *[à]
|
|--c
|  |--h
|  |  |__a
|  |     |__p
|  |        |__e *[chape]
|  |           |__a
|  |              |__u *[chapeau]
|  |
|  |__r
|     |__é
|        |__a
|           |__t
|              |__i
|                 |--f *[créatif]
|                 |__o
|                    |__n *[création]
|
|--œ
|  |__u
|     |__f *[œuf]
|
|__z
   |__è
      |__b
         |__r
            |__e *[zèbre]
```
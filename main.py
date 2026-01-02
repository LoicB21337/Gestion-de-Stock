"""Programme principal pour tester le gestionnaire de stock.

Le stock initial ci-dessous contient plusieurs produits de test.
"""

from gestionDeStock import *

magasin = GestionDeStock(
    "A1, A1, A1, A1, A1, A1, A2, A2, A2, A2,"
    " B1, B1, B1, B1, B1, B2, B2, B2, B2,"
    " C1, C1, C1, C1, C1, C1, C2, C2, C2, C2, C2,"
    " C3, C3, C3, C3, D1, D1, D1, E1, E1, E1, E2, E2, E2, E2"
)
magasin.afficherStock()
magasin.commander()
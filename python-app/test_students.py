import pytest
import psycopg2
from students import add_student, get_student, average_grade

@pytest.fixture
def conn():
    """Prépare une connexion propre à la base de données et vide la table avant chaque test."""
    # Connexion à la base 'tp' sur localhost configurée par db/setup.sh
    connection = psycopg2.connect(
        host="localhost",
        database="tp",
        user="postgres",
        password="postgres"
    )
    # Nettoyage de sécurité : on repart d'une table vide
    with connection.cursor() as cur:
        cur.execute("TRUNCATE TABLE students RESTART IDENTITY;")
    connection.commit()
    
    yield connection
    connection.close()

def test_ajouter_et_lire(conn):
    # 1. Ajouter un étudiant, puis le relire : on retrouve son nom et sa note
    add_student(conn, "Samy", 16.5)
    student = get_student(conn, "Samy")
    assert student is not None
    assert student[1] == "Samy"
    assert float(student[2]) == 16.5

def test_lire_inexistant(conn):
    # 2. Lire un étudiant qui n'existe pas : on obtient « rien » (None)
    student = get_student(conn, "Inconnu")
    assert student is None

def test_moyenne(conn):
    # 3. Ajouter deux étudiants (notes 10 and 14) : la moyenne vaut 12
    add_student(conn, "Amel", 10)
    add_student(conn, "Karim", 14)
    assert average_grade(conn) == 12.0


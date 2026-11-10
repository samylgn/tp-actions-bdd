import psycopg2

def add_student(conn, name, grade):
    """Ajoute un étudiant dans la base de données."""
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (name, grade) VALUES (%s, %s);",
            (name, grade)
        )
    conn.commit()

def get_student(conn, name):
    """Lit un étudiant par son nom. Retourne un tuple (id, name, grade) ou None."""
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, grade FROM students WHERE name = %s;", (name,))
        return cur.fetchone()

def average_grade(conn):
    """Calcule la moyenne des notes."""
    with conn.cursor() as cur:
        # 1. Requête SQL pour récupérer la moyenne de la colonne grade
        cur.execute("SELECT AVG(grade) FROM students;")
        
        # 2. Récupère la première ligne du résultat
        row = cur.fetchone()
        
        # row contient un tuple, par exemple (12.0,). On extrait le premier élément row[0]
        # Si la table est vide, row[0] vaudra None, sinon on retourne la valeur convertie en float
        return float(row[0]) if row[0] is not None else 0.0

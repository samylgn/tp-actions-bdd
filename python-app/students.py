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
    """Calcule la moyenne des notes (À laisser non implémenté pour le moment !)."""
    # On lève volontairement l'erreur demandée par la consigne pour faire échouer le test
    raise NotImplementedError("La fonction average_grade n'est pas encore écrite")

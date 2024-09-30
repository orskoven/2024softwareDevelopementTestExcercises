import sqlite3

class GradesConverter:
    def __init__(self, db_path='grades.db'):
        """
        Constructor
        Connects to the database
        @param db_path: Path to the SQLite database file
        """
        self.conn = sqlite3.connect(db_path)

    def convert(self, grade, target_country):
        """
        Converts the grade to the target country's grading system.
        @param grade: The grade to convert
        @param target_country: The country to whose grading system the grade corresponds to ('danish' or 'american')
        @return: The converted grade
        """
        target_country = target_country.lower()
        if target_country not in ['danish', 'american']:
            raise ValueError("Invalid country. Must be 'danish' or 'american'.")
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT {target_country} FROM grade_conversion WHERE grade = ?", (grade,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            raise ValueError("Grade not found in database.")

    def close_connection(self):
        """
        Closes the database connection
        """
        if self.conn:
            self.conn.close()
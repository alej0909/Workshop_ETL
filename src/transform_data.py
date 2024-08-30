import pandas as pd

class DataTransformer:
    """
    Clase para transformar datos de un archivo CSV.
    """

    def __init__(self, filepath):
        """
        Inicializa la clase DataTransformer cargando un archivo CSV en un DataFrame.

        Args:
            filepath (str): Ruta del archivo CSV.
        """
        self.data = pd.read_csv(filepath, sep=';', encoding='utf-8')

    def standardize_column_names(self):
        """
        Estandariza los nombres de las columnas del DataFrame para que sean más consistentes.
        """
        self.data.rename(columns={
            'First Name': 'First_Name',
            'Last Name': 'Last_Name',
            'Application Date': 'Application_Date',
            'Code Challenge Score': 'Code_Challenge_Score',
            'Technical Interview Score': 'Technical_Interview_Score'
        }, inplace=True)

    def generate_ids(self):
        """
        Genera una columna de ID única para cada fila en el DataFrame.
        """
        self.data['ID'] = range(1, len(self.data) + 1)

    def calculate_hiring_status(self):
        """
        Calcula el estado de contratación del candidato en función de las puntuaciones.
        Agrega una columna 'Hired' que es 1 si el candidato fue contratado, 0 de lo contrario.
        """
        self.data['Hired'] = (
            (self.data['Code_Challenge_Score'] >= 7) &
            (self.data['Technical_Interview_Score'] >= 7)
        ).astype(int)

    def categorize_technology(self):
        """
        Asigna una categoría a cada fila del DataFrame basada en la tecnología.
        Las categorías están definidas por un diccionario.
        """
        tech_to_category = {
            'Development - CMS Backend': 'Web Development',
            'Development - CMS Frontend': 'Web Development',
            'Development - Backend': 'Web Development',
            'Adobe Experience Manager': 'Web Development',
            'Development - Frontend': 'Web Development',
            'Development - FullStack': 'Web Development',
            'Game Development': 'Software Development',
            'DevOps': 'Infrastructure',
            'Mulesoft': 'Integration Solutions',
            'Business Intelligence': 'Data Analysis',
            'Business Analytics / Project Management': 'Data Analysis',
            'Data Engineer': 'Data Engineering',
            'Database Administration': 'Database Management',
            'QA Manual': 'Quality Assurance',
            'QA Automation': 'Quality Assurance',
            'Security': 'Cybersecurity',
            'Security Compliance': 'Cybersecurity',
            'System Administration': 'Infrastructure',
            'Design': 'Creative & Design',
            'Client Success': 'Customer Support',
            'Social Media Community Management': 'Digital Marketing',
            'Technical Writing': 'Documentation',
            'Sales': 'Sales & Marketing',
            'Salesforce': 'Sales & Marketing'
        }

        self.data['Technology'] = self.data['Technology'].map(tech_to_category).fillna('Other')

    def save_transformed_data(self, output_path):
        """
        Guarda el DataFrame transformado en un nuevo archivo CSV.

        Args:
            output_path (str): Ruta donde se guardará el archivo CSV transformado.
        """
        self.data.to_csv(output_path, index=False, sep=';', encoding='utf-8')

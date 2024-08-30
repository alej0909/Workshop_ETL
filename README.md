# Workshop_ETL

Presented by:
- Manuel Alejandro Gruezo [manuel.gruezo@uao.edu.co](mailto:manuel.gruezo@uao.edu.co)

## 📝 Introduction

Exploratory Data Analysis (EDA) is a crucial step in any data science project, as it allows us to better understand the structure, relationships, and patterns within the data before conducting any advanced modeling or analysis.

In this project, we will work with a synthetic dataset focused on candidate applications, containing details such as names, countries, years of experience, technologies, seniority levels, and interview scores.

#### Data Description

The dataset contains various features, including:

- *Personal Information*: Candidate's name, email, country, and application date.
- *Experience & Skills*: Years of experience (YOE), seniority level, technology specialization.
- *Assessment Scores*: Code challenge and technical interview scores.
- *Hiring Status*: A binary indicator of whether the candidate was hired based on their scores.

| Feature                     | Variable Type         | Variable      | Value Type                               |
|-----------------------------|-----------------------|---------------|------------------------------------------|
| First Name                  | Personal Information  | first_name    | string                                   |
| Last Name                   | Personal Information  | last_name     | string                                   |
| Email                       | Personal Information  | email         | string                                   |
| Application Date            | Personal Information  | application_date | date                                    |
| Country                     | Personal Information  | country       | string                                   |
| Years of Experience (YOE)   | Experience & Skills   | yoe           | integer                                  |
| Seniority                   | Experience & Skills   | seniority     | string                                   |
| Technology                  | Experience & Skills   | technology    | string                                   |
| Code Challenge Score        | Assessment Scores     | code_challenge_score | integer                               |
| Technical Interview Score   | Assessment Scores     | technical_interview_score | integer                             |
| Hired                       | Hiring Status         | hired         | binary (0 = not hired, 1 = hired)        |

### 🎯 Objectives of the ETL

- **📊 Understanding Data Distribution**: Analyze the distribution of individual variables to identify outliers, missing values, and understand the nature of the data.
- **🔗 Exploring Relationships Between Variables**: Investigate possible correlations between different variables that might be useful for subsequent modeling.
- **🔍 Identifying Patterns and Trends**: Search for patterns and trends in the data that could reveal relevant information for the project’s objectives.
- **🛠️ Data Preparation**: Perform the necessary transformations to clean and prepare the data for analysis and modeling.

### Tools Used

- **Python** <img src="https://cdn-icons-png.flaticon.com/128/3098/3098090.png" alt="Python" width="21px" height="21px">
- **Jupyter Notebooks** <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png" alt="Jupyter" width="21px" height="21px">
- **PostgreSQL** <img src="https://cdn-icons-png.flaticon.com/128/5968/5968342.png" alt="Postgres" width="21px" height="21px">
- **SQLAlchemy** <img src="https://quintagroup.com/cms/python/images/sqlalchemy-logo.png/@@images/eca35254-a2db-47a8-850b-2678f7f8bc09.png" alt="SQLAlchemy" width="50px" height="21px">

### Repository Organization

- **data:** This folder contains the CSV files used in the project.
- **notebooks:** This folder contains the Jupyter notebooks used for data migration, exploratory data analysis, and data transformation.
- **src:** This folder contains the Python code responsible for connecting to the database and managing the data models.

### Requirements

1. Install Python: [Python Downloads](https://www.python.org/downloads/)
2. Install PostgreSQL: [PostgreSQL Downloads](https://www.postgresql.org/download/)

## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file (place the file in the root of the project):

- `PGDIALECT` - Specifies the PostgreSQL dialect for the connection.
- `PGUSER` - The username for authenticating against the PostgreSQL database.
- `PGPASSWD` - The password associated with the PostgreSQL user.
- `PGHOST` - The address of the PostgreSQL database server.
- `PGPORT` - The port on which the PostgreSQL server is listening.
- `PGDB` - The name of the database to connect to.
- `WORK_DIR` - The working directory for the application.

## Notebooks

### 1. Data Migration

- **File:** `Data_Setup.ipynb`
- **Description:** Imports the CSV file, transforms it, and migrates it to a relational PostgreSQL database using SQLAlchemy. In this step, the necessary tables are also created in the database.

### 2. Exploratory Data Analysis (EDA)

- **File:** `EDA.ipynb`
- **Description:** Performs exploratory analysis of the data loaded into the database. This includes identifying null values, reviewing data types, analyzing data distribution, and searching for patterns and correlations.

### 3. Data Transformation

- **File:** `Data_Transformation.ipynb`
- **Description:** Performs deeper data transformation, such as creating new columns (e.g., the `Hired` column) and categorizing technologies. The transformed data is loaded back into the database.

## Setting Up the Environment

1. Clone this repository:

    ```bash
    git clone https://github.com/alej0909/Workshop_ETL.git
    cd Workshop_ETL
    ```

2. Create the database:

    ```sql
    CREATE DATABASE your_db_name;
    ```

3. Create a `.env` file in the root of the project with the following environment variables for connecting to the PostgreSQL database:

    ```env
    PGDIALECT=your_host
    PGUSER=your_db_password
    PGPASSWD=your_db_user
    PGHOST=your_host_address
    PGPORT=5432
    PGDB=your_db_name
    WORK_DIR=your_working_directory
    ```

4. Set up and activate your virtual environment:

    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

5. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

You are now ready to start working on this workshop.


# 05_SQL – Structured Query Language

This folder covers my learning journey of **SQL (Structured Query Language)**, starting with theoretical concepts and moving into practical implementations.  
SQL is an essential tool for data analysis, data engineering, and database management, and this module lays the foundation for working with **relational databases**.

---

## Contents

### **Day 30 – SQL Theory Introduction**
- Learned the fundamentals of **databases and data storage**:
  - What is **data** and its types (structured, unstructured).
  - What is a **database** and why it is needed.
  - Types of databases:
    - Structured (SQL / Relational DBs).
    - Unstructured (NoSQL).
    - Vector Databases (used in AI/ML and GenAI applications).
  - SQL vs NoSQL vs Vector Databases.
  - Database deployment (server, cloud, dev vs production environments).
  - Evolution of databases (Flat file → Hierarchical → Relational → NoSQL → Vector).
  - Relational Database Concepts:
    - Tables, rows, columns.
    - Primary keys, foreign keys.
  - Importance of SQL for data professionals.
  - Real-world applications of SQL in **Banking, Healthcare, E-commerce, Social Media, Education**.

---

### **Day 31 – SQL Practical**
* Practiced writing SQL queries and commands for working with relational databases:

  * **DDL (Data Definition Language)**: Creating and modifying tables. `CREATE DATABASE`, `USE`, `SHOW DATABASES`
  * **DML (Data Manipulation Language)**: Inserting, updating, and deleting records.
  * **DQL (Data Query Language)**: Selecting and filtering data using `SELECT`, `WHERE`, `ORDER BY`.
  * **Constraints**: Applying primary keys, unique constraints, and not null.
  * **Joins**: Understanding how to combine data across multiple tables.
          * **INNER JOIN** – Common rows from both tables.
          * **LEFT JOIN** – All rows from left + matching from right.
          * **RIGHT JOIN** – All rows from right + matching from left.
          * **CROSS JOIN** – Cartesian product of both tables.
  * **Aggregate Functions**: Using `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
  * **Group By & Having** clauses.

---

### **Day 33 – SQL vs Python Data Analysis**

* Explored a **comparative study** between SQL queries and Python’s **Pandas library** for data analysis tasks.
* Tasks performed in **both SQL and Pandas**:

  * Selecting all or specific columns.
  * Filtering rows (exact matches, ranges, multiple values, prefix matching).
  * Sorting results.
  * Performing aggregations (`SUM`, `AVG`, `MIN`, `MAX`, `COUNT`, `DISTINCT`).
  * Grouping data with `GROUP BY` and filtering with `HAVING`.
  * Renaming columns.
  * Combining datasets with **UNION** and **JOINs**.
* **Key Observations:**

  * SQL is ideal for querying and managing large datasets directly within databases.
  * Pandas provides more flexibility for in-memory data analysis and works well with visualization/statistical tools.
---

## Key Takeaways

* SQL is the backbone of working with **structured data**.
* Learned both **theoretical concepts** (Day 30), **hands-on SQL queries** (Day 31), and **comparison with Python** (Day 33).
* Built understanding of how SQL complements **data science, machine learning, and analytics workflows**.
* Developed clarity on when to use SQL vs Python for data-related tasks.

---

# **Python Scripts**

This subdirectory has six scripts which are intended to be executed in logical sequence beginning with inspections_step_1.py.

*Note: Data objects are saved and shared across all scripts using **usuable.pkl**.*
***
### **Purpose of Scripts** 

- [inspections_step_1.py](inspections_step_1.py)
    - Removes unwanted columns
    - Renames column names
    - Drops records  of establishments with no violations
    - Determines the number of violations (critical and non-critical) by inspection date, establishment and borough. 

- [inspections_step_2.py](inspections_step_2.py)
    - Data cleaning
    - Standardizes restaurant names
    - Initial analysis on the number of violations in facilities with multiple locations across the five boroughs

- [inspections_step_3.py](inspections_step_3.py)
    - Removes non-gradable inspection types, special program and administrative violations that do not contribute towards overall score and grade

- [inspections_step_4.py](inspections_step_4.py)
    -  Assigns grades A, B or C based on the DoH scores

- [inspections_step_5.py](inspections_step_5.py)
    - Filters out duplicate and missing records for latitude and longitude coordinates 
    - Spells out abbreviations in street address
    - Standardizes and cleans up the street names
    - Creates three new variables to color code inspection grades in Tableau    

- [inspections_step_6.py](inspections_step_6.py)
    - Generates two summary figures: one showing the number of restaurants by food type/cuisine and another illustrating the count of resturants by borough

 
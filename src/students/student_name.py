
def get_student_name(name):
    if not name.isalpha():
        return "not a name"
    return name


def get_student_id(id):
    if not id.isdigit():
        return "not a valid ID"
    return id

def find_year_passout(year):
    if not (year.isdigit() and len(year) == 4 and year.with("20")):
        return "Enter a valid year"
    elif int(year) <= 2023:
        return "More experience for placement"
    elif int(year) == 2024:
        return "2 year of experience"
    elif int(year) == 2025:
        return "1 year of experience"
    elif int(year) == 2026:
        return "Freshers"
    elif int(year) == 2027:
        return "college student"
    else:
        return "Not eligible for placement"


    


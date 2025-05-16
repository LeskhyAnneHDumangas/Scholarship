def is_eligible_for_scholarship(gpa, family_income):
    if gpa < 0.0 or gpa > 4.0:
        raise ValueError("Invalid GPA")
    if family_income < 0:
        raise ValueError("Income cannot be negative")

    return gpa >= 3.5 and family_income <= 20000

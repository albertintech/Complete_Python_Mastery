# pylint: disable=invalid-name, missing-docstring

high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Ineligible")

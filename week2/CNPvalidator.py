def has_valid_length(cnp):
    if len(cnp) == 13:
        return 1
    return -1


def is_all_digits(cnp):
    for i in cnp:
        if not i.isdigit():
            return False
    return True


def has_valid_gender(cnp):
    if int(cnp[0]) in range(1, 10):
        return True
    return False


def has_valid_birth_month(cnp):
    if int(cnp[3]) == 0:
        return True
    if int(cnp[3]) == 1:
        if int(cnp[4]) in range(0, 3):
            return True
    return False


def has_valid_birth_day(cnp):
    if int(cnp[5]) in range(0, 2):
        return True
    if int(cnp[5]) == 3:
        if int(cnp[6]) in range(0, 2):
            return True
    return False


def has_valid_county_code(cnp):
    if int(cnp[7]) == 0:
        return True
    elif int(''.join(cnp[7:9])) in range(10, 53):
        return True
    return False


def has_valid_3digit_county_code(cnp):
    if cnp[9:12] != '000':
        return True
    return False


def has_valid_control_digit(cnp):
    control = '279146358279'
    s = 0
    for i in range(len(cnp) - 1):
        s += int(cnp[i]) * int(control[i])

    if s % 11 == 10:
        if int(cnp[12]) == 1:
            return True
    if int(cnp[12]) == s % 10:
        return True
    return False


def verify_cnp(cnp):
    if not has_valid_length(cnp):
        return 'The CNP has not a valid length! Make sure it has 13 digits'
    if not is_all_digits(cnp):
        return 'The CNP does not contain just digits!'
    if not has_valid_gender(cnp):
        return 'S - The gender digit is invalid!'
    if not has_valid_birth_month(cnp):
        return 'LL - The birth month digits are invalid!'
    if not has_valid_birth_day(cnp):
        return 'ZZ - The birth day digits are invalid!'
    if not has_valid_county_code(cnp):
        return 'JJ - The county code is invalid!'
    if not has_valid_3digit_county_code(cnp):
        return 'NN - The 3 digit county code is invalid!'
    if not has_valid_control_digit(cnp):
        return 'C - The control digit is invalid!'
    return 'The CNP is valid!'


print(verify_cnp('9990301410102'))

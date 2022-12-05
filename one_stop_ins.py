# QAP 4: A program for One Stop Insurance. Allows to enter and calculate new insurance policies
# as well as output a receipt.
# Author: Glen Sturge       Date: 12/04/2022

# Imports
import fmt_fun as ff
import valid_fun as vf
import datetime

dt = datetime.datetime


# Constants
with open('OSICDef.dat', 'r') as f:
    POLICY_ID = int(f.readline().strip())
    BASIC_PREM = float(f.readline().strip())
    MULTI_DISC_RATE = float(f.readline().strip())
    LIABILITY_COVER = float(f.readline().strip())
    GLASS_COVER = float(f.readline().strip())
    LOANER_COVER = float(f.readline().strip())
    HST_RATE = float(f.readline().strip())
    PROC_FEE = float(f.readline().strip())

PROV_CODES = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"]
COMP_NAME = "One Stop Insurance Company"
REC_BREAK = " " + "_" * 39
REC_BREAK_SMALL = " " * 30 + "-" * 10


# """
TODAY = dt.today()


# print(POLICY_ID)
# print(BASIC_PREM)
# print(MULTI_CAR_DISC)
# print(LIABILITY_COVER)
# print(GLASS_COVER)
# print(LOANER_COVER)
# print(HST_RATE)
# print(PROC_FEE)


while True:

    # Inputs
    # | Customer Personal Data
    # || Customer First Name
    while True:
        cust_fn = input(ff.f_inp_f30("Enter Customer First Name")).capitalize()
        if vf.not_blank(cust_fn):
            break

    # || Customer Last Name
    while True:
        cust_ln = input(ff.f_inp_f30("Enter Customer Last Name")).capitalize()
        if vf.not_blank(cust_ln):
            break

    # || Customer Street Address
    while True:
        cust_street = input(ff.f_inp_f30("Enter Customer Street Address"))
        if vf.not_blank(cust_street):
            cust_street = ff.f_space_cap(cust_street)
            break

    # || Customer City
    while True:
        cust_city = input(ff.f_inp_f30("Enter Customer City"))
        if vf.not_blank(cust_city):
            cust_city = ff.f_space_cap(cust_city)
            break

    # || Customer Province
    while True:
        print()
        print(PROV_CODES)
        print()
        cust_prov = input(ff.f_inp_f30("Enter Customer Province Code")).upper().strip()
        if cust_prov in PROV_CODES:
            break
        else:
            print("\nCheck Input & Try Again.\n")

    # || Customer Postal
    while True:
        print("\nPostal Code Format : L#L#L#\n")
        cust_postal = input(ff.f_inp_f30("Enter Customer Postal Code")).upper()
        if vf.check_postal(cust_postal):
            break

    # || Customer Phone
    while True:
        print("\nPhone Format : ###-###-####\n")
        cust_phone = input(ff.f_inp_f30("Enter Customer 10-Digit Phone"))
        if vf.check_phone(cust_phone):
            break

    # | Customer Options
    # || Liability
    while True:
        print("\nExtra Liability Coverage Up To $1,000,000.\n")
        liability = input(ff.f_inp_f30("Enter Customer Choice (Y/N)")).upper().strip()
        if liability == 'Y' or liability == 'N':
            break
        else:
            print("\nCheck Input & Try Again.")

    # || Glass Coverage
    while True:
        print("\nOptional Glass Coverage.\n")
        glass_cover = input(ff.f_inp_f30("Enter Customer Choice (Y/N)")).upper().strip()
        if glass_cover == 'Y' or glass_cover == 'N':
            break
        else:
            print("\nCheck Input & Try Again.")

    # || Optional Loaner Coverage
    while True:
        print("\nOptional Loaner Coverage.\n")
        loaner_cover = input(ff.f_inp_f30("Enter Customer Choice (Y/N)")).upper().strip()
        if loaner_cover == 'Y' or loaner_cover == 'N':
            break
        else:
            print("\nCheck Input & Try Again.")

    # || Full Annual or Monthly Pay
    while True:
        print("\nPay Full Annual Amount or Pay Monthly\n")
        pay_type = input(ff.f_inp_f30("Enter Customer Choice (F/M)")).upper().strip()
        if pay_type == 'F' or pay_type == 'M':
            break
        else:
            print("\nCheck Input & Try Again.")

    # || Number Of Vehicles
    while True:
        num_cars = 0
        try:
            num_cars = int(input(ff.f_inp_f30("Enter Number Of Vehicles")))
        except ValueError:
            print("That Wasn't A Number")
        if num_cars <= 0:
            print("Number Of Cars Must Be 1 or Greater.")
        else:
            break

    # """

    # | Test Assignments
    # TODAY = dt.strptime("2022-05-26", "%Y-%m-%d")
    # cust_fn = "Bjarne"
    # cust_ln = "Stroustrup"
    # cust_street = "45 Aarhus Ave"
    # cust_city = "St. John's"
    # cust_prov = "NL"
    # cust_postal = "A3E5T2"
    # cust_phone = "195-012-3071"
    # liability = "Y"
    # glass_cover = "Y"
    # loaner_cover = "Y"
    # pay_type = "M"
    # num_cars = 10

    # Calculations
    # | Insurance Premium.
    ins_premium_before_disco = BASIC_PREM * num_cars
    ins_premium_disc = 0
    ins_premium = 0
    if num_cars > 1:
        ins_premium_disc = (num_cars - 1) * BASIC_PREM * MULTI_DISC_RATE
        ins_premium = ins_premium_before_disco - ins_premium_disc
    else:
        ins_premium = ins_premium_before_disco

    # | Optional Coverage Options.
    liability_cost, glass_cost, loaner_cost = 0, 0, 0
    if vf.check_yes(liability):
        liability_cost = LIABILITY_COVER * num_cars
    if vf.check_yes(glass_cover):
        glass_cost = GLASS_COVER * num_cars
    if vf.check_yes(loaner_cover):
        loaner_cost = LOANER_COVER * num_cars
    extras_total = liability_cost + glass_cost + loaner_cost

    # | Totals & HST.
    total_ins_premium = ins_premium + extras_total
    hst = total_ins_premium * HST_RATE
    total_cost = total_ins_premium + hst

    # | Monthly Payment Mod.
    monthly_payment = 0
    first_pay_date = TODAY
    if pay_type == 'M':
        monthly_payment = (total_cost + PROC_FEE) / 8
        # || First Payment Date
        if TODAY.month == 12:
            if TODAY.day > 25:
                first_pay_date = dt.strptime(f"{TODAY.year + 1}-02-01", "%Y-%m-%d")
            else:
                first_pay_date = dt.strptime(f"{TODAY.year + 1}-01-01", "%Y-%m-%d")
        elif TODAY.month == 11:
            if TODAY.day > 25:
                first_pay_date = dt.strptime(f"{TODAY.year + 1}-01-01", "%Y-%m-%d")
        elif TODAY.day > 25:
            first_pay_date = dt.strptime(f"{TODAY.year}-{TODAY.month + 2}-01", "%Y-%m-%d")
        else:
            first_pay_date = dt.strptime(f"{TODAY.year}-{TODAY.month + 1}-01", "%Y-%m-%d")

    policy_num = f"{POLICY_ID}-{cust_fn[0]}{cust_ln[0]}"
    policy_date = TODAY.strftime('%Y-%m-%d')

    # | Test prints
    # print(f"Multi discount: {ins_premium_disc}")
    # print(f"Premium: {ins_premium}")
    # print(f"Liability cost: {liability_cost}")
    # print(f"glass cost: {glass_cost}")
    # print(f"loaner cost: {loaner_cost}")
    # print(f"total premium: {total_ins_premium}")
    # print(f"hst: {hst}")
    # print(f"total cost: {total_cost}")
    #
    # print(f"Monthly payment: {monthly_payment}")
    #
    # print(f"Policy Num : {policy_num}")
    # print(f"Policy date : {policy_date}")

    # | Receipt
    print("\n\n")

    print(f"{REC_BREAK}\n")
    print(f" {COMP_NAME}")
    print(" 2 Big Insurance Ave")
    print(" St. John's, NL, A1B2J1")
    print(" Phone: (709) 444-1260")
    print(" Fax: (709) 444-1261")
    print(" Email: inquire@onestopinsurance.com\n")

    print(" Customer info:")
    print(f" {cust_fn} {cust_ln}")
    print(f" {cust_street}")
    print(f" {cust_city}, {cust_prov}, {cust_postal}")

    print(f" Phone: {ff.f_phone_10(cust_phone.replace('-', ''))}\n")

    print(f" Policy Number: {policy_num}")
    print(f" Policy date:   {policy_date}")

    print(f"{REC_BREAK}\n")

    print(" Customer options:")
    # print(" -----------------")
    print(f" Number of vehicles to insure:        {num_cars:>2d}")
    print(f" Extra liability ($1M):              {ff.yes_no_dsp(liability):>3s}")
    print(f" Glass coverage:                     {ff.yes_no_dsp(glass_cover):>3s}")
    print(f" Loaner coverage:                    {ff.yes_no_dsp(loaner_cover):>3s}")

    print(f"{REC_BREAK}\n")

    print(f" Premium cost\n before discount:             {ff.f_dol_com_2d(ins_premium_before_disco):>10s}")
    print(f" Multi-vehicle\n discount savings:            {ff.f_dol_com_2d(ins_premium_disc):>10s}")
    print(REC_BREAK_SMALL)
    print(f" Premium cost:                {ff.f_dol_com_2d(ins_premium):>10s}\n")

    if vf.check_yes(liability) or vf.check_yes(glass_cover) or vf.check_yes(loaner_cover):
        print(" Extras charges:")
    if vf.check_yes(liability):
        print(f" Liability coverage:          {ff.f_dol_com_2d(liability_cost):>10s}")
    if vf.check_yes(glass_cover):
        print(f" Glass coverage:              {ff.f_dol_com_2d(glass_cost):>10s}")
    if vf.check_yes(loaner_cover):
        print(f" Loaner coverage:             {ff.f_dol_com_2d(loaner_cost):>10s}")
    print(REC_BREAK_SMALL)
    print(f" Total:                       {ff.f_dol_com_2d(extras_total):>10s}")
    print(f"{REC_BREAK}\n")
    print(f" Subtotal:                    {ff.f_dol_com_2d(total_ins_premium):>10s}")
    print(f" HST:                         {ff.f_dol_com_2d(hst):>10s}")
    print(REC_BREAK_SMALL)
    print(f" Total:                       {ff.f_dol_com_2d(total_cost):>10s}")
    print(f"{REC_BREAK}\n")

    if pay_type == "M":
        print(" Monthly payment selected:\n")
        print(f" Processing fee:              {ff.f_dol_com_2d(PROC_FEE):>10s}")
        print(f" Monthly payment:             {ff.f_dol_com_2d(monthly_payment):>10s}")
        print(f" First payment date:          {ff.f_date_standard(first_pay_date)}")
        print(f"{REC_BREAK}\n")

    print(f"{'We appreciate you business!':^40s}")
    print(f"{'Please retain this receipt for':^40s}")
    print(f"{'your records.':^40s}\n")
    print(f"{'Thank You!':^40s}")

    print(REC_BREAK)

    # Character ruler.
    # print("\n1234567890123456789012345678901234567890")
    # print("         10        20        30        40")

    # Append current policy data to file.
    with open("Policies.dat", "a") as p:
        p.write("{}, ".format(policy_num))
        p.write("{}, ".format(cust_fn))
        p.write("{}, ".format(cust_ln))
        p.write("{}, ".format(cust_street))
        p.write("{}, ".format(cust_city))
        p.write("{}, ".format(cust_prov))
        p.write("{}, ".format(cust_postal))
        p.write("{}, ".format(cust_phone))
        p.write("{}, ".format(num_cars))
        p.write("{}, ".format(liability))
        p.write("{}, ".format(glass_cover))
        p.write("{}, ".format(loaner_cover))
        p.write("{}, ".format(pay_type))
        p.write("{}\n".format(total_ins_premium))

    print("\nPolicy information processed and saved.\n")
    POLICY_ID += 1

    # Ask user if they want to continue to process another policy.
    while True:
        ask_continue = input(ff.f_inp_f30("Would you like to process another policy? (Y/N)")).upper()
        if ask_continue != "Y" and ask_continue != "N":
            print("Error! Check input and try again.\n")
        else:
            break

    if not vf.check_yes(ask_continue):
        break

    print()

# Write defaults and updated policy number back to file.
with open('OSICDef.dat', 'w') as f:
    f.write("{}\n".format(str(POLICY_ID)))
    f.write("{}\n".format(str(BASIC_PREM)))
    f.write("{}\n".format(str(MULTI_DISC_RATE)))
    f.write("{}\n".format(str(LIABILITY_COVER)))
    f.write("{}\n".format(str(GLASS_COVER)))
    f.write("{}\n".format(str(LOANER_COVER)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(PROC_FEE)))

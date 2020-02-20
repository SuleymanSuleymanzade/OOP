import payment_system 


def main():
    emp1 = payment_system.SalaryEmployee("N1", "S1", 432)
    emp2 = payment_system.CommissionEmployee("N2", "S2", 432, 22)
    emp3 = payment_system.HourlyEmployee("N3", "S3", 24, 20)

    ps = payment_system.PaymentSystem([emp1, emp2, emp3])
    ps.show_salaries()

if __name__ == "__main__":
    main()

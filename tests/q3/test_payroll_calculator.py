import pytest

from refatoracao.q3.payroll_calculator import Employee, Overtime, PayrollCalculator


def test_net_salary_examples():
    calc = PayrollCalculator()

    e1 = Employee(
        2800,
        [Overtime(10, 25)],
        True,
        120,
    )
    salary1 = calc.monthly_net_salary(e1)
    assert salary1 == pytest.approx(
        2800 + (10 * 25) - ((2800 + (10 * 25)) * 0.12) - 120 + 450, abs=0.01
    )

    e2 = Employee(
        7500,
        [],
        False,
        200,
    )
    salary2 = calc.monthly_net_salary(e2)
    assert salary2 == pytest.approx(7500 - (7500 * 0.18) - 200, abs=0.01)

    e3 = Employee(
        2000,
        [],
        False,
        50,
    )
    salary3 = calc.monthly_net_salary(e3)
    assert salary3 == pytest.approx(2000 - (2000 * 0.08) - 50, abs=0.01)


def test_refactor_goal_replace_temps_with_queries():
    # TODO: após refatorar, use queries (métodos) no lugar de muitos temporários.
    # Testes acima devem continuar passando.
    calc = PayrollCalculator()
    e = Employee(3000, [Overtime(2, 50)], True, 100)
    
    assert calc._overtime_pay(e) == 100.0
    assert calc._gross_salary(e) == 3100.0
    assert calc._tax(e) == pytest.approx(3100.0 * 0.12)
    assert calc._meal_voucher(e) == 450.0

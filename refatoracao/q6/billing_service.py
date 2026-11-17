from abc import ABC, abstractmethod
from enum import Enum


class Plan(Enum):
    FREE = "FREE"
    STUDENT = "STUDENT"
    PRO = "PRO"
    ENTERPRISE = "ENTERPRISE"

class PlanPricing(ABC):
    @abstractmethod
    def calculate(self, active_users: int, priority_support: bool) -> float: ...

class FreePlanPricing(PlanPricing):
    def calculate(self, active_users: int, priority_support: bool) -> float:
        return 0.0

class StudentPlanPricing(PlanPricing):
    def calculate(self, active_users: int, priority_support: bool) -> float:
        price = 19.90
        if priority_support:
            price += 59.90
        return price

class ProPlanPricing(PlanPricing):
    def calculate(self, active_users: int, priority_support: bool) -> float:
        price = 49.90 + (active_users * 1.25)
        if priority_support:
            price += 59.90
        if active_users > 200:
            price *= 0.95
        return price

class EnterprisePlanPricing(PlanPricing):
    def calculate(self, active_users: int, priority_support: bool) -> float:
        price = 199.90 + (active_users * 0.90)
        if priority_support:
            price += 59.90
        return price

_PRICING_POLICIES: dict[Plan, PlanPricing] = {
    Plan.FREE: FreePlanPricing(),
    Plan.STUDENT: StudentPlanPricing(),
    Plan.PRO: ProPlanPricing(),
    Plan.ENTERPRISE: EnterprisePlanPricing(),
}


class BillingService:

    def monthly_price(self, plan: Plan, active_users: int, priority_support: bool) -> float:
        policy = _PRICING_POLICIES.get(plan)
        if policy is None:
            raise ValueError(f"Plano desconhecido: {plan}")
        return round(policy.calculate(active_users, priority_support), 2)

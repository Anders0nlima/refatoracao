from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class PurchaseItem:
    name: str
    quantity: int
    unit_price: float


@dataclass(frozen=True)
class Address:
    street: str
    number: str
    city: str
    zip_code: str


@dataclass(frozen=True)
class Purchase:
    id: str
    customer_name: str
    items: list[PurchaseItem]
    is_express: bool
    coupon: str | None
    address: Address


class PurchaseEmailService:

    def build_email(self, purchase: Purchase) -> str:
        subtotal = self._calculate_subtotal(purchase.items)
        shipping = self._calculate_shipping(purchase.is_express)
        discount = self._calculate_discount(subtotal, purchase.coupon)
        total = subtotal + shipping - discount
        
        parts = [
            f"Olá, {purchase.customer_name}!\n\n",
            f"Seu pedido #{purchase.id} foi confirmado em {date.today()}.\n\n",
            self._format_items(purchase.items),
            f"\nSubtotal: R$ {subtotal:.2f}\n",
            f"Frete: R$ {shipping:.2f}\n",
            f"Descontos: R$ {discount:.2f}\n",
            f"TOTAL: R$ {total:.2f}\n\n",
            self._format_address(purchase.address),
            "Obrigado por comprar com a gente!\n",
        ]
        return "".join(parts)

    def _calculate_subtotal(self, items: list[PurchaseItem]) -> float:
        return sum(it.unit_price * it.quantity for it in items)
    
    def _calculate_shipping(self, is_express: bool) -> float:
        return 29.90 if is_express else 14.90
    
    def _calculate_discount(self, subtotal: float, coupon: str | None) -> float:
        discount = 0.0
        if subtotal >= 300.0:
            discount += subtotal * 0.10
        if coupon is not None and coupon.startswith("VIP"):
            discount += 20.0
        return discount
    
    def _format_items(self, items: list[PurchaseItem]) -> str:
        lines = ["Itens:\n"]
        for it in items:
            line = it.unit_price * it.quantity
            lines.append(f"- {it.name} ({it.quantity}x) : R$ {line:.2f}\n")
        return "".join(lines)
    
    def _format_address(self, address: Address) -> str:
        return (
            f"Endereço de entrega:\n"
            f"{address.street}, {address.number}\n"
            f"{address.city} - {address.zip_code}\n\n"
        )

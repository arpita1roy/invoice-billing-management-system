def calculate_invoice(items, discount_percent=0, tax_percent=0):
    """
    Calculate subtotal, discount, tax and final invoice amount.

    items should contain:
    {
        "name": product/service name,
        "quantity": quantity,
        "price": price per unit
    }
    """

    subtotal = sum(
        item["quantity"] * item["price"]
        for item in items
    )

    discount = subtotal * (discount_percent / 100)
    taxable_amount = subtotal - discount
    tax = taxable_amount * (tax_percent / 100)

    total = taxable_amount + tax

    return {
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "tax": round(tax, 2),
        "total": round(total, 2)
    }


if __name__ == "__main__":
    items = [
        {
            "name": "Website Development",
            "quantity": 1,
            "price": 15000
        },
        {
            "name": "Domain & Hosting",
            "quantity": 1,
            "price": 3000
        }
    ]

    invoice = calculate_invoice(
        items,
        discount_percent=10,
        tax_percent=18
    )

    print("Invoice Summary")
    print("----------------")
    print(f"Subtotal : ₹{invoice['subtotal']}")
    print(f"Discount : ₹{invoice['discount']}")
    print(f"Tax      : ₹{invoice['tax']}")
    print(f"Total    : ₹{invoice['total']}")

def shopping_cart(*items, **prices):
    print("Items:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

    print("\nPrices:")
    total = 0
    for i, (item, price) in enumerate(prices.items(), 1):
        print(f"{i}. {item}: {price}")
        total += price

    print(f"\nTotal bill: {round(total, 2)}")

shopping_cart(
    "Shoes", "T-shirt",
    Shoes=50, Tshirt=20
)

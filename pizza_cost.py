#!/usr/bin/env python3
# calculating pizza cost
# maximiliano fairman
import constants


def calculate_pizza_cost():

    diameter = float(input("Enter the diameter of the pizza in inches: "))
    subtotal = (
        constants.LABOUR
        + constants.RENTAL
        + (constants.INGREDIENT_COST_PER_INCH * diameter)
    )
    tax = subtotal * constants.HST
    total = subtotal + tax

    print(f"Total cost: ${total:.2f}")


if __name__ == "__main__":
    calculate_pizza_cost()

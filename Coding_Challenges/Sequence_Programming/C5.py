def calculate_sales():
    acres_per_segment = 16

    # Tomato calculation
    tomato_yield = (
        (0.3 * acres_per_segment * 10) +
        (0.7 * acres_per_segment * 12)
    )
    tomato_sales = tomato_yield * 1000 * 7

    # Potato calculation
    potato_yield = acres_per_segment * 10
    potato_sales = potato_yield * 1000 * 20

    # Cabbage calculation
    cabbage_yield = acres_per_segment * 14
    cabbage_sales = cabbage_yield * 1000 * 24

    # Sunflower calculation
    sunflower_yield = acres_per_segment * 0.7
    sunflower_sales = sunflower_yield * 1000 * 200

    # Sugarcane calculation
    sugarcane_yield = acres_per_segment * 45
    sugarcane_sales = sugarcane_yield * 4000

    # a) Overall sales
    overall_sales = (
        tomato_sales + potato_sales +
        cabbage_sales + sunflower_sales +
        sugarcane_sales
    )

    # b) Chemical-free sales at end of 11 months
    chemical_free_sales = (
        tomato_sales + potato_sales +
        cabbage_sales + sunflower_sales
    )

    return overall_sales, chemical_free_sales


if __name__ == "__main__":
    total_sales, chemical_free_sales = calculate_sales()

    print("Overall Sales from 80 acres: ₹", int(total_sales))
    print("Chemical-free Sales after 11 months: ₹", int(chemical_free_sales))

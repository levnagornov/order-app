import product_service

def main() -> None:
    products = product_service.get_products()
    product_service.print_product_categories_name(products)

if __name__ == "__main__":
    main()
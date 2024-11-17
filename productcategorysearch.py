# Example test for BBST (AVL Tree)
product_tree = ProductCategoryTree()
product_tree.insert("Electronics", "Smartphone")  # Insert product into category
product_tree.insert("Electronics", "Laptop")  # Insert another product

# Search for products in Electronics category
print(product_tree.search("Electronics"))  # Expected output: ["Smartphone", "Laptop"]
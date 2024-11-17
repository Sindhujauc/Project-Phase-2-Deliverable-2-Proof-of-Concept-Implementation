# Full Integration Testing
if _name_ == "_main_":
    system = RecommendationSystem()
    
    # Adding interactions
    print("Adding interactions...")
    system.add_interaction(1, 101, "Electronics", 90)
    system.add_interaction(1, 102, "Electronics", 85)
    system.add_interaction(2, 201, "Home Appliances", 95)
    
    # Testing user recommendations
    print("Recommendations for User 1:")
    print(system.recommend(1, 2))  # Expect top 2 products for User 1
    
    print("Recommendations for User 2:")
    print(system.recommend(2, 1))  # Expect top 1 product for User 2
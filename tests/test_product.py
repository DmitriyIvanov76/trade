def test_product(mobile_telephone):
    assert mobile_telephone.name == "Samsung"
    assert mobile_telephone.description == "256GB"
    assert mobile_telephone.price == 50000
    assert mobile_telephone.quantity == 5

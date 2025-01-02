import hystorian_hysteria

def test_calc_digits():
    nums = [2, 1, 0, 1, 2, 5]
    result = hystorian_hysteria.calc_digits(nums)
    assert result == 11

def test_calc_pair_distance():
    r1 = hystorian_hysteria.cacl_pair_distance(3, 7)
    r2 = hystorian_hysteria.cacl_pair_distance(9, 3)

    assert r1 == 4
    assert r2 == 6

def test_sort_list():
    nums = [3, 4, 2, 1, 3, 3]
    sorted = hystorian_hysteria.sort_list(nums)

    assert sorted ==  [1, 2, 3, 3, 3, 4]

def test_get_list_distances():
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]
    
    result = hystorian_hysteria.get_list_distances(left, right)

    assert result == [2, 1, 0, 1, 2, 5]

def test_get_nums_from_input_line():
    f = open("inputs/hystorian_hysteria.txt", "r")
    input = f.readline()

    tuple = hystorian_hysteria.get_nums_from_input_line(input)
    assert tuple == [35039, 67568]

def test_get_distance_total():
    result = hystorian_hysteria.get_distance_total()
    print(result)

    assert result == 2164381

def test_similarity_score():
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]

    result = hystorian_hysteria.get_similarity_score(left, right)

    assert result == 31

def test_similarity_total():

    result = hystorian_hysteria.get_similarity_total()

    assert result == 20719933


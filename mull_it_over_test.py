
import mull_it_over

def test_get_enabled_mul_instances():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    result = mull_it_over.get_enabled_mul_instances(input)

    assert len(result) == 2

def test_parse_mul():
    input = "mul(123,432)"
    result = mull_it_over.parse_mul(input)

    assert result == (123, 432)

def test_calculate_mul_total():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    result = mull_it_over.calc_mul_total(input)

    assert result == 48

def test_calculate_mul_total_from_input():
    f = open("inputs/mull_it_over.txt", "r")

    input = f.read()
    result = mull_it_over.calc_mul_total(input)

    f.close

    assert result == 76729637
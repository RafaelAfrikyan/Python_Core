from typing import Union
import math
NumType = Union[int, float]

def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
  result = None
  result = (12 * a + 25 * b) / (1 + a**(2**b))
  rounded_result = round(result, 2)
  return math.ceil(rounded_result * 100) / 100
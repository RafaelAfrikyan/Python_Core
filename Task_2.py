def get_fractions(a_b: str, c_b: str) -> str:
   
   numerator1, denominator = a_b.split('/')
   numerator2 = c_b.split('/')[0]
   numerator_sum = int(numerator1) + int(numerator2)

   return   f"{a_b} + {c_b} = {numerator_sum}/{denominator}"
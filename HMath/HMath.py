modes = ["add", "subtract", "multiply", "divide", "remainder"]
def add(a, b, *extra):
  out = a + b
  for c in extra:
    out = out + c
  return out
def subtract(a, b, *extra):
  out = a - b
  for c in extra:
    out = out - c
  return out
def multiply(a, b, *extra):
  out = a * b
  for c in extra:
    out = out * c
  return out
def divide(a, b, *extra):
  out = a / b
  for c in extra:
    out = out / c
  return out
def power(a, b, *extra):
  out = a ** b
  for c in extra:
    out = out ** c
  return out
def remainder(a, b, *extra):
  out = a % b
  for c in extra:
    out = out % c
  return out
def any(mode, a, b *extra):
  for mode2 in modes:
    if mode2 in mode:
      if extra == []:
        return eval(f"{mode2}({a}, {b})")
      else:
        return eval(f"{mode2}({a}, {b}, {str(extra).replace("[", "").replace("]", "")})")

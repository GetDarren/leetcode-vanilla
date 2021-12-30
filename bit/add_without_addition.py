def addBinary(a: str, b: str) -> str:
  '''
  AND + left shift to find where to carry
  XOR to perform the addition
  '''
  res = ''
  carry = 0
  a = list(a)
  b = list(b)
  while a or b or carry:
    tmp_a = a.pop() if a else '0'
    tmp_b= b.pop() if b else '0'
    tmp = tmp_a + tmp_b
    if tmp == '00':
      if carry:
        res += '1'
      else:
        res += '0'

      carry = 0
    elif tmp in ['01','10']:
      if carry:
        res += '0'
      else:
        res += '1'
    elif tmp == '11':
      if carry:
        res += '1'
      else:
        res += '0'
        carry = 1
  return res

print(addBinary('11','1'))
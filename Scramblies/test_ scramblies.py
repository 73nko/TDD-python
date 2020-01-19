from scramblies import scramble


def test_simple_word():
  s1 = 'rkqodlw'
  s2 = 'world'
  assert scramble(s1, s2) == True




# Test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
# Test.assert_equals(scramble('katas', 'steak'), False)
# Test.assert_equals(scramble('scriptjava', 'javascript'), True)
# Test.assert_equals(scramble('scriptingjava', 'javascript'), True)
const StringCalculator = require('./StringCalculator')

describe('StringCalculator', () => {
  let calculator

  beforeEach(() => {
    calculator = new StringCalculator()
  })

  test('returns 0 for an empty string', () => {
    expect(calculator.add('')).toBe(0)
  })

  test('returns the number itself for a single number', () => {
    expect(calculator.add('1')).toBe(1)
  })

  test('returns the sum of two numbers', () => {
    expect(calculator.add('1,5')).toBe(6)
  })

  test('handles an unknown amount of numbers', () => {
    expect(calculator.add('1,2,3,4,5')).toBe(15)
  })

  test('handles newlines between numbers', () => {
    expect(calculator.add('1\n2,3')).toBe(6)
  })

  test('handles custom delimiters', () => {
    expect(calculator.add('//;\n1;2;3')).toBe(6)
  })

  test('throws an error for a single negative number', () => {
    expect(() => calculator.add('1,-2,3')).toThrow(
      'Negative numbers not allowed: -2'
    )
  })

  test('throws an error for multiple negative numbers', () => {
    expect(() => calculator.add('-1,-2,3')).toThrow(
      'Negative numbers not allowed: -1, -2'
    )
  })
})

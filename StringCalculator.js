class StringCalculator {
  add(numbers) {
    if (!numbers) return 0

    let delimiter = /,|\n/
    if (numbers.startsWith('//')) {
      const delimiterMatch = numbers.match(/^\/\/(.+)\n/)
      delimiter = new RegExp(delimiterMatch[1])
      numbers = numbers.slice(delimiterMatch[0].length)
    }

    const nums = numbers
      .split(delimiter)
      .map((num) => parseInt(num, 10))
      .filter((num) => !isNaN(num))
  }
}

// Exporting the class for unit testing
module.exports = StringCalculator

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = ",|\n"
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            custom_delimiter = parts[0][2:]
            delimiter = custom_delimiter
            numbers = parts[1]

        import re
        nums = re.split(delimiter, numbers)

        nums = [int(num) for num in nums if num.isdigit()]

        negatives = [num for num in nums if num < 0]
        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

        return sum(nums)

class FizzBuzz:
    def do_fizz(self, number):
        if int(number) % 3 == 0 and int(number) % 5 == 0:
            return 'FizzBuzz'
        if int(number) % 3 == 0:
            return 'Fizz'
        if int(number) % 5 == 0:
            return 'Buzz'
        return number

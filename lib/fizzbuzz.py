class FizzBuzz:
    def do_fizz(self, number):
        # multiple return method
        if number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz'
        if number % 3 == 0:
            return 'Fizz'
        if number % 5 == 0:
            return 'Buzz'
        return number

        # single return method
        # answer = number
        # if number % 3 == 0:
        #     answer = 'Fizz'
        # if number % 5 == 0:
        #     answer = 'Buzz'
        # if number % 3 == 0 and number % 5 == 0:
        #     answer = 'FizzBuzz'
        # return answer

        # string concatenate method
        # answer = ''
        # if number % 3 == 0:
        #     answer += 'Fizz'
        # if number % 5 == 0:
        #     answer += 'Buzz'
        # if answer == '':
        #     answer = number
        # return answer

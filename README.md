# Abstract
The infamous FizzBuzz kata.

# Requirements
```commandline
pip install behave pyhamcrest
```

# Run tests
```commandline
behave features
```

```text
Feature: FizzBuzz # features/fizzbuzz.feature:2
  Write a program that prints the numbers from 1 to 100. But
  for multiples of three print "Fizz" instead of the number and
  for the multiples of five print "Buzz". For numbers which are
  multiples of both three and five print "FizzBuzz".
  Sample output:
  1
  2
  Fizz
  4
  Buzz
  Fizz
  7
  8
  Fizz
  Buzz
  11
  Fizz
  13
  14
  FizzBuzz
  16
  17
  Fizz
  19
  Buzz
  ...etc up to 100
  Scenario: 1 = 1                       # features/fizzbuzz.feature:32
    Given the number "1"                # features/steps/fizzbuzz_steps.py:5 0.000s
    When we run do_fizz with the number # features/steps/fizzbuzz_steps.py:9 0.000s
    Then we expect back "1"             # features/steps/fizzbuzz_steps.py:14 0.000s

  Scenario: 2 = 2                       # features/fizzbuzz.feature:37
    Given the number "2"                # features/steps/fizzbuzz_steps.py:5 0.000s
    When we run do_fizz with the number # features/steps/fizzbuzz_steps.py:9 0.000s
    Then we expect back "2"             # features/steps/fizzbuzz_steps.py:14 0.000s

  Scenario: 3 = Fizz                    # features/fizzbuzz.feature:42
    Given the number "3"                # features/steps/fizzbuzz_steps.py:5 0.000s
    When we run do_fizz with the number # features/steps/fizzbuzz_steps.py:9 0.000s
    Then we expect back "Fizz"          # features/steps/fizzbuzz_steps.py:14 0.000s

  Scenario: 5 = Buzz                    # features/fizzbuzz.feature:47
    Given the number "5"                # features/steps/fizzbuzz_steps.py:5 0.000s
    When we run do_fizz with the number # features/steps/fizzbuzz_steps.py:9 0.000s
    Then we expect back "Buzz"          # features/steps/fizzbuzz_steps.py:14 0.000s

  Scenario: 15 = FizzBuzz               # features/fizzbuzz.feature:52
    Given the number "15"               # features/steps/fizzbuzz_steps.py:5 0.000s
    When we run do_fizz with the number # features/steps/fizzbuzz_steps.py:9 0.000s
    Then we expect back "FizzBuzz"      # features/steps/fizzbuzz_steps.py:14 0.000s

1 feature passed, 0 failed, 0 skipped
5 scenarios passed, 0 failed, 0 skipped
15 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.002s
```


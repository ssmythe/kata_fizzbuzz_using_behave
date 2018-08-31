# Created by ss250852 at 8/31/18
Feature: FizzBuzz

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

  Scenario: 1 = 1
    Given the number "1"
    When we run do_fizz with the number
    Then we expect back "1"

  Scenario: 2 = 2
    Given the number "2"
    When we run do_fizz with the number
    Then we expect back "2"

  Scenario: 3 = Fizz
    Given the number "3"
    When we run do_fizz with the number
    Then we expect back "Fizz"

  Scenario: 5 = Buzz
    Given the number "5"
    When we run do_fizz with the number
    Then we expect back "Buzz"

  Scenario: 15 = FizzBuzz
    Given the number "15"
    When we run do_fizz with the number
    Then we expect back "FizzBuzz"

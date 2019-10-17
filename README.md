# Joshua_Challenge

## Infrastructure

### The Problem

Create a fully scripted process to deploy a web server instance, secure it,
serve a static page on it and test it's configuration.

### The Solution

Create a set of Ansible playbooks to:
- Create and start a EC2 instance.
- Create and place the static content.
- Install, configure and start a Nginx server.
- Verify server configuration.

## Coding

### The Problem

Create a complex number type.

Use the type to take two complex numbers and print the result of their
addition, subtraction, multiplication, division and modulus operations.
Values should be printed with two decimal points of precision.

Note: Modulus, in the case of complex numbers, is the real-only magnitude
of the number.

### Solution

If this were a real-world scenario, the most likely solution would be "just
use the built-in type". If that didn't satisfy certain requirements, the
next best thing would be to find a library that provides what is needed or
to subclass the complex type and customize it's behavior. Unfortunately,
these answers aren't in the spirit of the exercise, so we'll have to do
this the hard way.

Specifically, we'll make a custom class that with two float values to hold
the real and imaginary parts of the complex number. We'll then provide
implementations for numeric operations so our class can be used with
mathematical operators just like a built-in type. Then we'll provide a
string representation function for output purposes.

### Tasks

- Create a custom complex number type.
- Create a test script for manual and automated testing.
- Add given examples to the test script for automated testing.
- Add input capability for manual testing.
- Allow running test script with built-in or custom type.
- Add operator support to the custom type:
    - addition
    - subtraction
    - multiplacation
    - division
    - modulus
- Add string representation support.
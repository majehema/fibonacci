Write a RESTful service in Python that features the following endpoints. Try to apply general python best
practices where applicable (i.e. imagine this will be a larger application later).

• GET /fib/<number>: Given a number, find all combinations of fibonacci number that add up to
that particular number.

Remember, the fibonacci sequence is being calculated as follows: fn = fn−1 +fn−2∀n > 2; with the first
two numbers being f1 = f2 = 1 are excluded from the sequence, hence your f1 = 2.

Example for »/fib/11« the response will be a list of all possible combinations with a status code 200.
[ [2, 2, 2, 2, 3], [2, 2, 2, 5], [2, 3, 3, 3], [3, 3, 5], [8, 3] ]

• GET/health: Return health information about the service. Definition of »healt check« is up to you.
You can use any framework you like. We recommend using Flask.

What is important to us:
• code efficiency and speed
• code structure and cleanliness (a solid bet is to follow the S.O.L.I.D principles ;)
• code testability
• correctness of the result
• bonus points achieved

Optional Bonus Points
Feel free to do as much of the bonus points as you can. You can choose the order yourself.
• Write tests where it makes sense to you.
• Log the requests/responses being made to /fib in a database of your choice.
• Caching layer to avoid recalculating of Fibonacci sequences.
• Basic benchmarking to see how you code preform.
• Setup tox to test your project with several python versions.
• Dockerize your service.

Tip: Choose early what bonus points you want to take on

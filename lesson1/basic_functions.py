"""This is a file that explains how to create understand some simple
programming concepts in Python.  We will look at the idea of a
variable, a type, and a function

A variable is a _thing_ in a programming language that can hold a
value. An example of this is below

"""

my_favorite_number = 17


"""The name of the variable is my_favorite_number.  It has the _value_
the integer 17.
 
Notice how I didn't name the variable something like x or var.
There's a reason from that.  People who give variables names like that
are evil and should be slapped in the face repeatedly until they stop
doing so.  It is important to name your variables descriptively, so
that other people who read your code understand how you are using
them.

While it is not necessary for the computer, in Python it is
considered good coding practice to name your variables in all
lowercase with underscores separating words.  Other languages are
different.  For example, in Java one would use a naming convention
named camelCase, and the most common way to write that same variable
name would be as myFavoriteNumber instead of my_favorite_number.

Here's another variable.

"""

my_first_name = "Ian"

"""In this case I again descriptively named the variable.  This time
though the value of the variable was a string, a bunch of characters
in a row.  In Python we create these sorts of strings by enclosing our
characters in either single or double quotes.  I chose to use double
quotes and wrote "Ian" but I could have equivalently written 'Ian'.
It makes no difference.  Some companies have style guides for their
coders that tell them which one they prefer.

Lets move on to the second next most important idea in programming, a
function. A function is a named procedure that your overall program
can carry out.  Like variables, they should be named descriptively.
People who give their functions names like g or func deserve to have
their feet chewed off by rabid bears.  Lets write a simple function
that does something to an integer.

"""

def add_five(my_number):
    output_number = my_number + 5
    return output_number

"""This function is really silly, but it shows what we need it to show.  We will break it down line by line.

Line 1:
def add_five(my_number):

Let's go word by word here.

The keyword "def" means that we are about to define a function. (The abbreciation def is, unsurprisingly, short for the word define.) 

Next, "add_five" is the name of the function that we're defining.  It
is a description of what the function will do (it adds five to a
number), so no one else on your team who needs to use your code gets
confused.  Confusing other coders is something that everyone does, but
we want to do it as little as humanly possible.  I'd rather have a
decent, clear coder on my team than an awesome confusing one.

The important thing is actually the set of parentheses "(" and ")".  In Python the parentheses after that name of a function tell you that you are talking about the functions 'arguments' which is a fancy way of saying its inputs.  Since there is only one thing inside the parentheses, our function only needs one argument (aka input). 

The name of that argument is "my_number".  Again I have named this descriptively.  The name "my_number" is a hint to anyone using the function that the argument should be a number.  You probably won't get something that works correctly if you try to input a string or list instead.

The final thing on the line is the colon ":".  The colon character means that we're ready to start actually saying what the function does.

"""

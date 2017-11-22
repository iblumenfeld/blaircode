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

"""This function is really silly, but it shows what we need it to
show.  We will break it down line by line.

Line 1:
def add_five(my_number):

Let's go word by word here.

The keyword "def" means that we are about to define a function. (The
abreviation def is, unsurprisingly, short for the word define.)

Next, "add_five" is the name of the function that we're defining.  It
is a description of what the function will do (it adds five to a
number), so no one else on your team who needs to use your code gets
confused.  Confusing other coders is something that everyone does, but
we want to do it as little as humanly possible.  I'd rather have a
decent, clear coder on my team than an awesome confusing one.

The important thing is actually the set of parentheses "(" and ")".
In Python the parentheses after that name of a function tell you that
you are talking about the functions 'arguments' which is a fancy way
of saying its inputs.  Since there is only one thing inside the
parentheses, our function only needs one argument (aka input).  If
there were more than one argument, they would each have different
names, and those names should be separated by commas. 

The name of that argument is "my_number".  Again I have named this
descriptively.  The name "my_number" is a hint to anyone using the
function that the argument should be a number.  You probably won't get
something that works correctly if you try to input a string or list
instead.

The final thing on the line is the colon ":".  The colon character
means that we're ready to start actually saying what the function
does.

Now lets move on to the next line:
    output_number = my_number + 5

The first thing to note here is that the line is indented.  Python is
a very weird language in one important respect.  It is what we call
"white space sensitive."  Most languages don't care about spaces and
tabs.  Some don't even care about new lines.  Python cares about
these.  A lot.  By indenting underneath the def line of a function,
Python knows that you are describing the actions of that functions.
When you are no longer indented, it knows that you are done.

Lets take the rest of the line in parts again.

First, look at "output_number".  This is the name of a new variable.
Note the descriptive name.  It is a number and we will output it.  An
important point about output_number is that it is first named or
"declared" inside the definition of a function.  A variable like that
is called a "local variable" or "locally scoped variable".  This means
that it can only be "seen" inside the function.  Any use of it outside
the function will either result in a new variable being created or in
an error, depending on how you try to use it.

Next we have the "=" sign.  It's important to understand that in
coding there are two ways you can use that equals character.  The
first is the one we have here.  This one is the single "=" called
"assignent."  This "=" performs an action.  It takes a variable on the
left side and _assigns_ it the value on the right side.  So if when I
write 'output_numer =' it means that I am going to set the variable
output_number to whatever is on the right side of the equals sign.

The second version of equals is written == and is called the
double-equals or logical-equals.  Instead of being an assignment
operator it is a _comparison_ operator.  If I write 'x == y' I am
actually asking the program the question "Does x equal y?"  The answer
is either True or False.  Neither x nor y will get changed by the ==
operator.

It is important to know the difference between theses.  Confusing them
is a very common problem for beginner programmers.

The next part of the line "my_number + 5" says what we should assign
to output_number.  Namely, we say that we are making the value of
output_number the value of the argument my_number plus 5.

The next line is:
    return output_number

Note that this line is again indented.  The indentation indicates, as
before that this is part of the definition of the function add_five

The first word here is "return".  The keyword return says "whatever is
after this is what the function will evaluate to when called."
Basically it means that when you see the function inside a program,
Python will compute whatever it returns and then the expression by
that.  In this case we simply return the value of the local variable
output_number.

Now lets look at how this function might be called.

"""

print(add_five(12))

"""This line has calls the special built-in print function to output
whatever it's argument is to the screen.  In this case the argument of
print is add_five(12).  Now how does python figure out what that is?

Python sees add_five(12).  The first thing it does is look to see if
add_five is a function that you've definied somewhere.  It is!  Now it
looks to see how many arguments it needs.  It turns out that it needs
only 1 argument.  It checks to make sure that you gave it the correct
number of argument, and you did!

Internally it knows that it's one argument is named my_number.  Since
you gave the value 12 as its argument it assigns the value 12 to
my_number.  This is basically the same as if at the beginning of the
function you had written the line "my_number = 12".

Now on the next line it sees:
   output_number = my_number + 5

Since my_number has been assigned the value 12, it pulls that
information from memory and actually reads it as: 
   output_number = 12 + 5

Python automatically will add 12 and 5 to get 17.  So it actually sees
    output_number = 17

Now it goes to the next line and sees:
    return output_number

It pulls the fact that output_number is assigned the value 17 out of
memory and actually sees:

    return 17

This means that it then replaces the add_five(12) by 17 in the line:
print(add_five(12))

and instead sees

print(17)

Which it then executes, printing the number 17 to the screen.

To see this happen, on the command line type:
python basic_functions.py

It will output the number 17 and then exit, since this document is
actually a program, but one that just defines add_five and then has
the above print statement.

Thus ends lesson 1.

Exercises below:

"""
# Any line following the '#' character is a comment.  It won't be
# executed.  All the exercises are written in comments.  You should
# type them WITHOUT comments below the comment.

# Exercise 1: Define a function named double_and_add that takes two
# arguments. The two arguments are numbers.  It should output one
# number that is the sum of two times the first argument plus the
# second argument.  Give your variables good names.  Keep trying until
# you can get it to work.  If you need to, reread the doc-strings as
# many times as you need to.  Only ask for help if you need to well
# and truly give up.

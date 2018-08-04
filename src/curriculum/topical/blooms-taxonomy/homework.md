# Classification according to Bloom's taxonomy

Bloom's taxonomy is one of the most widely-known models of learning. It divides cognitive processes into six distinct levels:

* **Remember:** To rotely memorize information. _Example: Listing Python's primitive types._
* **Understand:** To grasp a concept well enough that you can say it in your own words. _Example: Explaining how recursion works on a high level._
* **Apply:** To solve a new problem using information and strategies you've been taught. _Example: Writing a recursive solution to `fibonacci(n)`, when you've already learned what recursion is and seen an example like `factorial(n)`._
* **Analyze:** To break down information into constituent parts, identify structure, or contrast two bodies of information. _Example: Determine the base case in a mutually recursive function call, without carrying out the whole evaluation process._
* **Evaluate:** To analyze a body of information, and then make a judgement call about it. _Example: To claim whether a solution to a problem has a "good" asymptotic running time, and justify your answer._
* **Create:** To evaluate a body of information, and then improve upon it. _Example: To improve the asymptotic running time of a function._

Note that a problem may appear at different levels of the taxonomy for different students. Consider the two scenarios below.

1. A student has never learned asymptotic analysis. You ask them how many times the recursive `fibonacci` function will get invoked when you make the function call `fibonacci(n)`. The student will have to **analyze** the `fibonacci` function to determine the underlying structure of function calls.
2. A student has had significant experience with asymptotic analysis, and has seen many examples of recursive functions that grow exponentially. You ask them how many times the recursive `fibonacci` function will get invoked when you make the function call `fibonacci(n)`. The student will have to **apply** a procedure they're already familiar with.

Also keep in mind that problems high on the taxonomy are not necessarily hard, and problems low on the taxonomy are not necessarily easy. This is just a way of classifying problems. Both easy and hard ones can occur at any level.

For each level of Bloom's taxonomy, provide an example from a computer science class you teach. Also specify the student's prior knowledge base and why it's important. Justify all your answers in a few setences.

# Analyzing a problem with Bloom's taxonomy

In 2001 (the year, not the space odyssey), Bloom's taxonomy was revised to include another axis measuring the level of abstraction of the task at hand. These resources will explain how it works:

* [Iowa State's model of Bloom's revised taxonomy](http://www.celt.iastate.edu/wp-content/uploads/2015/09/RevisedBloomsHandout-1.pdf)
* [Iowa State's associated explanation of Bloom's revised taxonomy](http://www.celt.iastate.edu/teaching/effective-teaching-practices/revised-blooms-taxonomy/blooms-revised-taxonomy-model)

First pick a difficult problem from the class that you teach. You may refer to past discussions, past midterms, guerilla section worksheets, etc. In your homework submission please include a link to the question that you chose, and additionally copy / paste it for ease of reference.

For the question you selected, describe the necessary steps to solve it. Be as explicit as possible. Each step should be designed to gently guide a student toward the solution, rather than simply explaining the solution yourself. Look out for common questions or misconceptions that students might have regarding the question. Then, for each step of the solution, identify where it falls on the Bloom's revised taxonomy. Justify why you think your classification is correct. Here are some good examples from past iterations of this assignment:

* [Example 1](https://docs.google.com/document/d/1JmBzA8qTsLp0iX0-6X6L_CJIuQmAqfX3t6SOWq_SbCg/edit?usp=sharing)
* [Example 2](https://docs.google.com/document/d/1R_uXY24GkAR4EswJaJFk7ffmKG3SepfXGs6eWWAitZs/edit?usp=sharing)
* [Example 3](https://docs.google.com/document/d/1dIQ0feab7_5Lc8-ALGK0yuSJjwtNYA_uwOHWAw1usAI/edit?usp=sharing)

You shouldn't make yours exactly like these, but hopefully they give you an idea of what we expect.
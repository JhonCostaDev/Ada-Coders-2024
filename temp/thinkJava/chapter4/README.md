Chapter 4 - Methods and Testing

```java
public static void main (String [] args) {
	System.out.println("First line.");

	newLine();

	System.out.println("Second line.");
}


public class void newLine(){
	System.out.println(); //
}
```
In this example, the newLine and main methods are both public, which means they can be 
**invoked** (or called) from the other classes. And they are both void, which means that they 
don't return a result.. 


## FLOW OF EXECUTION
When you look at a class definition that contains several mehods, it is tempting to read
it from top to bottom. Bt that is not the **flow of execution**, ot the order the program 
actually runs. The NewLine program runs methods in the opposite order than they are listed.

Programs always begin at the first statement of main, regardless of where it is in the source
file. Statement are executed one at a time, in order, until you reach a method invocation, 
which you can thihk of as a detour. Instead of going to the next statement, you jump to the 
first line of the invoked method, execute all the statement there, and then come back and 
pick up the exactly where you left off. 

## PARAMETERS AND ARGUMENTS
Some of the methods we have used require **arguments**, which are the values you provide in 
parentheses when you invoke the method.


## MATH METHODS

You don't always have to write new methods to get work done. As a reminder, the Java library 
contains thousands of classes you can use. 

```java
double root = Math.sqrt(17.0);
double angle = 1.5;
double height = Math.sin(angle);
double degrees = 90;
double angle2 = degrees / 180 * Math.PI;
double x = Math.pow(2.0, 10.0);
```

## RETURN VALUES
When you invoke a void method, the invocation is usually on a line all by itself.
```java
printTime(hour + 1, 0);
```
When you invoke a value-returning method, you have to do something with the return value.
We usually assign it ot a variable oruse it as part of an expression, like this:

```java
	double erro = Math.abs(expect - actual); 
```

## INCREMENTAL DEVELOPMENT

* Start with a working program and make small, incremental changes. At any point, if there
is an erro, you will know where to look.

* Use variables to hold intermediate values so you can check them, either wth print statement
or by using a debugger.

* Once the program is working, you can consolidade multiple statement into compound expressions
(but only if it does not make the program more difficult to read).

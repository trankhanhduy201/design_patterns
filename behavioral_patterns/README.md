# Behavioral Patterns

Behavioral patterns focus on how objects communicate and collaborate to get things done.

---

## Chain of Responsitory Pattern
It is useful because it allows you to execute multiple sequential behaviors where each behavior triggers the next one, without behaviors knowing about each other — leading to loose coupling, flexibility, and extensibility.

## Strategy Pattern
The Strategy Pattern is used when you have multiple ways (algorithms or behaviors) to perform a task, and you want to switch between them easily at runtime without changing the main code. This makes the algorithms interchangeable and keeps your code flexible and clean by separating each algorithm into its own class.

## Template Method Pattern
The Template Method Pattern is used when you want to define the overall structure of an algorithm once but allow subclasses to override and customize specific steps without changing its overall structure.
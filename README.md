# Design Patterns

Design patterns are reusable solutions to common problems in software design. They are categorized into three main types: Creational, Structural, and Behavioral patterns.

---

## Creational Patterns

Creational patterns provide strategic ways to create objects without hard-coding their types.

### Abstract Factory Pattern
The Abstract Factory Pattern provides an interface for creating families of related objects without specifying their concrete classes.

### Builder Pattern
The Builder Pattern is used to break down the construction of a complex object into manageable steps, enabling different configurations of the same object using the same construction process.

### Factory Pattern
The Factory Pattern lets you create objects without specifying their exact class by using a common interface and delegating the creation to a separate factory. It centralizes object creation based on input or configuration.

---

## Structural Patterns

Structural patterns help organize code by showing how objects can work together.

### Bridge Pattern
The Bridge Pattern focuses on decoupling an abstraction from its implementation to allow them to vary independently without affecting each other. The abstraction and implementation work together through a shared interface without knowing the details of the other. The abstraction holds a reference to the implementation’s interface.

### Facade Pattern
The Facade Pattern provides a simple interface that hides the complexity of a larger system and makes it easier to use.

### Adapter Pattern
The Adapter Pattern is used to make two incompatible interfaces work together by converting one interface into another that the client expects. This is achieved by wrapping an incompatible component inside a new adapter class that implements the compatible interface.

### Decorator Pattern
The Decorator Pattern is used to dynamically add new behaviors or responsibilities to individual objects at runtime without modifying their existing code or affecting other objects. This is done by wrapping them with decorator classes that implement the same interface.

### Proxy Pattern
The Proxy Pattern provides a substitute object that controls access to a real object, managing its creation or usage without changing its interface.

#### Proxy Pattern vs Decorator Pattern
- **Decorator Pattern**: Focuses on adding new behaviors or responsibilities to an object dynamically.
- **Proxy Pattern**: Focuses on controlling access to an object, often managing its creation or usage without changing its interface.

### Composite Pattern
The Composite Pattern allows you to build a collection-like structure where you can group child components and treat them in the same way as individual ones.

---

## Behavioral Patterns

Behavioral patterns focus on how objects communicate and collaborate to get things done.

## Chain of Responsitory Pattern
It is useful because it allows you to execute multiple sequential behaviors where each behavior triggers the next one, without behaviors knowing about each other — leading to loose coupling, flexibility, and extensibility.

### Strategy Pattern
The Strategy Pattern is used when you have multiple ways (algorithms or behaviors) to perform a task, and you want to switch between them easily at runtime without changing the main code. This makes the algorithms interchangeable and keeps your code flexible and clean by separating each algorithm into its own class.

### Template Method Pattern
The Template Method Pattern is used when you want to define the overall structure of an algorithm once but allow subclasses to override and customize specific steps without changing its overall structure.
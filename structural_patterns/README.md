# Structural Patterns

Structural patterns help organize code by showing how objects can work together.

---

## Bridge Pattern
The Bridge Pattern focuses on decoupling an abstraction from its implementation to allow them to vary independently without affecting each other. The abstraction and implementation work together through a shared interface without knowing the details of the other. The abstraction holds a reference to the implementation’s interface.

## Facade Pattern
The Facade Pattern provides a simple interface that hides the complexity of a larger system and makes it easier to use.

## Adapter Pattern
The Adapter Pattern is used to make two incompatible interfaces work together by converting one interface into another that the client expects. This is achieved by wrapping an incompatible component inside a new adapter class that implements the compatible interface.

## Decorator Pattern
The Decorator Pattern is used to dynamically add new behaviors or responsibilities to individual objects at runtime without modifying their existing code or affecting other objects. This is done by wrapping them with decorator classes that implement the same interface.

## Proxy Pattern
The Proxy Pattern provides a substitute object that controls access to a real object, managing its creation or usage without changing its interface.

### Proxy Pattern vs Decorator Pattern
- **Decorator Pattern**: Focuses on adding new behaviors or responsibilities to an object dynamically.
- **Proxy Pattern**: Focuses on controlling access to an object, often managing its creation or usage without changing its interface.

## Composite Pattern
The Composite Pattern allows you to build a collection-like structure where you can group child components and treat them in the same way as individual ones.
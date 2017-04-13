# Java Access Modifier
* Visible to the package, default. No modifers needed
* Visible to class only (private)
* Visible to the world (public)
* Visible to the package and all related subclasses (protected)

# Non Access Modifier
* 'static' modifier for creating methods and variables
  * variable: one copy for any instances created for class
  * method: exist independently for any instances
* 'final' modifier for finalizing the implementation of classes, methods, and variables
  * variable: explict initialize once, can never be reassign to refer
  * method: cannot be override by any subclasses
  * class: prevent class from being subclass
* 'abstract' mofieifer for creating abstract classes and methods
  * class: can never be instantiated
  * method: method declared without implementation (no body)
* 'synchronized' and 'volatile' modifier, used for threads
  * synchronized modifier: method can only be accessed by only one thread at a time
  * transient modifier: skip variable when serializing object containing it
  * volatile modifier: thread accessing the variable must always merge its own private copy with master copy in memory




# Local Variables
* declared within method, constructors or block
* access modifers cannot be used for local variable
* only visible within method, constructors or block
* implmented at stack level internally
* no default value so must be assign with initial value before use

# Instance Variables
* declared in class, but outside of method, constructors or any blocks
* created when an object is created with the use of 'new' and destroyed when object is destroyed
* holds value that is referenced by more than one method, constructors or block
* can be declared in class level before or after use
* access modifer can be given for instance variable
* visible to all methods, constructors and block in class (recommended to make these variables private to access level)
* have default values, num = 0, bool = false, char = null

# Class/Static Variables
* declare in class, outside of method, constructor, block but with 'static' key word
* only one copy for each variable per class regardless of how many objects are created
* rarely used except for constants
* visibility similar to instance but normally public
* default values are same with instance variable
* when declaring as 'public static final' names must be all upper case

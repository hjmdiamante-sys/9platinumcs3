# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation can be used by keeping each product’s information, such as its name, price, and quantity, inside a Product object. Methods such as addStock() and sellItem() can be used to change the quantity instead of changing it directly. This keeps the product data organized and prevents other parts of the program from changing important values incorrectly.

### 2. Abstraction
Abstraction can make the inventory system easier to use by hiding complicated processes behind simple methods. For example, a sellItem() method can automatically check whether there is enough stock, subtract the quantity sold, and calculate the total price. The cashier only needs to call the method without knowing every step happening inside it.

### 3. Inheritance
Inheritance can be used when the sari-sari store has different types of products that share common properties. A general Product class can contain properties such as name, price, and quantity, while classes such as FoodProduct and DrinkProduct can inherit these properties and add their own, such as expirationDate or size. This avoids repeating the same properties and methods for every type of product.

### 4. Polymorphism
Polymorphism allows different types of products to use the same method in different ways. Example, all products may have a displayInfo() method, but a FoodProduct could display its expiration date while a DrinkProduct could display its bottle size. This allows the inventory program to work with different product types using the same general method while still showing information specific to each product.

## Reflection
Through this activity, I learned that Object-Oriented Programming can make a sari-sari store inventory system easier to organize and manage. Instead of creating separate variables and functions for every product, OOP allows products to be represented as objects with their own properties and methods. I also understood how encapsulation, abstraction, inheritance, and polymorphism each help make a program more organized. 

const animal = {
  speak() {
    console.log("Animal sound");
  }
};

const dog = Object.create(animal);
dog.speak = function() {
  console.log("Woof!");
};

dog.speak(); // Output: Woof!
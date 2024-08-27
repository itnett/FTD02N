class Person {
    private String name;

    public Person(String name) {
        this.name = name;
    }

    public String greet() {
        return "Hello, " + this.name + "!";
    }
}

Person person = new Person("Alice");
System.out.println(person.greet());
const contacts = [];

     function addContact(name, email) {
       contacts.push({ name, email });
     }

     function listContacts() {
       contacts.forEach(contact => console.log(`${contact.name}: ${contact.email}`));
     }

     addContact("John Doe", "john.doe@example.com");
     listContacts();
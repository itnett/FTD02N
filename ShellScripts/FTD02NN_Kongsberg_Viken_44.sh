bash
  # Installer MongoDB
  sudo apt-get install -y mongodb

  # Start MongoDB-tjenesten
  sudo systemctl start mongodb

  # Koble til MongoDB
  mongo

  # Opprett en ny database og samling
  use ECommerceDB
  db.createCollection("products")

  # Sett inn dokumenter i samlingen
  db.products.insertMany([
      { "name": "Laptop", "price": 999.99, "stock": 50 },
      { "name": "Smartphone", "price": 499.99, "stock": 100 },
      { "name": "Headphones", "price": 29.99, "stock": 200 }
  ])

  # Finn alle produkter
  db.products.find()
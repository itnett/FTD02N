package com.example.demo;

   import org.springframework.web.bind.annotation.*;

   import java.util.ArrayList;
   import java.util.List;

   @RestController
   @RequestMapping("/api/items")
   public class ItemController {

       private List<Item> items = new ArrayList<>();

       @GetMapping
       public List<Item> getItems() {
           return items;
       }

       @PostMapping
       public Item addItem(@RequestBody Item item) {
           items.add(item);
           return item;
       }

       @DeleteMapping("/{id}")
       public void deleteItem(@PathVariable String id) {
           items.removeIf(item -> item.getId().equals(id));
       }
   }
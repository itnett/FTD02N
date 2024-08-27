<?php
   header("Access-Control-Allow-Origin: *");
   header("Access-Control-Allow-Methods: GET, POST, DELETE");
   header("Access-Control-Allow-Headers: Content-Type");

   $data = json_decode(file_get_contents("php://input"));

   $file = 'items.json';

   if (!file_exists($file)) {
       file_put_contents($file, json_encode([]));
   }

   $items = json_decode(file_get_contents($file), true);

   if ($_SERVER['REQUEST_METHOD'] === 'GET') {
       echo json_encode($items);
   } elseif ($_SERVER['REQUEST_METHOD'] === 'POST') {
       $newItem = ['id' => $data->id, 'name' => $data->name];
       $items[] = $newItem;
       file_put_contents($file, json_encode($items));
       echo json_encode($newItem);
   } elseif ($_SERVER['REQUEST_METHOD'] === 'DELETE') {
       $id = basename($_SERVER['REQUEST_URI']);
       $items = array_filter($items, function($item) use ($id) {
           return $item['id'] !== $id;
       });
       file_put_contents($file, json_encode($items));
   }
   ?>
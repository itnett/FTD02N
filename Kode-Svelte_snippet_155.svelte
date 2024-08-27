<script>
     let username = '';
     let password = '';

     function login() {
       if (username && password) {
         // Handle login
       } else {
         alert('Please fill in all fields');
       }
     }
   </script>

   <main>
     <h1>Login</h1>
     <input type="text" placeholder="Username" bind:value={username} />
     <input type="password" placeholder="Password" bind:value={password} />
     <button on:click={login}>Login</button>
   </main>
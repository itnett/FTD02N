python
    from ipywidgets import HTML
    from IPython.display import display

    # Svelte-kode (i en egen fil eller streng)
    svelte_component = """
    <script>
      let count = 0;
      function increment() {
        count += 1;
      }
    </script>

    <button on:click={increment}>
      Clicked {count} {count === 1 ? 'time' : 'times'}
    </button>
    """

    # Vis Svelte-komponenten i Jupyter Notebook
    display(HTML(svelte_component))
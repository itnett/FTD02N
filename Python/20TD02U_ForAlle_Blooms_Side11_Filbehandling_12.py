python
   base_dir = '/sikret/område/'
   filbane = os.path.join(base_dir, os.path.normpath(bruker_input))

   if os.path.commonprefix([filbane, base_dir]) != base_dir:
       raise ValueError('Ugyldig filbane!')
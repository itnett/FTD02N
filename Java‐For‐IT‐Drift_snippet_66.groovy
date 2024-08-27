def listFiles(String dir) {
       new File(dir).eachFile { file ->
           println file.name
       }
   }

   listFiles('.')
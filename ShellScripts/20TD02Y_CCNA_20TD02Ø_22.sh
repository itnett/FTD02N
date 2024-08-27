shell
   echo '#!/bin/bash' > update.sh
   echo 'sudo apt update && sudo apt upgrade -y' >> update.sh
   chmod +x update.sh
   ./update.sh
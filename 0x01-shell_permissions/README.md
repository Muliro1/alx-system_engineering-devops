THIS IS A COLLECTION OF SCRIPTS TO PERFORM VAROIUS TASKS ON THE LINUX TERMINAL.

1. su Betty changes the user to Betty.
2. whoami prints the effective username of the current user.
3. groups prints all the groups that the user belongs to.
4. chown Betty hello changes ownership of the file hello to Betty
5. touch hello creates an empty file called hello.
6. chmod u+x hello gives x permission to the owner of the hello file.
7. chmod ugo+x add execute permission for everybody on the hello file.
8. chmod u+x,g+x,o+r hello
9. chmod 007 only other users permissions, nothing for owner nad group.
10. chmod 753.
11. chmod --reference-olleh hello Mirror's olleh's permissions to hello.
12. chmod -R ugo+X.
13. mkdir -m 751 mydir creates a directory with 751 permissions.
14. chgrp chool hello changes the owning group of the hello file to school.
15. chown vincent:staff . 

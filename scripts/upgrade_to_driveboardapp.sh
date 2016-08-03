#!/bin/bash

echo "Switching from LasaurApp to DriveboardApp ..."

update-rc.d -f lasaurapp.sh remove

cp driveboardapp.sh /etc/init.d/driveboardapp.sh
chmod 755 /etc/init.d/driveboardapp.sh
update-rc.d driveboardapp.sh defaults

echo "Done!"

# ethOS rig hashing monitor

ethOS python script to restart a rig if it stops hashing for more than 7 minutes.

## Motivation

From time to time I find that one of the GPUs in my rigs stops hashing and usually a restart takes care of the issue. I got tired of manually restarting the rig when noticing (Sometimes I wouldn't notice until after 5+ hours, because... you know... I sleep and stuff).

To make life simpler, I created this script and I no longer have to monitor my rigs anymore.

Hope it makes your life easy too!

## Getting Started

ethOS locally writes the statistics of the rig on a file located in "/var/run/ethos/stats.file". One of the properties written in that file is called "miner_hashes", which is a string that represents the hashing rate of each of the GPUs connected, in the form of:

```
"12.67 13.50 21.03 00.00" //For a rig with 4 GPUs, each number representing the hash-rate of each GPU
```

This script runs every 7 minutes with a cron job and if one of the GPUs is 00.00 (not hashing) it will restart the rig

### Installing

1.- Create a directory named "Rig-monitor" under /home/ethos/

```
cd /home/ethos/
mkdir Rig-monitor
```

2.- Place the "rig-monitor.py" script inside the created directory.

3.- Open a new terminal and enter:

```
crontab -e
```

4.- Edit the crontab by going all the way down (after the commented section), and type:

```
@reboot python /home/ethos/Rig-monitor/rig-monitor.py &
```

5.- Type "ctrl+X" to save the changes, then "Y" to confirm and "Enter" to go apply the changes.

6.- Enter "r" on the terminal to restart the rig

You're set!


## Author

**Pepe Ramirez** - [peperamirez89](https://github.com/peperamirez89)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
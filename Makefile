
init-service: cp-service enable start

cp-service:
	sudo cp co2_monitor.service /etc/systemd/system/co2_monitor.service

enable:
	sudo systemctl enable co2_monitor

start:
	sudo systemctl start co2_monitor

status:
	sudo systemctl status co2_monitor

restart:
	sudo systemctl restart co2_monitor

stop:
	sudo systemctl stop co2_monitor

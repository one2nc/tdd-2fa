launch:
	python server/controller.py

generate_otp:
	python device/device.py --device-id ${DEVICE_ID}

deps:
	pip install -r requirements.txt

test:
	python -m unittest -v

coverage:
	coverage run -m unittest -v

coverage_report:
	coverage report -m

validate:
	curl -XGET http://localhost:5000/validate/${DEVICE_ID} --header 'Content-Type: application/json' --data-raw '{ "OTP": ${OTP} }'

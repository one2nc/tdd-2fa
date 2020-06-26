# tdd-2fa

1. To run tests: `make test`
2. To get coverage report: `make coverage coverage_report`
3. To start server: `make launch`
4. To generate OTP for a device id: `make generate_otp DEVICE_ID=1`
5. To validate generated OTP against server: `make validate DEVICE_ID=1 OTP=<otp>`
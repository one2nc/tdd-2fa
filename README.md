# tdd-2fa

1. Install dependencies: `make deps`
2. To run tests: `make test`
3. To get coverage report: `make coverage coverage_report`
4. To start server: `make launch`
5. To generate OTP for a device id: `make generate_otp DEVICE_ID=1`
6. To validate generated OTP against server: `make validate DEVICE_ID=1 OTP=<otp>`
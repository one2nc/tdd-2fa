# tdd-2fa

1. Run linter: `make lint`
2. Install dependencies: `make deps`
3. To run tests: `make test`
4. To get coverage report: `make coverage coverage_report`
5. To start server: `make launch`
6. To generate OTP for a device id: `make generate_otp DEVICE_ID=1`
7. To validate generated OTP against server: `make validate DEVICE_ID=1 OTP=<otp>`
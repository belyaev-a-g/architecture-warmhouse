# Build stage
FROM golang:1.22-alpine AS builder

# Set working directory
WORKDIR /app

# Set proxy
RUN go env -w GOPROXY="http://172.16.0.250:4343"

# Прокси для HTTP/HTTPS
ENV HTTP_PROXY=http://172.16.0.250:4343
ENV HTTPS_PROXY=http://172.16.0.250:4343

# Прокси для Go modules
ENV GOPROXY=https://proxy.golang.org,direct

# Отключение проверки сертификатов (если прокси использует самоподписанные сертификаты)
ENV GIT_SSL_NO_VERIFY=1

# Copy the source code
COPY . .

# Build the application
RUN CGO_ENABLED=0 GOOS=linux go build -o temperature-client test.go 

# Runtime stage
FROM alpine:latest

# Прокси для HTTP/HTTPS
ENV HTTP_PROXY=http://172.16.0.250:4343
ENV HTTPS_PROXY=http://172.16.0.250:4343

# Install necessary runtime dependencies
RUN apk --no-cache add ca-certificates tzdata

# Add curl
RUN apk add curl

# Set working directory
WORKDIR /app

# Copy the binary from the builder stage
COPY --from=builder /app/temperature-client .

# Явно сбрасываем proxy переменные
ENV HTTP_PROXY=
ENV HTTPS_PROXY=
ENV http_proxy=
ENV https_proxy=

# Command to run the application
CMD ["./temperature-client"]

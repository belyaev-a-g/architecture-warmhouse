# Build stage
FROM golang:1.22-alpine AS builder

# Set working directory
WORKDIR /app

# Copy go.mod and go.sum files
COPY go.mod go.sum ./

# Set proxy
#RUN go env -w GOPROXY="http://172.16.0.250:4343"
# Прокси для HTTP/HTTPS
ENV HTTP_PROXY=http://172.16.0.250:4343
ENV HTTPS_PROXY=http://172.16.0.250:4343

# Прокси для Go modules
ENV GOPROXY=https://proxy.golang.org,direct

# Отключение проверки сертификатов (если прокси использует самоподписанные сертификаты)
ENV GIT_SSL_NO_VERIFY=1

# Download dependencies
RUN go mod download

# Copy the source code
COPY . .

# Build the application
RUN CGO_ENABLED=0 GOOS=linux go build -o smarthome

# Runtime stage
FROM alpine:latest

ENV HTTP_PROXY=http://172.16.0.250:4343
ENV HTTPS_PROXY=http://172.16.0.250:4343

# Install necessary runtime dependencies
RUN apk --no-cache add ca-certificates tzdata

# Add curl
RUN apk add curl

# Set working directory
WORKDIR /app

# Copy the binary from the builder stage
COPY --from=builder /app/smarthome .

# Unset proxy
RUN unset HTTP_PROXY
RUN unset HTTPS_PROXY

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["./smarthome"]

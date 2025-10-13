# Use Debian-based OpenJDK (has apt-get)
FROM openjdk:17-jdk-bullseye

# Install Maven and Git
RUN apt-get update && apt-get install -y \
    maven \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /workspace

# Keep container running
CMD ["bash"]

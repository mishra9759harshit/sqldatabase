# Use a base image
FROM python:3.10-slim

# Create a directory to store the ASCII art securely
RUN mkdir /ascii_art

# Add the ASCII art file to the container
COPY ascii_art.txt /ascii_art/

# Set the directory as read-only
RUN chmod 444 /ascii_art/ascii_art.txt

# Set working directory
WORKDIR /ascii_art

# Default command to run
CMD ["cat", "ascii_art.txt"]

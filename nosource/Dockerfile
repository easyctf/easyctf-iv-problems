FROM node:8.9.4

# Copy source code
COPY src /app

# Change working directory
WORKDIR /app

# Install dependencies
RUN npm install

# Expose API port to the outside
EXPOSE 80
ENV PORT 80

# Launch application
CMD ["npm","start"]

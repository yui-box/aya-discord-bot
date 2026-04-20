# claude-project-boilerplate

A minimal, reusable starter template for building Claude-powered applications and services.

## Features

- Standardized project structure for Claude-based projects
- Preconfigured environment variables for Claude API keys
- Example prompts and integration patterns
- Basic logging, error handling, and configuration setup
- Ready for extension into prototypes or production services

## Getting Started

1. Clone the repository:
   ```bash
   git clone git@github.com:AndreaSoto/claude-project-boilerplate.git
   cd claude-project-boilerplate
   ```

2. Install dependencies:
   ```bash
   # example for Node
   npm install
   ```

3. Configure environment:
   ```bash
   cp .env.example .env
   # fill in your Claude / API keys
   ```

4. Run the project:
   ```bash
   npm run dev
   ```

## Usage

- Use the included example scripts as a reference for calling Claude.
- Extend the handlers, routes, or agents to match your application needs.

## Project Structure

- `src/` – application code and Claude integration logic
- `config/` – configuration and environment handling
- `scripts/` – example scripts and utilities
- `tests/` – test setup and sample tests

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

## License

MITS
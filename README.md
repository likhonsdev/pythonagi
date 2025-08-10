# Python AGi: A Simple and Powerful AI Agent

![GitHub release (latest by date)](https://img.shields.io/github/v/release/likhonsdev/pythonagi)
![GitHub issues](https://img.shields.io/github/issues/likhonsdev/pythonagi)
![GitHub pull requests](https://img.shields.io/github/issues-pr/likhonsdev/pythonagi)
![GitHub stars](https://img.shields.io/github/stars/likhonsdev/pythonagi)
![GitHub forks](https://img.shields.io/github/forks/likhonsdev/pythonagi)

A simple yet powerful AI agent built with Python and Flask. This project provides a solid foundation for building and deploying your own AI-powered applications.

## Features

*   **Flask Backend**: A lightweight and flexible web framework for Python.
*   **Vercel Deployment**: Easily deploy your application to Vercel with the included `vercel.json` configuration.
*   **GitHub Actions**: Automated release workflow to streamline your development process.
*   **Docker Support**: Includes a `Dockerfile` for easy containerization.
*   **Extensible**: Designed to be easily extended with new features and capabilities.

## Getting Started

To get started with this project, follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/likhonsdev/pythonagi.git
    ```
2.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
3.  **Run the development server:**
    ```sh
    ./devserver.sh
    ```

## Docker

This project includes a `Dockerfile` for easy containerization.

1.  **Build the Docker image:**
    ```sh
    docker build -t pythonagi .
    ```
2.  **Run the Docker container:**
    ```sh
    docker run -p 80:80 pythonagi
    ```

## Deployment

This project is configured for easy deployment to Vercel. Simply connect your GitHub repository to Vercel and it will automatically build and deploy your application.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any feedback or suggestions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
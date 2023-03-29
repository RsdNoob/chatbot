# Chat-GPT Client

This is a sample web application built with Flask and Chat-GPT. The application allows users to chat with a legal advice bot powered by Chat-GPT.

## Features

- Set an API key for authentication
- Update the initial message shown in the chat
- View the message history

## Getting Started

To get started with the application, clone this repository to your local machine:

```
git clone https://github.com/your-username/chatgpt-client.git
```

Navigate to the cloned repository and create a docker image using the `Dockerfile`:

```
docker build -t your-image-name .
```

To run the application, execute the following command:

```
docker run -p 5000:5000 your-image-name
```

The application will be available at http://localhost:5000.

## Usage

### Setting the API Key
To use the application, you must set an API key for authentication. When you first open the application, you will be prompted to enter an API key.

Enter your API key and click the "Submit API Key" button. Once your API key has been authenticated, you will be able to use the application.

### Updating the Initial Message

The initial message shown in the chat can be updated by clicking the "Update Initial Message" button.

Enter your desired initial message and click the "Update Initial Message" button. The updated message will be shown in the chat history.

### Viewing the Message History

The message history can be viewed by scrolling through the chat history:

## Conclusion

This sample application demonstrates how to build a web-based chatbot client using Flask and Chat-GPT. It can be used as a starting point for building more complex chatbot applications.
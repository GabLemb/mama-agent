# Mama Agent

Mama Agent is a Django-based application that serves as a gateway for two main APIs: a message service and an Ollama service.

## Project Structure

- **gateway/**: Contains the Django project configuration (settings, urls, wsgi, etc).
- **message_app/**: Manages messaging functionality with models, views, and URLs.
- **ollama_app/**: Provides API endpoints and utility functions for the Ollama service.

## Getting Started

Follow these steps to set up the project locally:

1. **Clone the Repository**

   ```zsh
   git clone https://github.com/GabLembo/mama-agent.git
   cd mama-agent
   ```

2. **Set Up Virtual Environment**

   Using Python’s built-in venv module:

   ```zsh
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies**

   ```zsh
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```zsh
   python manage.py migrate
   ```

5. **Run the Development Server**

   ```zsh
   python manage.py runserver
   ```

## Example of usage

```
curl -X POST http://localhost:8000/api/message/send/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Are there pepperoni pizza?"}'
```

## Additional Information

- Update `/gateway/gateway/urls.py` to customize URL routing for your project.
- Explore the `message_app` and `ollama_app` folders for application-specific logic and endpoints.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

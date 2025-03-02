# Arabic to English Transformer

This project is a Streamlit application that translates Arabic text to English using a Seq2Seq trained transformer model for Nueral Machine Translation. The application provides an elegant user interface for users to input Arabic text and receive the corresponding English translation.

## Project Structure

```
Arabic-2-English-Transformer
├── app.py                  # Main entry point of the Streamlit application
├── models
│   └── model_loader.py     # Loads the trained model weights
├── utils
│   ├── preprocessing.py     # Preprocesses the Arabic text input
│   └── translation.py       # Contains the translation logic
├── assets
│   └── style.css           # CSS styles for the Streamlit application
├── requirements.txt         # Lists the dependencies required for the project
└── README.md                # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ali-aj/Arabic-2-English-Transformer.git
   cd Arabic-2-English-Transformer
   ```

2. **Install the required dependencies:**
   It is recommended to create a virtual environment before installing the dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage

- Open the application in your web browser.
- Input the Arabic text you wish to translate in the provided text box.
- Click the "Translate" button to see the English translation.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
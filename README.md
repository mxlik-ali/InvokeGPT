
# InvokeGPT - Your Coding Companion

Welcome to InvokeGPT, your versatile command-line interface (CLI) tool designed to enhance your coding experience. Whether you're debugging, seeking detailed code explanations, refactoring for improved readability, automating test generation, handling custom prompts, or resolving non-code-related terminal errors, InvokeGPT has got you covered. Additionally, it can generate a README file for your project.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Setup](#setup)
  - [OpenAI API Key](#1-openai-api-key)
  - [Alternative: gpt4free](#2-alternative-gpt4free)
  - [Verify Setup](#3-verify-setup)
  - [System Environment Variable](#system-environment-variable)
  - [Install Requirements](#install-requirements)
- [Usage](#usage)
- [File Processing](#file-processing)
- [Further Information](#further-information)

## Features

- **Code Error-Finding (`debug`):** Analyze and highlight errors in your code, providing repair suggestions.
- **Code Explanation:** Receive detailed explanations for your code, enhancing your understanding of its logic and functionality.
- **Code Refractoring (`refractor`):** Effortlessly refractor your code with clear insights into the changes made for improved readability and efficiency.
- **Test Generation (`addtest`):** Quickly add tests to your code using the ChatGPT-powered test generation feature.
- **Custom Prompts (`customprompts`):** Tailor your queries with custom prompts, allowing you to address specific coding concerns.
- **Terminal Error Resolution (`error`):** Solve non-code-related errors in the terminal, such as dependency issues or other problems affecting the development environment.

## How It Works

InvokeGPT utilizes the [gpt4free](https://github.com/xtekky/gpt4free) API, a third-party provider, and advanced natural language processing to deliver accurate and insightful feedback. Whether you're a beginner learning the ropes or an experienced developer seeking efficient code improvements, InvokeGPT is designed to be your coding companion.

---

## Setup

### 1. OpenAI API Key

Before diving into the rich features of InvokeGPT, ensure you have obtained your OpenAI API key. Sign up at [OpenAI](https://beta.openai.com/signup/) to acquire your key.

### 2. Alternative: gpt4free

Alternatively, if you prefer to use the [gpt4free](https://github.com/xtekky/gpt4free) API, follow these steps:

1. Download the provider's file from their [GitHub repository](https://github.com/xtekky/gpt4free). Refer to their documentation for instructions on obtaining the necessary credentials and setup details.

2. Set up a system environment variable for the provider's API key. The process may vary depending on the provider's documentation, so make sure to follow their guidelines.

#### Windows:

1. Right-click on the Start button and select "System."
2. Click on "Advanced system settings" on the left.
3. In the System Properties window, click "Environment Variables."
4. Under "System variables," find and select the "Path" variable, then click "Edit."
5. Click "New" and add the path to the directory containing the `invokegpt.bat` file.

   Example:
   ```
   C:\Path\To\InvokeGPT
   ```

6. Click "OK" to close each dialog.

#### MacOS/Linux:

1. Open a terminal window.

2. Open your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.) in a text editor, e.g.:
   ```bash
   nano ~/.bashrc
   ```

3. Add the following line at the end, replacing `/path/to/InvokeGPT` with the actual path to the directory containing the `invokegpt.sh` file:
   ```bash
   export PATH=$PATH:/path/to/InvokeGPT
   ```

4. Save the file and exit the text editor.

5. Restart your terminal or run the following command to apply the changes:
   ```bash
   source ~/.bashrc
   ```

### 3. Verify Setup

To ensure a successful setup, open a new command prompt or terminal window and run:

```bash
invokegpt --version
```

You should see the version information of InvokeGPT. If any issues arise, double-check your OpenAI API key or the credentials provided by the gpt4free API and the correctness of the system environment variable setup.

#### System Environment Variable

To set up the system environment variable for your OpenAI API key, follow the steps based on your operating system:

### Windows:

1. Right-click on the Start button and select "System."
2. Click on "Advanced system settings" on the left.
3. In the System Properties window, click "Environment Variables."
4. Under "System variables," find and select the "Path" variable, then click "Edit."
5. Click "New" and add the path to the directory containing the `invokegpt.bat` file.

   Example:
   ```
   C:\Path\To\InvokeGPT
   ```

6. Click "OK" to close each dialog.

### MacOS/Linux:

1. Open a terminal window.

2. Open your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.) in a text editor, e.g.:
   ```bash
   nano ~/.bashrc
   ```

3. Add the following line at the end, replacing `/path/to/InvokeGPT` with the

 actual path to the directory containing the `invokegpt.sh` file:
   ```bash
   export PATH=$PATH:/path/to/InvokeGPT
   ```

4. Save the file and exit the text editor.

5. Restart your terminal or run the following command to apply the changes:
   ```bash
   source ~/.bashrc
   ```

### Install Requirements

Before using InvokeGPT, make sure to install the required dependencies. Open a terminal or command prompt and navigate to the directory containing `requirements.txt`. Run the following command:

```bash
pip install -r requirements.txt
```

This will install all the necessary dependencies for InvokeGPT.

Now you're ready to choose between the OpenAI path or the gpt4free path for setting up InvokeGPT.

### Usage

To utilize InvokeGPT, run the following command in your terminal or command prompt:

```bash
invokegpt chatgpt [keyword] [file_name]
```

Replace `[keyword]` with one of the following options:
- `debug`: Analyze and highlight errors in your code, providing repair suggestions.
- `refactor`: Effortlessly refactor your code with clear insights into the changes made.
- `addtest`: Quickly add tests to your code using the ChatGPT-powered test generation feature.
- `prompts`: Tailor your queries with custom prompts, allowing you to address specific coding concerns.
- `error`: Solve non-code-related errors in the terminal, such as dependency issues or other problems affecting the development environment.

Replace `[file_name]` with the name of the file you want to process.

#### Example:

```bash
invokegpt chatgpt debug my_code.py
```

#### Keyword Options:

| Keyword   | Description                                                                                     |
|-----------|-------------------------------------------------------------------------------------------------|
| `debug`   | Analyze and highlight errors in the code, providing repair suggestions.                         |
| `refractor`| Refactor the code, with clear insights into the changes made for improved readability.          |
| `addtest` | Generate tests for the code using ChatGPT, helping you enhance the test coverage of your code.   |
| `customprompts` | Use custom prompts to address specific coding concerns, allowing you to tailor your queries.     |
| `error`   | Solve non-code-related errors in the terminal, such as dependency issues or other problems.     |

#### File Processing:

After using the `debug` or `refactor` keyword, the changes are made directly into your current file (`[file_name]`).

Now you're all set to harness the power of InvokeGPT for debugging, refactoring, resolving terminal errors, and more in your coding projects!

---

## Further Information

For additional details, tips, and updates, refer to the [official documentation](https://github.com/mxlik-ali/InvokeGPT) of InvokeGPT. If you encounter any issues or have questions, feel free to reach out to the [community](https://github.com/mxlik-ali/InvokeGPT/discussions).

Happy coding with InvokeGPT!
